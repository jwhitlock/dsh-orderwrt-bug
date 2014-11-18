# -*- coding: utf-8 -*-
"""URL routing patterns for dsh-orderwrt-bug."""

from django.conf.urls import patterns, include, url
from django.contrib import admin

from sample.urls import (
    urlpatterns as sample_urlpatterns)

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(sample_urlpatterns)),
)
