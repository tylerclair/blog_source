#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tyler Clair'
SITENAME = 'ITA Blog'
SITEURL = 'https://tylerclair.github.io'

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

THEME = 'tuxlite_tbs'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/tylerclair'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DEFUALT_METADATA = {
    'status': 'draft',
}

# Output directory
OUTPUT_PATH = '../blog_html'