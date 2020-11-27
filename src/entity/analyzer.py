# -*- coding: utf-8 -*-
# @Time: 2020/11/27 10:13
# @Author: Rollbear
# @Filename: analyzer.py

from entity.syntax import Syntax


class Analyzer:
    """文法分析器"""
    def __init__(self, syntax: Syntax):
        self.syntax = syntax

    def analyze_single_sent(self, sentence):
        """分析单个句子的文法结构"""
        pass
