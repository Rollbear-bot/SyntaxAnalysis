# -*- coding: utf-8 -*-
# @Time: 2020/11/30 11:01
# @Author: Rollbear
# @Filename: word_type.py


class WordType:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return str(self.__class__) + ": " + self.content


class ReservedWord(WordType):
    def __init__(self, content):
        super().__init__(content)


class Identifier(WordType):
    def __init__(self, content):
        super().__init__(content)


class Number(WordType):
    def __init__(self, content):
        super().__init__(content)


class Operator(WordType):
    def __init__(self, content):
        super().__init__(content)


class Delimiter(WordType):
    def __init__(self, content):
        super().__init__(content)


class EOF(WordType):
    def __init__(self, content):
        super().__init__(content)
