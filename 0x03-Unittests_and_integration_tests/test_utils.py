#!/usr/bin/env python3
"""Learning unittesting in python
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessnestedMap(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand([
        # test case 1
        ({"a": 1}, ("a",), 1),
        # test case 2
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        # test case 3
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_maps(self, nested_map, path, expected_result):
        """_summary_

        Args:
            nested_map (_type_): _description_
            path (_type_): _description_
            expected_result (_type_): _description_
        """
        result = access_nested_map(nested_map=nested_map, path=path)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
