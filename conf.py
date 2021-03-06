# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

BLOG_AUTHOR = "Chaos Computer Club Wien"
BLOG_TITLE = "CCC Wien"
SITE_URL = "/"
BLOG_EMAIL = "buero@c3w.at"
BLOG_DESCRIPTION = "Chaos Computer Club Wien"  # (translatable)
THEME = 'c3w-eh18'
USE_BUNDLES = True
USE_CDN = False

TWITTER_CARD = {
	'use_twitter_cards': True,
	'card': 'summary_large_image',
	'site': '@c3wien',
	'creator': '@c3wien',
}

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = ""


DEFAULT_LANG = "de"
TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # "en": "./en",
}
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
		('/aktuelles/', 'Aktuelles'),
		('/mitmachen/', 'Mitmachen'),
		('/events/', 'Events'),
		('/projekte/', 'Projekte'),
                ('/services/', 'Services'),
		('/categories/publikationen/', 'Publikationen'),
		('/presse/', 'Pressespiegel'),
		('/links/', 'Links'),
		('/datenschutz/', 'Datenschutz'),
#        ('/archive.html', 'Archiv'),
#		('/categories/index.html', 'Tags'),
#		('/rss.xml', 'RSS'),
#        ((('/foo', 'FOO'),
#          ('/bar', 'BAR')), 'BAZ'),
	),
}

CONTENT_FOOTER = 'Die <span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Inhalte</span> stehen unter <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">CC BY-NC 4.0</a> &#8208; <a href="/impressum/">Impressum</a> - <a href="/datenschutz/">Datenschutz</a> - Fediverse: <a rel="me" href="https://chaos.social/@C3Wien">@C3Wien@chaos.social</a>'
TIMEZONE = "Europe/Vienna"

COMPILERS = {
    "markdown": ('.md', '.mdown', '.markdown'),
    "rest": ('.rst', '.txt'),
    "html": ('.html', '.htm'),
}

# Writes tag cloud data in form of tag_cloud_data.json.
# Warning: this option will change its default value to False in v8!
WRITE_TAG_CLOUD = True

IMAGE_FOLDERS = {'content/images': 'images'}
# IMAGE_THUMBNAIL_SIZE = 400

FILES_FOLDERS = {'content/files': 'files', 'webroot': ''}

INDEX_TEASERS = True
# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the feeds, if FEED_TEASERS is True (translatable)
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'


CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}
STRIP_INDEXES = True
PRETTY_URLS = True
COPY_SOURCES = False
MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite', 'extra']
FILE_METADATA_UNSLUGIFY_TITLES = True
ENABLE_AUTHOR_PAGES = False
COMMENT_SYSTEM = False
INDEX_PATH = "aktuelles"
ARCHIVE_PATH = "posts"

POSTS = (
    ("content/posts/*.rst", "posts", "post.tmpl"),
    ("content/posts/*.md", "posts", "post.tmpl"),
    ("content/posts/*.txt", "posts", "post.tmpl"),
    ("content/posts/*.html", "posts", "post.tmpl"),
)
PAGES = (
    ("content/pages/*.rst", "", "story.tmpl"),
    ("content/pages/*.md", "", "story.tmpl"),
    ("content/pages/*.txt", "", "story.tmpl"),
    ("content/pages/*.html", "", "story.tmpl"),
)
