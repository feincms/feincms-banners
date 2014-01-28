# -*- coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent

from feincms_banners.contents import BannerContent


Page.register_templates({
    'key': 'default',
    'title': 'default',
    'path': 'base.html',
    'regions': (
        ('main', 'Main content area'),
    ),
})
Page.create_content_type(RichTextContent, cleanse=False, regions=('main',))
Page.create_content_type(BannerContent)
