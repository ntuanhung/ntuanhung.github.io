---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<!-- {% if author.googlescholar %} -->
  
<!-- {% endif %} -->

{% include base_path %}

<p>You can also find my publications on <u><a href="{{site.author.googlescholar}}">my Google Scholar profile</a></u> or <u><a href="{{site.author.researchmap}}">my ResearchMap profile</a>.</u></p>

<h2>Journal Articles</h2>
<hr style="width:50%">

{% for post in site.publications reversed %}
  {% if post.papertype == "article" %}
    {% include archive-single-publication.html %}
  {% endif %}
{% endfor %}

<h2>Conference Proceedings</h2>
<hr>

{% for post in site.publications reversed %}
  {% if post.papertype == "proceedings" %}
    {% include archive-single-publication.html %}
  {% endif %}
{% endfor %}

<hr>
<h2>Books and Chapters</h2>

{% for post in site.publications reversed %}
  {% if post.papertype == "book" or post.papertype == "chapter" or post.papertype == "section" %}
    {% include archive-single-publication.html %}
  {% endif %}
{% endfor %}

<hr>
<h2>Technical Reports</h2>

{% for post in site.publications reversed %}
  {% if post.papertype == "techreport" %}
    {% include archive-single-publication.html %}
  {% endif %}
{% endfor %}
