from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from feincms_banners import views


urlpatterns = [
    url(r'^b/c/(?P<code>[^/]+)/$', views.click, name='banner_click'),
    url(r'^b/i/(?P<code>[^/]+)/$', views.impression, name='banner_impression'),
]
