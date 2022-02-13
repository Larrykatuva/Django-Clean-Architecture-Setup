from django.test import TestCase
import unittest
import django
import pytest


@pytest.mark.django_db
class TestWorking(unittest.TestCase):
    def test_can_confirm_test_is_working(self):
        self.assertEqual("Working", "Working")