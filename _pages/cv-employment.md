---
layout: single
title: "Employment"
permalink: /cv/employment/
author_profile: true
---

{% assign employment = site.data.cv_details.employment %}
{% if employment and employment.size > 0 %}
  {% for e in employment %}
<div style="margin-bottom:1.4em;">
  <span style="color:var(--global-text-color-light); font-size:0.85em;">
    {{ e.start }}{% if e.end %}–{{ e.end }}{% endif %}
  </span><br>
  <strong>{{ e.title }}</strong><br>
  <em>{{ e.institution }}{% if e.city %}, {{ e.city }}{% endif %}</em>
  {% if e.description %}<br><span style="font-size:0.9em;">{{ e.description }}</span>{% endif %}
</div>
  {% endfor %}
{% else %}
*To be populated — edit `_data/cv_details.yml`.*
{% endif %}

[← Back to CV](/cv/)
