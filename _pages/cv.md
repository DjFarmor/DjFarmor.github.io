---
layout: single
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<style>
.cv-download-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7em;
  margin-bottom: 1.6em;
}
.cv-btn {
  display: inline-block;
  padding: 0.4em 1em;
  border: 1px solid var(--global-border-color);
  border-radius: 4px;
  font-size: 0.88em;
  text-decoration: none !important;
  color: var(--global-text-color) !important;
  background: var(--global-bg-color);
  transition: background 0.15s, border-color 0.15s;
}
.cv-btn:hover {
  background: var(--global-border-color);
}
.cv-btn.primary {
  background: #2d5986;
  color: #fff !important;
  border-color: #2d5986;
}
.cv-btn.primary:hover { background: #1e3d5c; }

.cv-details-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5em;
  margin: 0.8em 0 1.4em;
  font-size: 0.85em;
}
.cv-details-row a {
  padding: 0.2em 0.7em;
  border: 1px solid var(--global-border-color);
  border-radius: 20px;
  text-decoration: none;
  color: var(--global-text-color-light);
}
.cv-details-row a:hover { color: var(--global-link-color-hover); border-color: currentColor; }

details summary {
  cursor: pointer;
  font-weight: 600;
  font-size: 0.95em;
  padding: 0.4em 0;
  color: var(--global-text-color-light);
  user-select: none;
}
details[open] summary { color: var(--global-text-color); }
</style>

<!-- ── Download buttons ──────────────────────────────────── -->
<div class="cv-download-row">
  <a class="cv-btn primary" href="/files/cv.pdf" target="_blank">↓ Full CV (PDF)</a>
  <a class="cv-btn" href="/files/cv-short.pdf" target="_blank">↓ Short CV (PDF)</a>
  <a class="cv-btn" href="/cv/visual/">📊 CV at a glance</a>
</div>

<!-- ── Details sub-pages ─────────────────────────────────── -->
<details>
<summary>Details</summary>
<div class="cv-details-row">
  <a href="/cv/education/">Education</a>
  <a href="/cv/employment/">Employment</a>
  <a href="/cv/grants/">Grants &amp; Stipends</a>
  <a href="/cv/awards/">Awards</a>
</div>
</details>

---

<!-- ── Embedded full CV ──────────────────────────────────── -->
<div style="width:100%; height:82vh; border:1px solid var(--global-border-color);
            border-radius:4px; overflow:hidden; margin-top:0.8em;">
  <iframe
    src="/files/cv.pdf"
    width="100%"
    height="100%"
    style="border:none;"
    title="Curriculum Vitae">
    <p>Your browser does not support inline PDFs.
       <a href="/files/cv.pdf">Download the CV here.</a></p>
  </iframe>
</div>
