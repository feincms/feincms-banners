from django.contrib import admin

from feincms_banners import models


admin.site.register(
    models.Banner,
    list_display=(
        'name', 'is_active', 'type', 'url', 'active_from',
        'active_until', 'embeds', 'impressions', 'click_count'),
    list_filter=('is_active', 'type'),
    raw_id_fields=('mediafile',),
    search_fields=('name', 'url', 'code'),
)
admin.site.register(
    models.Click,
    list_display=('timestamp', 'banner', 'ip', 'user_agent', 'referrer'),
    search_fields=('banner__name', 'user_agent', 'referrer'),
)
