# -*- coding: utf-8 -*-
# @Time: 2020/11/29 10:51
# @Author: Rollbear
# @Filename: tiny_follow_set.py

from entity.tokens import *
from entity.rule import *


TINY_FOLLOW = {
    "program": {"EOF"},
    "stmt-sequence": {"EOF"},
    "statement": {";", "EOF"},
    "if-stmt": {";", "EOF"},
    "repeat-stmt": {";", "EOF"},
    "assign-stmt": {";", "EOF"},
    "read-stmt": {";", "EOF"},
    "write-stmt": {";", "EOF"},
    "exp": {";", "EOF", "then", ")"},
    "comparison-op": {"identifier", "number", "("},
    "simple-exp": {";", "EOF", "then", ")", "<", "="},
    "addop": {"identifier", "number", "("},
    "term": {";", "EOF", "then", ")", "<", "="},
    "mulop": {"identifier", "number", "("},
    "factor": {"*", "/", ";", "EOF", "then", ")", "<", "="}
}
