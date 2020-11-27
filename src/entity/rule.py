# -*- coding: utf-8 -*-
# @Time: 2020/11/27 8:52
# @Author: Rollbear
# @Filename: rule.py

from entity.tokens import NonTerminalToken


class RuleStmt:
    def __init__(self, tokens):
        self.tokens = tokens

    def __str__(self):
        pass

    def __getitem__(self, item):
        return self.tokens[item]


class BranchStmt(RuleStmt):
    """分支|"""
    def __init__(self, branches: iter):
        super().__init__(tokens=None)
        self.branches = branches

    def __str__(self):
        return " | ".join([str(elem) for elem in self.branches])


class BooleanStmt(RuleStmt):
    """出现0或1次[]"""
    def __init__(self, tokens):
        super().__init__(tokens)

    def __str__(self):
        return f"[{' '.join([str(elem) for elem in self.tokens])}]"


class RepeatStmt(RuleStmt):
    """出现一次或多次{}"""
    def __init__(self, tokens):
        super().__init__(tokens)

    def __str__(self):
        return "{" + " ".join([str(elem) for elem in self.tokens]) + "}"


class SeqStmt(RuleStmt):
    """顺序出现"""
    def __init__(self, tokens):
        super().__init__(tokens)

    def __str__(self):
        return " ".join([str(elem) for elem in self.tokens])

    def __iter__(self):
        return iter(self.tokens)

    def __getitem__(self, item):
        return self.tokens[item]


class Rule:
    def __init__(self, f: NonTerminalToken, p):
        self.forward = f  # 前键
        self.post = SeqStmt(p) if isinstance(p, list) else None   # 后键

    def __str__(self):
        return str(self.forward) + " -> " +\
               " ".join([str(elem) for elem in self.post])
