# -*- coding: utf-8 -*-
"""URL routing patterns for sample."""

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views
assert views  # Remove when views are used

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(
        template_name='sample/home.jinja2'),
        name='home'),
)
