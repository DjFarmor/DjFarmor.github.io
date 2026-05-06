---
layout: single
title: "Future Projects"
permalink: /projects/future/
author_profile: true
---

Planned or possible research projects — ideas at various stages of development.

---

{% assign future_projects = site.portfolio | where: 'status', 'future' | sort: 'title' %}
{% if future_projects.size > 0 %}
  {% for project in future_projects %}
### {{ project.title }}

{{ project.content }}

  {% endfor %}
{% else %}
*Nothing listed yet.*
{% endif %}

---

[← Back to Projects](/projects/)
