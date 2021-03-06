#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Yoldee.fr'
SITENAME = 'Yoldee.fr'
SITEURL = 'http://www.yoldee.fr'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

#THEME = '/Users/vdagoury/Projects/yoldee.fr/00_Websites/www/themes/pelican-twitchy/'
THEME = 'attila-1.3'

HEADER_COVER = 'theme/images/home-bg.jpg'

COLOR_SCHEME_CSS = 'monokai.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('envelope', 'mailto:yodleefr@gmail.com'),
          ('twitter', 'https://twitter.com/yoldee'),
          ('blogger', 'https://blog.yoldee.fr'))

AUTHORS_BIO = {
  "Yoldee.fr": {
    "name": "Yoldee.fr",
    "cover": "https://yoldee.github.io/website/assets/images/avatar.png",
    "image": "https://avatars1.githubusercontent.com/u/44941961?s=460&v=4",
    "website": "http://blog.yoldee.fr",
    "location": "FRANCE",
    "bio": "This is the place for a small company that wants to grow. Cool, hugh?"
  }
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
