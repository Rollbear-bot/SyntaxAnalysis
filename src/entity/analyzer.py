# -*- coding: utf-8 -*-
# @Time: 2020/11/27 10:13
# @Author: Rollbear
# @Filename: analyzer.py

from entity.syntax import Syntax
from entity.tokenizer import Tokenizer


class Analyzer:
    """文法分析器"""
    def __init__(self, syntax: Syntax, tokenizer: Tokenizer):
        self.syntax = syntax
        self.tokenizer = tokenizer

    def analyze_single_sent(self, sentence):
        """分析单个句子的文法结构"""
        pass

    def _get_token(self):
        """获取下一个单词"""
        return self.tokenizer.__next__()
