# -*- coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse


admin.autodiscover()


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^banners/", include("feincms_banners.urls")),
    url(r"^test-banner-1/$", lambda request: HttpResponse("Hello test banner 1")),
    url(r"", include("feincms.urls")),
]
