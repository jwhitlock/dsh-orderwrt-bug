# -*- coding: utf-8 -*-
"""Tests for sample models."""
from django.test import TestCase

from sample.models import Series, SeriesWork


class SeriesWorkTest(TestCase):

    """Tests for the SeriesWork model."""

    def setUp(self):
        """Create a test series."""
        s = self.series = Series.objects.create(
            name="The Chronicles of Narnia", author="C.S. Lewis")
        self.w_lion = s.works.create(
            title="The Lion, the Witch and the Wardrobe")
        self.w_caspian = s.works.create(title="Prince Caspian")
        self.w_voyage = s.works.create(title="The Voyage of the Dawn Treader")
        self.w_chair = s.works.create(title="The Silver Chair")
        self.w_horse = s.works.create(title="The Horse and His Boy")
        self.w_nephew = s.works.create(title="The Magician's Nephew")
        self.w_battle = s.works.create(title="The Last Battle")

    def test_serieswork_history(self):
        """Test series can be reverted."""
        self.w_caspian.title = 'Prince Caspian: The Return to Narnia'
        self.w_caspian.save()
        self.assertEqual(2, len(self.w_caspian.history.all()))
        oldest = self.w_caspian.history.all()[1]
        self.assertEqual(oldest.title, 'Prince Caspian')
        oldest.history_object.save()
        w_caspian = SeriesWork.objects.get(id=self.w_caspian.id)
        self.assertEqual(w_caspian.title, 'Prince Caspian')
