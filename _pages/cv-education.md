---
layout: single
title: "Education"
permalink: /cv/education/
author_profile: true
---

{% assign education = site.data.cv_details.education %}
{% if education and education.size > 0 %}
  {% for e in education %}
<div style="margin-bottom:1.4em;">
  <span style="color:var(--global-text-color-light); font-size:0.85em;">{{ e.year }}</span><br>
  <strong>{{ e.degree }}, {{ e.field }}</strong><br>
  <em>{{ e.institution }}{% if e.city %}, {{ e.city }}{% endif %}</em>
  {% if e.thesis and e.thesis != "" %}
  <br><span style="font-size:0.9em;">Thesis: <em>{{ e.thesis }}</em></span>
  {% endif %}
  {% if e.supervisor and e.supervisor != "" %}
  <br><span style="font-size:0.9em;">Supervisor: {{ e.supervisor }}</span>
  {% endif %}
</div>
  {% endfor %}
{% else %}
*To be populated — edit `_data/cv_details.yml`.*
{% endif %}

[← Back to CV](/cv/)
