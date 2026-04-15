#!/usr/bin/env python3
"""
generate_short_cv.py
Auto-generates files/cv-short.tex from Jekyll collection files and
_data/cv_details.yml.

Run from the repository root:
    python scripts/generate_short_cv.py
"""

import glob
import os
import re
import sys
from datetime import datetime

import yaml

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_frontmatter(filepath):
    """Return the YAML frontmatter dict of a Jekyll markdown file."""
    try:
        with open(filepath, encoding="utf-8") as fh:
            raw = fh.read()
    except OSError:
        return {}
    if not raw.startswith("---"):
        return {}
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def esc(s):
    """Escape special LaTeX characters in a string."""
    if s is None:
        return ""
    s = str(s)
    for ch, rep in [
        ("\\", r"\textbackslash{}"),
        ("&",  r"\&"),
        ("%",  r"\%"),
        ("$",  r"\$"),
        ("#",  r"\#"),
        ("_",  r"\_"),
        ("{",  r"\{"),
        ("}",  r"\}"),
        ("~",  r"\textasciitilde{}"),
        ("^",  r"\textasciicircum{}"),
    ]:
        s = s.replace(ch, rep)
    return s


def parse_date(val):
    """Return a sortable date string from various frontmatter formats."""
    if val is None:
        return "0000-01-01"
    if isinstance(val, datetime):
        return val.strftime("%Y-%m-%d")
    s = str(val).strip()
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(s[:len(fmt)], fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return s[:10] if len(s) >= 4 else "0000-01-01"


def year_of(val):
    return parse_date(val)[:4]


# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------

def load_collection(pattern):
    items = []
    for path in glob.glob(pattern):
        fm = read_frontmatter(path)
        if fm:
            fm["_path"] = path
            items.append(fm)
    return items


def load_cv_details():
    try:
        with open("_data/cv_details.yml", encoding="utf-8") as fh:
            return yaml.safe_load(fh) or {}
    except OSError:
        return {}


# ---------------------------------------------------------------------------
# LaTeX building blocks
# ---------------------------------------------------------------------------

PREAMBLE = r"""
\documentclass[10pt, a4paper]{article}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=1.8cm, top=2cm, bottom=2cm]{geometry}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{parskip}
\usepackage{microtype}
\usepackage{ifthen}

\definecolor{accent}{HTML}{2d5986}
\definecolor{lightgray}{gray}{0.5}

\hypersetup{
  colorlinks = true,
  urlcolor   = accent,
  linkcolor  = accent,
  citecolor  = accent,
  pdfauthor  = {Andre Sevenius Nilsen},
  pdftitle   = {Short CV -- Andre Sevenius Nilsen},
}

\titleformat{\section}{\large\bfseries\color{accent}}{}{0em}{}%
  [\vspace{-0.4em}\rule{\linewidth}{0.5pt}]
\titlespacing{\section}{0pt}{1.2em}{0.5em}

\newcommand{\cventry}[4]{%
  \noindent
  \begin{minipage}[t]{2.5cm}\small\color{lightgray}#1\end{minipage}%
  \hspace{0.4em}%
  \begin{minipage}[t]{\dimexpr\textwidth-2.9cm\relax}%
    \textbf{#2}%
    \ifthenelse{\equal{#3}{}}{}{\newline\textit{#3}}%
    \ifthenelse{\equal{#4}{}}{}{\newline\small #4}%
  \end{minipage}%
  \par\vspace{0.4em}%
}

\newcommand{\cvitem}[2]{%
  \noindent
  \begin{minipage}[t]{2.5cm}\small\color{lightgray}#1\end{minipage}%
  \hspace{0.4em}%
  \begin{minipage}[t]{\dimexpr\textwidth-2.9cm\relax}#2\end{minipage}%
  \par\vspace{0.3em}%
}
""".lstrip()

HEADER = r"""
\begin{document}
\pagestyle{plain}

\begin{center}
  {\huge\bfseries Andr\'e Sevenius Nilsen}\\[0.4em]
  {\normalsize
    Oslo, Norway
    \quad\textbar\quad
    \href{mailto:sevenius.nilsen@gmail.com}{sevenius.nilsen@gmail.com}
    \quad\textbar\quad
    \href{https://djfarmor.github.io}{djfarmor.github.io}%
  }
\end{center}

\vspace{0.6em}
""".lstrip()


def section_employment(employment):
    if not employment:
        return ""
    lines = [r"\section{Employment}", ""]
    for e in employment:
        start = esc(e.get("start", ""))
        end   = esc(e.get("end", ""))
        period = f"{start}--{end}" if end else str(start)
        lines.append(
            r"\cventry{%s}{%s}{%s}{%s}" % (
                period,
                esc(e.get("title", "")),
                esc(f"{e.get('institution','')}, {e.get('city','')}".strip(", ")),
                esc(e.get("description", "")),
            )
        )
    return "\n".join(lines) + "\n"


def section_education(education):
    if not education:
        return ""
    lines = [r"\section{Education}", ""]
    for e in education:
        notes = []
        if e.get("thesis"):
            notes.append(f"Thesis: \\textit{{{esc(e['thesis'])}}}")
        if e.get("supervisor"):
            notes.append(f"Supervisor: {esc(e['supervisor'])}")
        lines.append(
            r"\cventry{%s}{%s, %s}{%s}{%s}" % (
                esc(e.get("year", "")),
                esc(e.get("degree", "")),
                esc(e.get("field", "")),
                esc(f"{e.get('institution','')}, {e.get('city','')}".strip(", ")),
                ". ".join(notes),
            )
        )
    return "\n".join(lines) + "\n"


def section_publications(pubs, n=10):
    if not pubs:
        return ""
    sorted_pubs = sorted(pubs, key=lambda x: parse_date(x.get("date")), reverse=True)
    selected = sorted_pubs[:n]
    lines = [
        r"\section{Selected Publications (last %d)}" % len(selected),
        r"\begin{enumerate}[leftmargin=2em, label={[\arabic*]}, itemsep=0.25em]",
    ]
    for p in selected:
        citation = esc(p.get("citation", p.get("title", "Untitled")))
        url = p.get("paperurl", "")
        if url:
            citation += r"  \href{%s}{[link]}" % url
        lines.append(r"  \item " + citation)
    lines.append(r"\end{enumerate}")
    return "\n".join(lines) + "\n"


def section_talks(talks):
    if not talks:
        return ""
    sorted_talks = sorted(talks, key=lambda x: parse_date(x.get("date")), reverse=True)
    lines = [r"\section{Talks \& Presentations}", ""]
    for t in sorted_talks[:8]:  # cap at 8
        venue = esc(t.get("venue", ""))
        loc   = esc(t.get("location", ""))
        place = f"{venue}, {loc}".strip(", ") if loc else venue
        lines.append(r"\cventry{%s}{%s}{%s}{}" % (
            year_of(t.get("date")),
            esc(t.get("title", "Untitled")),
            place,
        ))
    total = len(sorted_talks)
    if total > 8:
        lines.append(r"\noindent\small (\textit{%d talks total; full list at \href{https://djfarmor.github.io/talks/}{djfarmor.github.io/talks}})" % total)
    return "\n".join(lines) + "\n"


def section_teaching(teaching):
    if not teaching:
        return ""
    sorted_t = sorted(teaching, key=lambda x: parse_date(x.get("date")), reverse=True)
    lines = [r"\section{Teaching}", ""]
    for t in sorted_t:
        lines.append(r"\cventry{%s}{%s}{%s}{}" % (
            year_of(t.get("date")),
            esc(t.get("title", "Untitled")),
            esc(t.get("venue", "")),
        ))
    return "\n".join(lines) + "\n"


def section_grants(grants):
    if not grants:
        return ""
    lines = [r"\section{Grants \& Stipends}", ""]
    for g in sorted(grants, key=lambda x: x.get("year", 0), reverse=True):
        amt = g.get("amount", "")
        cur = g.get("currency", "")
        note = f"{amt:,} {cur}".strip() if amt else ""
        lines.append(r"\cventry{%s}{%s}{%s}{%s}" % (
            esc(g.get("year", "")),
            esc(g.get("title", "")),
            esc(g.get("funder", "")),
            esc(note),
        ))
    return "\n".join(lines) + "\n"


def section_awards(awards):
    if not awards:
        return ""
    lines = [r"\section{Awards \& Honours}", ""]
    for a in sorted(awards, key=lambda x: x.get("year", 0), reverse=True):
        lines.append(r"\cventry{%s}{%s}{%s}{}" % (
            esc(a.get("year", "")),
            esc(a.get("title", "")),
            esc(a.get("institution", "")),
        ))
    return "\n".join(lines) + "\n"


def section_repos(repos):
    if not repos:
        return ""
    lines = [r"\section{Selected Software \& Repositories}", ""]
    for r in repos:
        url  = r.get("url", "")
        name = esc(r.get("name", ""))
        desc = esc(r.get("description", ""))
        if url:
            entry_title = r"\href{%s}{%s}" % (url, name)
        else:
            entry_title = name
        lines.append(r"\cventry{}{%s}{}{%s}" % (entry_title, desc))
    return "\n".join(lines) + "\n"


def section_skills(skills):
    if not skills:
        return ""
    lines = [r"\section{Skills}", ""]
    if skills.get("programming"):
        prog = ", ".join(esc(s["name"]) for s in skills["programming"])
        lines.append(r"\cvitem{Programming}{%s}" % prog)
    if skills.get("methods"):
        meth = ", ".join(esc(s["name"]) for s in skills["methods"])
        lines.append(r"\cvitem{Methods}{%s}" % meth)
    if skills.get("languages"):
        lang_parts = []
        for l in skills["languages"]:
            note = l.get("note", "")
            lang_parts.append(
                f"{esc(l['name'])} ({esc(note)})" if note else esc(l["name"])
            )
        lines.append(r"\cvitem{Languages}{%s}" % ", ".join(lang_parts))
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    details  = load_cv_details()
    pubs     = load_collection("_publications/*.md")
    talks    = load_collection("_talks/*.md")
    teaching = load_collection("_teaching/*.md")
    repos    = details.get("github_repos", [])

    sections = [
        PREAMBLE,
        HEADER,
        section_employment(details.get("employment", [])),
        section_education(details.get("education", [])),
        section_publications(pubs, n=10),
        section_talks(talks),
        section_teaching(teaching),
        section_grants(details.get("grants", [])),
        section_awards(details.get("awards", [])),
        section_repos(repos),
        section_skills(details.get("skills", {})),
        r"\end{document}",
    ]

    output = "\n".join(s for s in sections if s)
    out_path = os.path.join("files", "cv-short.tex")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(output)

    print(f"Generated {out_path}  ({len(pubs)} publications, "
          f"{len(talks)} talks, {len(teaching)} teaching entries)")


if __name__ == "__main__":
    main()
