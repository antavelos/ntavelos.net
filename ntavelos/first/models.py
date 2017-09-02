# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import datetime

from django.db import models

CV_SUBDIR = 'cv'


def upload_cv(instance, filename):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fname, ext = os.path.splitext(filename)

    return "{}/{}_{}{}".format(CV_SUBDIR, fname, timestamp, ext)


class CV(models.Model):
    file = models.FileField(upload_to=upload_cv)
    notes = models.CharField(max_length=1024, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    @property
    def name(self):
        return os.path.basename(self.file.path)

    @property
    def official_name(self):
        _, ext = os.path.splitext(self.name)
        return "Alexandros_Ntavelos_CV{}".format(ext)
