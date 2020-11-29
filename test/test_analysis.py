# -*- coding: utf-8 -*-
# @Time: 2020/11/27 8:44
# @Author: Rollbear
# @Filename: test_analysis.py

import unittest

from res.tiny_syntax import TINY_SYNTAX
from entity.analyzer import Analyzer
from entity.tokenizer import *


class TestAnalysis(unittest.TestCase):
    def test_hello_world(self):
        info = TINY_SYNTAX.rules_info()
        print(info)

    def test_parser(self):
        analyzer = Analyzer(TINY_SYNTAX, tokenizer_demo)
        print()
        analyzer.analyze()

    def test_ll_1_table(self):
        TINY_SYNTAX.print_ll_1_table_info()
        pass

    def test_doc_via_course(self):
        pass


if __name__ == '__main__':
    unittest.main()
