# pylint: disable=missing-docstring, line-too-long

import unittest
from recipe import parse


class TestRecipe(unittest.TestCase):
    def test_parse_carrot(self):
        recipes = parse(open('pages/carrot.html', encoding='utf-8'))
        self.assertIsInstance(recipes, list, "The `parse` method should return a `list` of `dict` objects")
        self.assertIsInstance(recipes[0], dict, "The `parse_recipe` method should return a `dict` object")
        self.assertEqual(recipes[0]['name'], 'Agave Glazed Carrots')
        self.assertEqual(recipes[0]['difficulty'], 'Very easy')
        self.assertEqual(recipes[0]['prep_time'], '-1 min')
