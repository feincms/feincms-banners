from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from feincms_banners.models import Banner

from feincms.admin.item_editor import FeinCMSInline


class BannerContentInline(FeinCMSInline):
    raw_id_fields = ('specific',)


class BannerContent(models.Model):
    feincms_item_editor_inline = BannerContentInline

    is_section_aware = True

    specific = models.ForeignKey(Banner, verbose_name=_('specific'),
        blank=True, null=True, help_text=_('If you leave this empty, a random banner will be selected.'),
        limit_choices_to={'is_active': True})
    type = models.CharField(_('type'), max_length=20, choices=Banner.TYPE_CHOICES)

    class Meta:
        abstract = True
        verbose_name = _('banner')
        verbose_name = _('banners')

    def render(self, **kwargs):
        if self.specific:
            if self.specific.is_active:
                banner = self.specific
                type = banner.type
            else:
                return u''
        else:
            try:
                banner = Banner.objects.active().filter(
                    type=self.type).select_related('mediafile').order_by('?')[0]
                type = self.type
            except IndexError:
                return u''

        return render_to_string([
            'content/banner/%s.html' % type,
            'content/banner/default.html',
            ], {'content': self, 'banner': banner})