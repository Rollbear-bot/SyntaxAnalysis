# -*- coding: utf-8 -*-
# @Time: 2020/11/27 8:53
# @Author: Rollbear
# @Filename: syntax.py

from entity.tokens import NonTerminalToken, StartToken, TerminalToken
from entity.rule import *


class Syntax:
    """文法"""
    def __init__(self, rules):
        self.rule_set = {rule.forward.token_content: rule for rule in rules}
        self.non_terminal_set = [rule.forward for rule in self.rule_set.values()]
        self.start_token = [token for token in self.non_terminal_set if isinstance(token, StartToken)]

        self.first = {}  # first元素集合
        self.build_first()
        # self.follow = self.build_follow()  # follow元素集合
        self.ll_1_table = None  # LL1分析表

    def build_first(self):
        """构建first集合"""
        for token in self.non_terminal_set:
            self.first[token] = self.get_first_single_stmt(self.rule_set[token.token_content].post)

    def get_first_single_stmt(self, stmt: RuleStmt):
        """
        求一个规则段的first元素集合
        :param stmt: 规则段
        :return: 该规则段的first集合
        """
        first_elem_set = set()

        if isinstance(stmt, TerminalToken):
            first_elem_set.add(stmt)

        elif isinstance(stmt, NonTerminalToken):
            first_elem_set.update(self.get_first_single_token(stmt))

        # 如果规则的开头就是终结符，那么first元素集合直接得到
        elif isinstance(stmt[0], TerminalToken):
            first_elem_set.add(stmt[0])

        # 如果规则的开头是另一非终结符，那么求该非终结符的first
        elif isinstance(stmt[0], NonTerminalToken):
            first_elem_set.update(self.get_first_single_token(stmt[0]))

        # 如果规则开头是分支形式，则进入每个分支，分别求first
        elif isinstance(stmt[0], BranchStmt):
            for branch in stmt[0].branches:
                first_elem_set.update(self.get_first_single_stmt(branch))

        # todo::如果规则开头是正闭包{}
        pass

        # todo::如果规则开头是可选语句[]
        pass

        return first_elem_set

    def get_first_single_token(self, token: NonTerminalToken):
        """
        求单个非终结符的first集合
        :param token: 指定的非终结符
        :return: 该非终结符的first集合
        """
        # 如果所求这个元素的first集合已经求过了，则直接返回
        if token in self.first:
            return self.first[token]

        # 没求过，则进入该非终结符对应的后件语句中求first集合
        post = self.rule_set[token.token_content].post
        if not isinstance(post[0], BranchStmt) and post[0].token_content == token.token_content:
            print("Error: recursion non-terminal-token!")
        return self.get_first_single_stmt(post)

    def build_follow(self):
        """构建follow集合"""
        follow_set = {}
        for token in self.non_terminal_set:
            follow_set[token] = self.get_follow_single_token(token)
        return follow_set

    def get_follow_single_token(self, stmt: RuleStmt):
        """求单个非终结符的follow集合"""
        follow_elem_set = set()
        # todo::得到单个非终结符的follow集合
        return follow_elem_set

    def rules_info(self):
        res = ""
        for rule in self.rule_set.values():
            res += (str(rule) + "\n")
        return res


