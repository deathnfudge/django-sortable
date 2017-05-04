import os
import unittest

from django.template.base import Token

os.environ["DJANGO_SETTINGS_MODULE"] = "django_sortable.settings"

from django_sortable.templatetags.sortable import parse_tag_token, sortable_link, sortable_header, sortable_url, \
    sortable_class


class TemplateTagTests(unittest.TestCase):

    def test_parse_tag_token(self):
        token = Token(token_type='TOKEN_TEXT', contents='{% sortable_link test_field test_title %}')

        result = parse_tag_token(token)

        self.assertEqual(result, (u'sortable_link', u'test_field'))

    def test_sortable_link(self):
        token = Token(token_type='TOKEN_TEXT', contents='{% sortable_link test_field test_title %}')
        result = sortable_link(self, token)

        self.assertEqual(result.default_direction, 'asc')
        self.assertEqual(result.field_name, 'sortable_link')
        self.assertEqual(result.title, 'test_field')

    def test_sortable_header(self):
        token = Token(token_type='TOKEN_TEXT', contents='{% sortable_header test_field test_title %}')
        result = sortable_header(self, token)

        self.assertEqual(result.default_direction, 'asc')
        self.assertEqual(result.field_name, 'sortable_header')
        self.assertEqual(result.title, 'test_field')

    def test_sortable_url(self):
        token = Token(token_type='TOKEN_TEXT', contents='{% sortable_url test_field test_title %}')
        result = sortable_url(self, token)

        self.assertEqual(result.default_direction, 'asc')
        self.assertEqual(result.field_name, 'sortable_url')
        self.assertEqual(result.title, 'test_field')

    def test_sortable_class(self):
        token = Token(token_type='TOKEN_TEXT', contents='{% sortable_class test_field test_title %}')
        result = sortable_class(self, token)

        self.assertEqual(result.default_direction, 'asc')
        self.assertEqual(result.field_name, 'sortable_class')
        self.assertEqual(result.title, 'test_field')
