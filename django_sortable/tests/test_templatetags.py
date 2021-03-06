import os
import unittest

from django.template import TemplateSyntaxError
from django.template.base import Token
from django.test import RequestFactory
from django.test import SimpleTestCase

os.environ["DJANGO_SETTINGS_MODULE"] = "django_sortable.test_settings"

from django_sortable.templatetags.sortable import parse_tag_token, sortable_link, \
    sortable_header, sortable_url, sortable_class, SortableTableHeaderNode


class TemplateTagTests(unittest.TestCase):

    def test_parse_tag_token(self):
        token = Token(token_type='TOKEN_TEXT', contents='sortable_link test_field test_title')

        result = parse_tag_token(token)

        self.assertEqual(result, (u'test_field', u'test_title'))

    def test_sortable_link(self):
        token = Token(token_type='TOKEN_TEXT', contents='sortable_link test_field test_title')
        result = sortable_link(None, token)

        self.assertEqual(result.default_direction, 'asc')
        self.assertEqual(result.field_name, 'test_field')
        self.assertEqual(result.title, 'test_title')

    def test_sortable_link_desc(self):
        token = Token(token_type='TOKEN_VAR', contents='sortable_link -test_field test_title')
        result = sortable_link(None, token)

        self.assertEqual(result.default_direction, 'desc')
        self.assertEqual(result.field_name, 'test_field')
        self.assertEqual(result.title, 'test_title')

    def test_sortable_header(self):
        token = Token(token_type='TOKEN_TEXT', contents='sortable_header test_field test_title')
        result = sortable_header(None, token)

        self.assertEqual(result.default_direction, 'asc')
        self.assertEqual(result.field_name, 'test_field')
        self.assertEqual(result.title, 'test_title')

    def test_sortable_url(self):
        token = Token(token_type='TOKEN_TEXT', contents='sortable_url test_field test_title')
        result = sortable_url(None, token)

        self.assertEqual(result.default_direction, 'asc')
        self.assertEqual(result.field_name, 'test_field')
        self.assertEqual(result.title, 'test_title')

    def test_sortable_class(self):
        token = Token(token_type='TOKEN_TEXT', contents='sortable_class test_field test_title')
        result = sortable_class(None, token)

        self.assertEqual(result.default_direction, 'asc')
        self.assertEqual(result.field_name, 'test_field')
        self.assertEqual(result.title, 'test_title')

    def test_too_few_arguments_raises_error(self):
        token = Token(token_type='TOKEN_TEXT', contents='sortable_link')

        with self.assertRaises(TemplateSyntaxError):
            parse_tag_token(token)

    def test_single_argument_sets_title_to_field_name(self):
        token = Token(token_type='TOKEN_TEXT', contents='sortable_link test_field')

        result = sortable_class(None, token)

        self.assertEqual(result.default_direction, 'asc')
        self.assertEqual(result.field_name, 'test_field')
        self.assertEqual(result.title, 'Test_field')

    def test_single_argument_with_dash_sets_title_to_field_name(self):
        token = Token(token_type='TOKEN_TEXT', contents='sortable_link -test_field')

        result = sortable_class(None, token)

        self.assertEqual(result.default_direction, 'desc')
        self.assertEqual(result.field_name, 'test_field')
        self.assertEqual(result.title, 'Test_field')

    def test_single_argument_with_plus_sets_title_to_field_name(self):
        token = Token(token_type='TOKEN_TEXT', contents='sortable_link +test_field')

        result = sortable_class(None, token)

        self.assertEqual(result.default_direction, 'asc')
        self.assertEqual(result.field_name, 'test_field')
        self.assertEqual(result.title, 'Test_field')


class TemplateTagWithRequestTests(SimpleTestCase):

    def setUp(self):
        self.requestFactory = RequestFactory()

    def test_sortable_table_header_node_render(self):
        node = SortableTableHeaderNode('test_field', 'test_title')
        result = node.render({'request': self.requestFactory.get('/test_path')})

        self.assertEqual(result, ('<th class="desc"><a href="/test_path?sort=test_field&amp;dir=asc" '
                                  'title="test_title">test_title</a></th>'))
