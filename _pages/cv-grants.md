---
layout: single
title: "Grants & Stipends"
permalink: /cv/grants/
author_profile: true
---

{% assign grants = site.data.cv_details.grants %}
{% if grants and grants.size > 0 %}

{% assign total = 0 %}
{% for g in grants %}{% assign total = total | plus: g.amount %}{% endfor %}

<p style="font-size:0.9em; color:var(--global-text-color-light);">
  {{ grants.size }} grant{% if grants.size != 1 %}s{% endif %} &mdash;
  total: {{ total | divided_by: 1000 }}k NOK
</p>

  {% for g in grants %}
<div style="margin-bottom:1.4em;">
  <span style="color:var(--global-text-color-light); font-size:0.85em;">{{ g.year }}</span><br>
  <strong>{{ g.title }}</strong><br>
  <em>{{ g.funder }}</em>
  {% if g.amount %}
  <br><span style="font-size:0.9em;">{{ g.amount | divided_by: 1000 }}k {{ g.currency }}</span>
  {% endif %}
  {% if g.description and g.description != "" %}
  <br><span style="font-size:0.9em;">{{ g.description }}</span>
  {% endif %}
</div>
  {% endfor %}
{% else %}
*To be populated — edit `_data/cv_details.yml`.*
{% endif %}

[← Back to CV](/cv/)
