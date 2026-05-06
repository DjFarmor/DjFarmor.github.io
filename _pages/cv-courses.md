---
layout: single
title: "Courses & Training"
permalink: /cv/courses/
author_profile: true
---

Additional formal courses and training beyond the main degrees.

| Course | Institution | Year |
|---|---|---|
{% for c in site.data.cv_details.skills.courses %}| {{ c.name }} | {{ c.institution }} | {{ c.year }} |
{% endfor %}

[← Back to Skills](/cv/skills/)
