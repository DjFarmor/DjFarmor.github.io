---
layout: single
title: "CV at a Glance"
permalink: /cv/visual/
author_profile: true
---

<style>
/* ── Layout ─────────────────────────────────────────────── */
.vis-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1.4em;
  margin: 1.4em 0 2em;
}
.vis-card {
  background: var(--global-bg-color);
  border: 1px solid var(--global-border-color);
  border-radius: 6px;
  padding: 1.1em 1.3em;
}
.vis-card h3 {
  margin: 0 0 0.7em;
  font-size: 0.85em;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--global-text-color-light);
  border-bottom: 1px solid var(--global-border-color);
  padding-bottom: 0.4em;
}

/* ── Stat badges ─────────────────────────────────────────── */
.stat-row { display: flex; flex-wrap: wrap; gap: 1em; margin-bottom: 0.5em; }
.stat-badge {
  text-align: center;
  min-width: 70px;
}
.stat-badge .num {
  display: block;
  font-size: 2.2em;
  font-weight: 700;
  color: #2d5986;
  line-height: 1;
}
.stat-badge .lbl {
  display: block;
  font-size: 0.75em;
  color: var(--global-text-color-light);
  margin-top: 0.2em;
}

/* ── Skill bars ──────────────────────────────────────────── */
.skill-bar-wrap { margin-bottom: 0.55em; }
.skill-bar-label {
  display: flex;
  justify-content: space-between;
  font-size: 0.82em;
  margin-bottom: 0.2em;
}
.skill-bar-track {
  height: 7px;
  background: var(--global-border-color);
  border-radius: 4px;
  overflow: hidden;
}
.skill-bar-fill {
  height: 100%;
  background: #2d5986;
  border-radius: 4px;
  transition: width 0.6s ease;
}

/* ── Print ───────────────────────────────────────────────── */
@media print {
  .author__avatar, .author__urls-wrapper, .sidebar, nav, footer,
  .page__share, .masthead { display: none !important; }
  .page { margin: 0; padding: 0; }
  .vis-card { break-inside: avoid; }
  canvas { max-width: 100% !important; }
}
</style>

<p style="font-size:0.88em; color:var(--global-text-color-light);">
  A graphical overview of my academic record.
  <a href="/cv/">Full CV</a> &nbsp;|&nbsp;
  <a href="/files/cv.pdf">Download full CV (PDF)</a> &nbsp;|&nbsp;
  <a href="/files/cv-short.pdf">Download short CV (PDF)</a> &nbsp;|&nbsp;
  <a href="javascript:window.print()">Print this page</a>
</p>

---

{% comment %} ── Compute counts from collections ───────────────────── {% endcomment %}

{% assign n_pubs      = site.publications | size %}
{% assign n_talks     = site.talks | size %}
{% assign n_teaching  = site.teaching | size %}
{% assign n_grants    = site.data.cv_details.grants | size %}
{% assign n_awards    = site.data.cv_details.awards | size %}
{% assign n_reviews   = site.data.cv_details.reviews.total_count | default: 0 %}

{% comment %} Publication authorship breakdown {% endcomment %}
{% assign n_first   = 0 %}
{% assign n_co      = 0 %}
{% assign n_unknown = 0 %}
{% for p in site.publications %}
  {% if p.author_position == "first" %}
    {% assign n_first = n_first | plus: 1 %}
  {% elsif p.author_position == "co" %}
    {% assign n_co = n_co | plus: 1 %}
  {% else %}
    {% assign n_unknown = n_unknown | plus: 1 %}
  {% endif %}
{% endfor %}

{% comment %} Publications per year for timeline chart {% endcomment %}
{% assign pub_years = "" %}
{% assign pub_counts = "" %}
{% for p in site.publications %}
  {% assign yr = p.date | date: "%Y" %}
  {% unless pub_years contains yr %}
    {% assign pub_years = pub_years | append: yr | append: "," %}
  {% endunless %}
{% endfor %}

{% comment %} Total grant amount {% endcomment %}
{% assign total_grant = 0 %}
{% for g in site.data.cv_details.grants %}
  {% assign total_grant = total_grant | plus: g.amount %}
{% endfor %}

<!-- ── Headline badges ──────────────────────────────────────── -->
<div class="vis-grid">

<div class="vis-card">
  <h3>Research output</h3>
  <div class="stat-row">
    <div class="stat-badge">
      <span class="num">{{ n_pubs }}</span>
      <span class="lbl">Publications</span>
    </div>
    <div class="stat-badge">
      <span class="num">{{ n_talks }}</span>
      <span class="lbl">Talks</span>
    </div>
    <div class="stat-badge">
      <span class="num">{{ n_reviews }}</span>
      <span class="lbl">Peer reviews</span>
    </div>
  </div>
</div>

