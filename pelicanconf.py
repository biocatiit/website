#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'BioCAT'
SITENAME = u'BioCAT'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'
SUMMARY_MAX_LENGTH = 200
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['bootstrap-rst',
    'i18n_subsites',
    'render_math',
    'tipue_search',
    ]

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TAG_SAVE_AS = ''

LOAD_CONTENT_CACHE = False
USE_FOLDER_AS_CATEGORY = True


THEME = "./themes/biocat-mod-pelican-bootstrap3"
BOOTSTRAP_THEME = 'sandstone'

# BANNER = './images/conf.jpg'
# BANNER_ALL_PAGES = False

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS=[
    ('About','/pages/about-biocat.html'),
    ('Users', '/pages/users.html'),
    ('Science', '/pages/biocat-science.html'),
    ('Contact', '/pages/contact.html'),
    ('Links', '/pages/links.html')

    ]

STATIC_PATHS = ['images', 'extra', 'files']

DELETE_OUTPUT_DIRECTORY = True

TYPOGRIFY = True

HIDE_SIDEBAR = True

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')


# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/favicon.ico': {'path': ''}
    # 'extra/business_cards/*'  :   {'path':'pages/business_cards/'}
    # 'extra/custom.js': {'path': 'static/js/custom.js'}
}

FAVICON = 'favicon.ico'

ARTICLE_EXCLUDES = ['extra']

CUSTOM_CSS = 'static/custom.css'

# INDEX_SAVE_AS = 'articles/science_highlights.html'
INDEX_SAVE_AS = 'science_highlights.html'

AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = 'tag/{slug}.html'
TAGS_SAVE_AS = ''
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARCHIVES_SAVE_AS = ''

GOOGLE_ANALYTICS = 'UA-104830878-3'

GITHUB_URL = 'http://github.com/biocatiit/website'

