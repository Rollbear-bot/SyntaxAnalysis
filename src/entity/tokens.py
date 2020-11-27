# -*- coding: utf-8 -*-
# @Time: 2020/11/27 8:57
# @Author: Rollbear
# @Filename: tokens.py

class TerminalToken:
    def __init__(self, token):
        self.token_content = token

    def __str__(self):
        return str(self.token_content)


class NonTerminalToken:
    def __init__(self, token):
        self.token_content = token

    def __str__(self):
        return str(self.token_content)


class StartToken(NonTerminalToken):
    def __init__(self, token):
        super().__init__(token)
