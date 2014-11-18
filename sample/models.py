# -*- coding: utf-8 -*-
"""Django models for sample."""
from django.db import models
from simple_history.models import HistoricalRecords


class Series(models.Model):

    """A series of works, like a trilogy of books."""

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)


class SeriesWork(models.Model):

    """A work in a a series of works."""

    series = models.ForeignKey('Series', related_name='works')
    title = models.CharField(max_length=100)
    history = HistoricalRecords()

    class Meta:
        order_with_respect_to = 'series'
