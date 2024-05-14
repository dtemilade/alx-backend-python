#!/usr/bin/env python3
""" Script for several test utils.
    combined four different test utils cases.
"""
import unittest
import requests
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """ class that inherits from unittest.TestCase """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path_map, result_expec):
        """ Using context manager to test that a KeyError is raised
        """
        self.assertEqual(access_nested_map(nested_map, path_map), result_expec)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path_map):
        """ Using context manager to test that a KeyError is raised
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path_map)

        self.assertEqual(
            f'KeyError({str(error.exception)})', repr(error.exception))


class TestGetJson(unittest.TestCase):
    """ The Test JSON class """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ method to test that utils.get_json returns the expected result.
        """
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ Test memoize Class that house another class"""

    def test_memoize(self):
        """ Decorator for test memoize Class """
        class TestClass:
            """ The test Class inside Test memoize Class """

            def a_method(self):
                """ The method for Test Class """
                return 42

            @memoize
            def a_property(self):
                """ Decorator defined for Test Class """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
