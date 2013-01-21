---
layout: page
title: WoNote
tagline: Supporting tagline
---
{% include JB/setup %}

Welcome to wogong's blog

---

我在这里记录有价值的信息

## Posts

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

## [Douban](http://www.douban.com/people/wogong38/)
<script type="text/javascript" src="http://www.douban.com/service/badge/wogong38/?show=collection&amp;n=6&amp;columns=6&amp;picsize=medium&amp;hidelogo=yes&amp;hideself=yes&amp;cat=movie|book" ></script>


