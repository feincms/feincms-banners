# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.admin",
    "django.contrib.staticfiles",
    "feincms",
    "feincms.module.medialibrary",
    "feincms.module.page",
    "mptt",
    "feincms_banners",
    "testapp",
    # 'django_nose',
)

# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

SECRET_KEY = "elephant"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "runserver.sqlite",
        # 'TEST_NAME': 'blog_test.sqlite',
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

MIDDLEWARE_CLASSES = MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)

ROOT_URLCONF = "testapp.urls"
BLOG_TITLE = "Blog of the usual elephant"
BLOG_DESCRIPTION = ""
TIME_ZONE = "America/Chicago"
USE_TZ = False
DEFAULT_CHARSET = "utf-8"
LANGUAGES = (("en", "English"), ("de", "German"))
LANGUAGE_CODE = "en"
USE_I18N = True

DEBUG = True  # tests run with DEBUG=False
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "media")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]