<div class="vis-card">
  <h3>Teaching & funding</h3>
  <div class="stat-row">
    <div class="stat-badge">
      <span class="num">{{ n_teaching }}</span>
      <span class="lbl">Courses</span>
    </div>
    <div class="stat-badge">
      <span class="num">{{ n_grants }}</span>
      <span class="lbl">Grants</span>
    </div>
    <div class="stat-badge">
      <span class="num">{{ n_awards }}</span>
      <span class="lbl">Awards</span>
    </div>
  </div>
  {% if total_grant > 0 %}
  <p style="font-size:0.82em; color:var(--global-text-color-light); margin:0.5em 0 0;">
    Total funding: {{ total_grant | divided_by: 1000 }}k NOK
  </p>
  {% endif %}
</div>

</div><!-- /vis-grid -->

<!-- ── Charts ──────────────────────────────────────────────── -->
<div class="vis-grid">

<div class="vis-card">
  <h3>Authorship breakdown</h3>
  <canvas id="authorshipChart" height="200"></canvas>
</div>

<div class="vis-card">
  <h3>Publications per year</h3>
  <canvas id="pubTimelineChart" height="200"></canvas>
</div>

</div><!-- /vis-grid -->

<!-- ── Skills ──────────────────────────────────────────────── -->
<div class="vis-grid">

{% if site.data.cv_details.skills.programming %}
<div class="vis-card">
  <h3>Programming</h3>
  {% for s in site.data.cv_details.skills.programming %}
  <div class="skill-bar-wrap">
    <div class="skill-bar-label"><span>{{ s.name }}</span><span>{{ s.level }}%</span></div>
    <div class="skill-bar-track"><div class="skill-bar-fill" style="width:{{ s.level }}%;"></div></div>
  </div>
  {% endfor %}
</div>
{% endif %}

{% if site.data.cv_details.skills.languages %}
<div class="vis-card">
  <h3>Languages</h3>
  {% for l in site.data.cv_details.skills.languages %}
  <div class="skill-bar-wrap">
    <div class="skill-bar-label">
      <span>{{ l.name }}{% if l.note %} <em style="font-size:0.85em;">({{ l.note }})</em>{% endif %}</span>
      <span>{{ l.level }}%</span>
    </div>
    <div class="skill-bar-track"><div class="skill-bar-fill" style="width:{{ l.level }}%;"></div></div>
  </div>
  {% endfor %}
</div>
{% endif %}

{% if site.data.cv_details.skills.methods %}
<div class="vis-card">
  <h3>Methods</h3>
  {% for s in site.data.cv_details.skills.methods %}
  <div class="skill-bar-wrap">
    <div class="skill-bar-label"><span>{{ s.name }}</span><span>{{ s.level }}%</span></div>
    <div class="skill-bar-track"><div class="skill-bar-fill" style="width:{{ s.level }}%;"></div></div>
  </div>
  {% endfor %}
</div>
{% endif %}

</div><!-- /vis-grid -->

<!-- ── Chart.js ──────────────────────────────────────────── -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<script>
(function () {
  const accent = "#2d5986";
  const muted  = getComputedStyle(document.documentElement)
                   .getPropertyValue("--global-text-color-light").trim() || "#888";

  /* ── Authorship pie ─────────────────────────────────── */
  const nFirst   = {{ n_first }};
  const nCo      = {{ n_co }};
  const nUnknown = {{ n_unknown }};

  new Chart(document.getElementById("authorshipChart"), {
    type: "doughnut",
    data: {
      labels: ["First author", "Co-author", "Position unset"],
      datasets: [{
        data: [nFirst, nCo, nUnknown],
        backgroundColor: ["#2d5986", "#5b8db8", "#c8d8e8"],
        borderWidth: 1,
      }]
    },
    options: {
      plugins: {
        legend: { position: "bottom", labels: { boxWidth: 12, font: { size: 11 } } }
      },
      cutout: "55%",
    }
  });

  /* ── Publications per year bar ──────────────────────── */
  {% assign pub_year_map = "" %}
  {% assign all_years = "" %}
  {% for p in site.publications %}
    {% assign yr = p.date | date: "%Y" %}
    {% unless all_years contains yr %}
      {% assign all_years = all_years | append: yr | append: ";" %}
    {% endunless %}
  {% endfor %}

  {% assign year_list = all_years | split: ";" | sort %}
  const yearLabels = [{% for y in year_list %}{% if y != "" %}"{{ y }}",{% endif %}{% endfor %}];

  {% comment %} Build count per year {% endcomment %}
  const yearCounts = yearLabels.map(yr => {
    return [
      {% for p in site.publications %}
      { yr: "{{ p.date | date: '%Y' }}" },
      {% endfor %}
    ].filter(p => p.yr === yr).length;
  });

  new Chart(document.getElementById("pubTimelineChart"), {
    type: "bar",
    data: {
      labels: yearLabels,
      datasets: [{
        label: "Publications",
        data: yearCounts,
        backgroundColor: accent,
        borderRadius: 3,
      }]
    },
    options: {
      plugins: { legend: { display: false } },
      scales: {
        y: { beginAtZero: true, ticks: { stepSize: 1 } }
      }
    }
  });
})();
</script>
