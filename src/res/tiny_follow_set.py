# -*- coding: utf-8 -*-
# @Time: 2020/11/29 10:51
# @Author: Rollbear
# @Filename: tiny_follow_set.py

from entity.tokens import *
from entity.rule import *


# TINY_FOLLOW = {
#     "program": {"EOF"},
#     "stmt-sequence": {"EOF"},
#     "statement": {"EOF"},
#     "if-stmt": {";", "EOF"},
#     "repeat-stmt": {";", "EOF"},
#     "assign-stmt": {";", "EOF"},
#     "read-stmt": {";", "EOF"},
#     "write-stmt": {";", "EOF"},
#     "exp": {";", "EOF", "then", ")"},
#     "comparison-op": {"identifier", "number", "("},
#     "simple-exp": {";", "EOF", "then", ")", "<", "="},
#     "addop": {"identifier", "number", "("},
#     "term": {";", "EOF", "then", ")", "<", "="},
#     "mulop": {"identifier", "number", "("},
#     "factor": {"*", "/", ";", "EOF", "then", ")", "<", "="}
# }

# 按照语句段来组织，而不是单个Token
end_of_stmt = {"EOF", "until", "enddo", "else", "endwhile", "while"}

TINY_FOLLOW = {
    "; statement": end_of_stmt,
    "comparison-op simple-exp": {";", "EOF", ")"} | end_of_stmt,
    "addop term": {";", "EOF", ")", "<", "="} | end_of_stmt,
    "mulop factor": {";", "EOF", ")", "<", "=", "+", "-"} | end_of_stmt,
    "else stmt-sequence": {"EOF"}
}
