from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from feincms_banners.models import Banner


def click(request, code):
    banner = get_object_or_404(Banner.objects.active(), code=code)
    banner.click(request)
    return HttpResponseRedirect(banner.url)


def impression(request, code):
    if (not request.is_ajax() and Banner.objects.filter(code=code).update(
            impressions=F('impressions') + 1
            )):
        return HttpResponse('+1')
    return HttpResponse('?')
