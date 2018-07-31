#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'BioCAT'
SITENAME = u'BioCAT'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['bootstrap-rst', 'i18n_subsites', 'render_math']
# PLUGINS = ['bootstrap-rst2', 'i18n_subsites', 'render_math']


JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# # Blogroll
LINKS = (('About Biocat', '#'),
         ('Science Highlights', '#'),
         ('Contact Us', '#'),
         ('Apply for beamtime', '#'),
         ('Prepare for your beamtime', '#'),
         ('APS', '#'),)

# LINKS = ()

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TAG_SAVE_AS = ''

LOAD_CONTENT_CACHE = False
USE_FOLDER_AS_CATEGORY = True


THEME = "./themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'sandstone'

# BANNER = './images/conf.jpg'
# BANNER_ALL_PAGES = False

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS=[
    ('About','/pages/about-biocat.html'),
    ('Users', '/pages/users.html'),
    ('Science', '/science_highlights.html'),
    ('Contact', '/pages/contact.html'),
    ('Links', '/pages/links.html')

    ]

STATIC_PATHS = ['images', 'extra']

DELETE_OUTPUT_DIRECTORY = True

TYPOGRIFY = True

PHOTO_LIBRARY = "./content/carousel"

HIDE_SIDEBAR = True


# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    # 'extra/business_cards/*'  :   {'path':'pages/business_cards/'}
    # 'extra/custom.js': {'path': 'static/js/custom.js'}
}

ARTICLE_EXCLUDES = ['extra']

CUSTOM_CSS = 'static/css/custom.css'

INDEX_SAVE_AS = 'science_highlights.html'
