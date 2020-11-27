# -*- coding: utf-8 -*-
# @Time: 2020/11/27 16:13
# @Author: Rollbear
# @Filename: tokenizer.py

class Tokenizer:
    def __init__(self, doc):
        self.tokens = []
        self.raw_string = doc
        self.index = -1

    def __iter__(self):
        return iter(self.tokens)

    def __next__(self):
        self.index += 1
        return self.tokens[self.index]


# todo::only for tokenizer TEST
tokenizer_demo = Tokenizer("")
tokenizer_demo.tokens = [
    "read", "x", ";",
    "if", "0", "<", "x", "then",
    "fact", ":=", "1", ";",
    "repeat",
    "fact", ":=", "fact", "*", "x", ";",
    "x", ":=", "x", "-", "1", ";",
    "until", "x", "=", "0", ";",
    "write", "fact", ";",
    "end",
    "EOF"
]
