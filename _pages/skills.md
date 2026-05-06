---
layout: single
title: "Skills"
permalink: /cv/skills/
author_profile: true
---

<style>
  .skill-section { margin-bottom: 2em; }
  .skill-section h3 { margin-bottom: 0.6em; font-size: 0.95em; color: var(--global-text-color-light); text-transform: uppercase; letter-spacing: 0.05em; }
  .skill-bar-row { display: flex; align-items: center; gap: 0.8em; margin-bottom: 0.45em; }
  .skill-label { width: 12em; font-size: 0.88em; flex-shrink: 0; color: var(--global-text-color); }
  .skill-track { flex: 1; height: 7px; background: var(--global-border-color); border-radius: 4px; overflow: hidden; }
  .skill-fill { height: 100%; background: #b49368; border-radius: 4px; }
  .skill-tags { display: flex; flex-wrap: wrap; gap: 0.4em; }
  .skill-tag { padding: 0.25em 0.7em; border: 1px solid var(--global-border-color); border-radius: 20px; font-size: 0.82em; color: var(--global-text-color-light); }
</style>

## Programming

<div class="skill-section">
{% for s in site.data.cv_details.skills.programming %}
<div class="skill-bar-row">
  <span class="skill-label">{{ s.name }}</span>
  <div class="skill-track"><div class="skill-fill" style="width:{{ s.level }}%"></div></div>
</div>
{% endfor %}
</div>

## Methods

<div class="skill-section">
{% for s in site.data.cv_details.skills.methods %}
<div class="skill-bar-row">
  <span class="skill-label">{{ s.name }}</span>
  <div class="skill-track"><div class="skill-fill" style="width:{{ s.level }}%"></div></div>
</div>
{% endfor %}
</div>

## Languages

<div class="skill-section">
{% for l in site.data.cv_details.skills.languages %}
<div class="skill-bar-row">
  <span class="skill-label">{{ l.name }}{% if l.note %} <span style="font-size:0.8em; color:var(--global-text-color-light);">({{ l.note }})</span>{% endif %}</span>
  <div class="skill-track"><div class="skill-fill" style="width:{{ l.level }}%"></div></div>
</div>
{% endfor %}
</div>

## Software

<div class="skill-section">
<div class="skill-tags">
{% for s in site.data.cv_details.skills.software %}
<span class="skill-tag">{{ s }}</span>
{% endfor %}
</div>
</div>

---

[Courses & training →](/cv/courses/)
