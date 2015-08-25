#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'wogong'
SITENAME = 'Inner Space'
# SITESUBTITLE = 'Personal page for wogong, including blog, wiki and other things.'
SITEURL = 'http://www.wogong.net'
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'
PATH = 'content'

# GITHUB_URL = ''
# REVERSE_CATEGORY_ORDER = False
# DATE_FORMATS = '%Y-%m-%d'
LOCALE = 'C'
DEFAULT_PAGINATION = 4
# DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)
DEFAULT_DATE = 'fs'

#FEED_ALL_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

## Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

## Social widget
#SOCIAL = (('Twitter', 'http://twitter.com/wogong38'),
#          ('Wechat', '#'),)

MENUITEMS = (('blog', '/blog'),
        ('wiki', '/wiki'),
        ('book', '/book'),
        ('movie', '/movie'),
        ('archive', '/archives.html'),
        ('about', '/about.html'),)

ARTICLE_URL = ('{category}/{slug}/')
ARTICLE_SAVE_AS = ('{category}/{slug}/index.html')
PAGE_URL = ('page/{slug}/')
PAGE_SAVE_AS = ('page/{slug}/index.html')
CATEGORY_URL = ('{slug}/')
CATEGORY_SAVE_AS = ('{slug}/index.html')

USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# THEME = "simple"
# THEME = "notmyidea"
THEME = "./themes/wogong"
# THEME = "./themes/bootlex"

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

#DISQUS_SITENAME = "wogong"
GOOGLE_ANALYTICS = "UA-34308107-1"
#TWITTER_USERNAME = "wogong38"

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
        'extra/robots.txt': {'path': 'robots.txt'},
        'extra/favicon.ico': {'path': 'favicon.ico'}
}

# default value is ('index', 'tags', 'categories', 'archives')
# so we just add a 'sitemap'
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'

# develop
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
