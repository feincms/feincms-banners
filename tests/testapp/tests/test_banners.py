from __future__ import absolute_import, print_function, unicode_literals

from django.core.files.base import ContentFile
from django.test import TestCase

from feincms.module.medialibrary.models import MediaFile
from feincms.module.page.models import Page

from feincms_banners.models import Banner


class BannerTest(TestCase):
    def test_bannercontent(self):
        page = Page.objects.create(
            title='Home',
            slug='home',
            override_url='/',
        )

        mediafile = MediaFile()
        mediafile.file.save(
            'whatever.txt',
            ContentFile('whatever'),
            save=True)

        banner = Banner.objects.create(
            is_active=True,
            name='test banner 1',
            mediafile=mediafile,
            url='http://testserver/test-banner-1/',
            type='leaderboard',
        )

        page.bannercontent_set.create(
            region='main',
            ordering=0,
            specific=banner,
            type='leaderboard',
        )

        response = self.client.get(page.get_absolute_url())

        impression_url = '/banners/b/i/{0}/?_bimp'.format(banner.code)

        self.assertContains(
            response,
            impression_url,
        )

        banner = Banner.objects.get(pk=banner.pk)
        self.assertEqual(banner.embeds, 1)
        self.assertEqual(banner.impressions, 0)
        self.assertEqual(banner.click_count(), 0)

        self.assertContains(
            self.client.get(impression_url),
            '?',
        )

        banner = Banner.objects.get(pk=banner.pk)
        self.assertEqual(banner.impressions, 0)

        self.assertContains(
            self.client.get(
                impression_url,
                HTTP_X_REQUESTED_WITH='XMLHttpRequest',
            ),
            '+1',
        )

        banner = Banner.objects.get(pk=banner.pk)
        self.assertEqual(banner.impressions, 1)
        self.assertEqual(banner.click_count(), 0)

        click_url = '/banners/b/c/{0}/'.format(banner.code)
        self.assertRedirects(
            self.client.get(click_url),
            'http://testserver/test-banner-1/',
        )

        self.assertEqual(banner.click_count(), 1)
