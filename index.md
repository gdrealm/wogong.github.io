---
layout: page
title: WoNote
tagline: Supporting tagline
---
{% include JB/setup %}

Welcome to wogong's blog

---

我在这里记录有价值的信息

---

- blog懒于更新，腹中无货难以示人。
- wiki更新较频繁，但是多用于自己备忘，旁人所需甚少，
  若能通过搜索找到这里，甚至能起些许帮助作用，已是不敢奢望之幸事。
- kindle自定义搜索，本人乃kindle拥虿。
- 碌碌无为，努力有为中。

## Posts

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
