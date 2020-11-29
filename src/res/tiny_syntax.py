# -*- coding: utf-8 -*-
# @Time: 2020/11/27 9:50
# @Author: Rollbear
# @Filename: tiny_syntax.py

from entity.syntax import Syntax
from res.tiny_syntax_rules import TINY_SYNTAX_RULES
from res.extent_tiny_syntax_rules import EXTENT_TINY_SYNTAX_RULES
from res.tiny_follow_set import TINY_FOLLOW

# Tiny语言上下文无关文法
TINY_SYNTAX = Syntax(rules=EXTENT_TINY_SYNTAX_RULES, follow_set_load=TINY_FOLLOW)
