---
layout: single
title: "Awards & Honours"
permalink: /cv/awards/
author_profile: true
---

{% assign awards = site.data.cv_details.awards %}
{% if awards and awards.size > 0 %}
  {% for a in awards %}
<div style="margin-bottom:1.2em;">
  <span style="color:var(--global-text-color-light); font-size:0.85em;">{{ a.year }}</span><br>
  <strong>{{ a.title }}</strong><br>
  <em>{{ a.institution }}</em>
  {% if a.description and a.description != "" %}
  <br><span style="font-size:0.9em;">{{ a.description }}</span>
  {% endif %}
</div>
  {% endfor %}
{% else %}
*To be populated — edit `_data/cv_details.yml`.*
{% endif %}

[← Back to CV](/cv/)
