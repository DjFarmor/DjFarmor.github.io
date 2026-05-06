---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

<style>
  /* ── Dirt-theme palette ────────────────────────────────────────────── */
  :root {
    --proj-bg          : #f3f3f3;
    --proj-bg-mid      : #ece9e0;
    --proj-bg-item     : #e9e6dc;
    --proj-border      : #e9dcbe;
    --proj-border-dark : #c9b98a;
    --proj-accent      : #b49368;
    --proj-text        : #343434;
    --proj-text-muted  : #8e8b82;
  }

  /* ── Status-level (outermost) ─────────────────────────────────────── */
  .proj-category {
    margin: 1.4em 0;
    border: 1px solid var(--proj-border-dark);
    border-radius: 4px;
    background: var(--proj-bg);
    overflow: hidden;
  }
  .proj-category > summary {
    cursor: pointer;
    list-style: none;
    display: flex;
    align-items: center;
    gap: 0.5em;
    padding: 0.75em 1em;
    font-size: 1.05em;
    font-weight: bold;
    color: var(--proj-text);
    background: var(--proj-bg);
    border-bottom: 1px solid transparent;
    user-select: none;
    transition: background 0.15s;
  }
  .proj-category > summary::-webkit-details-marker { display: none; }
  .proj-category > summary::before {
    content: "▶";
    font-size: 0.7em;
    transition: transform 0.2s;
    color: var(--proj-accent);
    display: inline-block;
  }
  .proj-category[open] > summary::before { transform: rotate(90deg); }
  .proj-category[open] > summary {
    border-bottom-color: var(--proj-border);
    background: var(--proj-bg-mid);
  }
  .proj-category > summary:hover { background: var(--proj-bg-mid); }

  .proj-category-body {
    padding: 0.75em 1em;
    display: flex;
    flex-direction: column;
    gap: 0.75em;
  }

  /* ── Individual project entries ───────────────────────────────────── */
  .proj-entry {
    border-left: 3px solid var(--proj-accent);
    background: var(--proj-bg-item);
    border-radius: 0 3px 3px 0;
    overflow: hidden;
  }
  .proj-entry > summary {
    cursor: pointer;
    list-style: none;
    padding: 0.6em 0.8em;
    user-select: none;
    display: grid;
    grid-template-areas:
      "title years"
      "excerpt excerpt";
    grid-template-columns: 1fr auto;
    gap: 0.15em 0.5em;
    align-items: baseline;
  }
  .proj-entry > summary::-webkit-details-marker { display: none; }
  .proj-entry > summary:hover { background: rgba(0,0,0,0.04); }

  .proj-entry-title {
    grid-area: title;
    font-weight: 600;
    font-size: 0.95em;
    color: var(--proj-text);
    line-height: 1.35;
  }
  .proj-entry-title::before {
    content: "▶";
    font-size: 0.6em;
    color: var(--proj-accent);
    transition: transform 0.2s;
    display: inline-block;
    margin-right: 0.4em;
    vertical-align: middle;
  }
  .proj-entry[open] > summary .proj-entry-title::before {
    transform: rotate(90deg);
  }
  .proj-entry-years {
    grid-area: years;
    font-size: 0.82em;
    font-style: italic;
    color: var(--proj-text-muted);
    text-align: right;
    white-space: nowrap;
  }
  .proj-entry-excerpt {
    grid-area: excerpt;
    font-size: 0.82em;
    color: var(--proj-text-muted);
    line-height: 1.4;
  }

  /* ── Expanded body ────────────────────────────────────────────────── */
  .proj-entry-body {
    padding: 0.6em 0.85em 0.85em;
    border-top: 1px solid var(--proj-border);
    font-size: 0.88em;
    color: var(--proj-text);
    line-height: 1.6;
  }
  .proj-entry-body p { margin: 0 0 0.5em; }
  .proj-entry-body ul { margin: 0.3em 0 0.5em 1.2em; }
  .proj-links a {
    display: inline-block;
    margin-right: 0.75em;
    margin-top: 0.5em;
    color: var(--proj-text);
    font-weight: 600;
    text-decoration: none;
    border-bottom: 1px solid var(--proj-accent);
    padding-bottom: 1px;
    transition: color 0.15s, border-color 0.15s;
  }
  .proj-links a:hover { color: var(--proj-accent); }

  .proj-count {
    font-size: 0.78em;
    font-weight: normal;
    color: var(--proj-text-muted);
    margin-left: 0.3em;
  }

  .proj-future-note {
    margin-top: 2em;
    padding: 0.75em 1em;
    border: 1px solid var(--proj-border);
    border-radius: 4px;
    background: var(--proj-bg);
    font-size: 0.9em;
    color: var(--proj-text-muted);
  }
  .proj-future-note a {
    color: var(--proj-text);
    font-weight: 600;
    border-bottom: 1px solid var(--proj-accent);
    text-decoration: none;
  }
  .proj-future-note a:hover { color: var(--proj-accent); }
</style>

{% assign all_projects = site.portfolio | sort: 'start_year' | reverse %}
{% assign current_projects = all_projects | where: 'status', 'current' %}
{% assign past_projects    = all_projects | where: 'status', 'past' %}

{% comment %}──────────────────────────────────────────────────────────────────
  CURRENT PROJECTS
──────────────────────────────────────────────────────────────────{% endcomment %}
{% if current_projects.size > 0 %}
<details class="proj-category" open>
  <summary>🔬 Current Projects <span class="proj-count">({{ current_projects.size }})</span></summary>
  <div class="proj-category-body">
    {% for project in current_projects %}
    <details class="proj-entry">
      <summary>
        <span class="proj-entry-title">{{ project.title }}</span>
        <span class="proj-entry-years">{{ project.start_year }}–{{ project.end_year }}</span>
        {% if project.excerpt %}<span class="proj-entry-excerpt">{{ project.excerpt }}</span>{% endif %}
      </summary>
      <div class="proj-entry-body">
        {{ project.content }}
        {% if project.project_url %}
        <div class="proj-links"><a href="{{ project.project_url }}" target="_blank" rel="noopener">Project page ↗</a></div>
        {% endif %}
      </div>
    </details>
    {% endfor %}
  </div>
</details>
{% endif %}

{% comment %}──────────────────────────────────────────────────────────────────
  PAST PROJECTS
──────────────────────────────────────────────────────────────────{% endcomment %}
{% if past_projects.size > 0 %}
<details class="proj-category" open>
  <summary>📁 Past Projects <span class="proj-count">({{ past_projects.size }})</span></summary>
  <div class="proj-category-body">
    {% for project in past_projects %}
    <details class="proj-entry">
      <summary>
        <span class="proj-entry-title">{{ project.title }}</span>
        <span class="proj-entry-years">{{ project.start_year }}–{{ project.end_year }}</span>
        {% if project.excerpt %}<span class="proj-entry-excerpt">{{ project.excerpt }}</span>{% endif %}
      </summary>
      <div class="proj-entry-body">
        {{ project.content }}
        {% if project.project_url %}
        <div class="proj-links"><a href="{{ project.project_url }}" target="_blank" rel="noopener">Project page ↗</a></div>
        {% endif %}
      </div>
    </details>
    {% endfor %}
  </div>
</details>
{% endif %}

<div class="proj-future-note">
  💡 <strong>Future projects:</strong> Planned and possible future research directions are described <a href="/projects/future/">on a separate page</a>.
</div>
