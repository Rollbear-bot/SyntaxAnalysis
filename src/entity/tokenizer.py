# -*- coding: utf-8 -*-
# @Time: 2020/11/27 16:13
# @Author: Rollbear
# @Filename: tokenizer.py

from enum import Enum
from entity.word_type import *


class State(Enum):
    IN_COMMENT = 0
    IN_WORD = 1
    IN_OP = 2
    IN_NUM = 3
    IN_BLANK = 4


alphabet = [chr(a) for a in list(range(ord("A"), ord("Z") + 1))
            + list(range(ord("a"), ord("z") + 1))]
number = [chr(a) for a in range(ord("0"), ord("9") + 1)]

reserved_words = ["if", "else", "repeat", "until", "read", "write", "while", "endwhile",
                  "for", "to", "downto", "do"]
ops_1_chr = ["+", "-", "=", "*", "/", "^", "%", "<", ">"]
ops_2_chr = [":=", "+=", "-=", "*=", "/=", "<=", ">=", "<>"]
ops_2_chr_start = ops_1_chr + [":"]
other_symbols = [".", "{", "}", "[", "]", ";", "(", ")", ","]
blank = [" ", "\n", "\t"]


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

    @staticmethod
    def word_type_wrapper(state, buffer):
        res_obj = None
        if state == State.IN_WORD:
            if buffer in reserved_words:
                res_obj = ReservedWord(buffer)
            else:
                res_obj = Identifier(buffer)
        elif state == State.IN_NUM:
            res_obj = Number(buffer)
        elif state == State.IN_OP:
            res_obj = Operator(buffer)
        return res_obj

    def run(self):
        state = -1
        buffer = ""

        for cur_char in self.raw_string:
            # 标识符与保留字
            if cur_char in alphabet or cur_char == "_":
                if state != -1 and state != State.IN_WORD:
                    if buffer != "":
                        self.tokens.append(self.word_type_wrapper(state, buffer))
                        buffer = ""

                buffer += cur_char
                state = State.IN_WORD

            # 操作符
            if cur_char in ops_2_chr_start:
                if state != -1 and state != State.IN_OP:
                    if buffer != "":
                        self.tokens.append(self.word_type_wrapper(state, buffer))
                        buffer = ""
                buffer += cur_char
                state = State.IN_OP
                if buffer + cur_char in ops_2_chr:
                    self.tokens.append(self.word_type_wrapper(state, buffer + cur_char))
                    buffer = ""

            # 数值
            if cur_char in number:
                if state != -1 and state != State.IN_NUM:
                    if buffer != "":
                        self.tokens.append(self.word_type_wrapper(state, buffer))
                        buffer = ""
                buffer += cur_char
                state = State.IN_NUM

            # 空白字符
            if cur_char in blank:
                if state != -1 and state != State.IN_BLANK:
                    if buffer != "":
                        self.tokens.append(self.word_type_wrapper(state, buffer))
                        buffer = ""
                # 空白字符不需要保存
                state = State.IN_BLANK

            # 界符等
            if cur_char in other_symbols:
                if buffer != "":
                    self.tokens.append(self.word_type_wrapper(state, buffer))
                    buffer = ""
                self.tokens.append(Delimiter(cur_char))


demo1 = [
    "read", "x", ";",
    "if", "0", "<", "x", "then",
    "fact", ":=", "1", ";",
    "repeat",
    "fact", ":=", "fact", "*", "x", ";",
    "x", ":=", "x", "-", "1",
    "until", "x", "=", "0", ";",
    "write", "fact", ";",
    "end",
    "EOF"
]

demo2 = [
    "read", "identifier", ";",
    "if", "(", "number", "<", "identifier", ")",
    "identifier", ":=", "number", ";",
    "repeat",
    "identifier", ":=", "identifier", "*", "identifier", ";",
    "identifier", ":=", "identifier", "-", "number", ";",
    "until", "identifier", "=", "number", ";",
    "write", "identifier", ";",
    "EOF"
]

demo3 = [
    "read", "x", ";",
    "if", "(", "0", "<", "x", ")",
    "fact", ":=", "1", ";",
    "while", "(", "x", ">", "0", ")",
    "fact", ":=", "fact", "*", "x", ";",
    "x", ":=", "x", "-", "1",
    "endwhile",
    "write", "fact", ";",
    "EOF"
]

demo4 = [
    "read", "identifier", ";",
    "if", "(", "number", "<", "identifier", ")",
    "identifier", ":=", "number", ";",
    "while", "(", "identifier", ">", "number", ")",
    "identifier", ":=", "identifier", "*", "identifier", ";",
    "identifier", ":=", "identifier", "-", "number", ";",
    "endwhile", ";",
    "write", "identifier", ";",
    "EOF"
]

# todo::only for tokenizer TEST
tokenizer_demo = Tokenizer("")
tokenizer_demo.tokens = demo4
