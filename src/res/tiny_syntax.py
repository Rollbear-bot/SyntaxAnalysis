# -*- coding: utf-8 -*-
# @Time: 2020/11/27 9:50
# @Author: Rollbear
# @Filename: tiny_syntax.py

from entity.syntax import Syntax
from res.tiny_syntax_rules import TINY_SYNTAX_RULES

# Tiny语言上下文无关文法
TINY_SYNTAX = Syntax(rules=TINY_SYNTAX_RULES)
