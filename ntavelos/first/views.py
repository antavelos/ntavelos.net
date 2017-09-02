# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.template import loader
from django.http import HttpResponse

from first.models import CV


def index(request):
    current_year = int(datetime.now().strftime("%Y"))

    template = loader.get_template('first/index.html')
    return HttpResponse(
            template.render({
                    'brussels_years': current_year - 2013,
                    'dev_years': current_year - 2011
                }, request))


def download(request):
    cv = CV.objects.latest('created')
    with open(cv.file.path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="")
        response['Content-Disposition'] = 'attachment; filename={}'\
                                          .format(cv.official_name)
        return response
