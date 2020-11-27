# -*- coding: utf-8 -*-
# @Time: 2020/11/27 8:44
# @Author: Rollbear
# @Filename: test_analysis.py

import unittest

from res.tiny_syntax import TINY_SYNTAX
from entity.analyzer import Analyzer


class TestAnalysis(unittest.TestCase):
    def test_hello_world(self):
        print(TINY_SYNTAX.rules_info())

    def test_parser(self):
        analyzer = Analyzer(TINY_SYNTAX)


if __name__ == '__main__':
    unittest.main()
