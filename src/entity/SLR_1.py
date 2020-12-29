# -*- coding: utf-8 -*-
# @Time: 2020/12/2 13:19
# @Author: Rollbear
# @Filename: SLR_1.py


class SLR1Analyzer:
    """使用SLR(1)分析法的语法分析器"""
    def __init__(self, syntax, tokenizer, debug=False):
        self.syntax = syntax
        self.tokenizer = tokenizer
        self.analyze_log = ""

        self._analyze(debug)

    def _get_token(self):
        return self.tokenizer.__next__()

    def _analyze(self, debug):
        self.analyze_log = ""
        stack = []

        start_token = self.syntax.start_token[0]

        cur_node = None
        cur_word = self._get_token()

