import os
import unittest

from django.template.base import Token

os.environ["DJANGO_SETTINGS_MODULE"] = "django_sortable.settings"

from django_sortable.templatetags.sortable import parse_tag_token


class TemplateTagTests(unittest.TestCase):

    def test_parse_tag_token(self):
        token = Token(token_type='TOKEN_TEXT', contents='{% sortable_link test_field test_title %}')

        result = parse_tag_token(token)

        self.assertEqual(result, (u'sortable_link', u'test_field'))
