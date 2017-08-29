# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.template import loader
from django.http import HttpResponse


def index(request):
    current_year = int(datetime.now().strftime("%Y"))

    template = loader.get_template('first/index.html')
    return HttpResponse(
            template.render({
                    'brussels_years': current_year - 2013,
                    'dev_years': current_year - 2011
                }, request))
