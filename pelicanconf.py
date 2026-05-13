#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Basic settings
AUTHOR = 'Justin Quick'
SITENAME = 'Justin Quick Developer Site'
SITEURL = ''

PATH = 'markdown-content'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Theme
THEME = 'themes/justquick'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL and save paths
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
INDEX_SAVE_AS = 'index.html'

# Disable unused features
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

OUTPUT_PATH = '.'

STATIC_PATHS = []
EXTRA_PATH_METADATA = {}

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['yaml_loader']

# Default pagination
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Template pages - map markdown files to specific templates
TEMPLATE_PAGES = {}

# Direct templates
DIRECT_TEMPLATES = ['index']

# Use file modification dates
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'

# Markdown extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
