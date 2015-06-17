#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'wogong'
SITENAME = 'Inner Space'
SITESUBTITLE = 'Personal page for wogong, including blog, wiki and other things.'
SITEURL = 'https://wogong.net'
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'
PATH = 'content'

# GITHUB_URL = 'http://github.com/ametaireau/'
# DISQUS_SITENAME = "wogong"
REVERSE_CATEGORY_ORDER = False
# DATE_FORMATS = '%Y-%m-%d'
LOCALE = 'C'
DEFAULT_PAGINATION = 4
# DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# FEED_ALL_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

## Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

## Social widget
#SOCIAL = (('Twitter', 'http://twitter.com/wogong38'),
#          ('Wechat', '#'),)

MENUITEMS = (('blog', '/category/blog'),
        ('wiki', '/category/wiki'),
        ('book', '/category/book'),
        ('movie', '/category/movie'),
        ('archive', '/archives'),)

## Uncomment following line if you want document-relative URLs when developing
## can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True
ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

LOAD_CONTENT_CACHE = False

USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# THEME = "simple"
# THEME = "notmyidea"
THEME = "/home/wogong/pelican/themes/wogong"

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
