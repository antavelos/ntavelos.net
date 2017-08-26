# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('first/index.html')
    return HttpResponse(template.render({}, request))
