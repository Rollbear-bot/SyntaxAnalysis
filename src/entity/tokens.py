# -*- coding: utf-8 -*-
# @Time: 2020/11/27 8:57
# @Author: Rollbear
# @Filename: tokens.py

class Token:
    """符号的基类"""
    def __init__(self, token_c):
        self.token_content = token_c

    def __str__(self):
        return str(self.token_content)


class TerminalToken(Token):
    """终结符"""
    def __init__(self, token_c):
        super().__init__(token_c)


class NonTerminalToken(Token):
    """非终结符"""
    def __init__(self, token_c):
        super().__init__(token_c)


class StartToken(NonTerminalToken):
    """文法开始符号"""
    def __init__(self, token_c):
        super().__init__(token_c)
