# -*- coding: utf-8 -*-
# @Time: 2020/11/27 8:53
# @Author: Rollbear
# @Filename: syntax.py

from entity.tokens import NonTerminalToken, StartToken, TerminalToken
from entity.rule import *


class Syntax:
    """文法"""
    def __init__(self, rules):
        self.rule_set = {rule.forward: rule for rule in rules}
        self.non_terminal_set = [rule.forward for rule in self.rule_set.values()]
        self.start_token = [token for token in self.non_terminal_set if isinstance(token, StartToken)]

        # self.first = self.build_first()  # first元素集合
        # self.follow = self.build_follow()  # follow元素集合
        self.ll_1_table = None  # LL1分析表

    def build_first(self):
        """构建first集合"""
        first_set = {}
        for token in self.non_terminal_set:
            first_set[token] = self.get_first_single_token(self.rule_set[token].post, first_set.copy())
        return first_set

    def get_first_single_stmt(self, stmt: RuleStmt):
        pass

    def get_first_single_token(self, token: NonTerminalToken, cur_first_dict):
        """求单个非终结符的first集合"""
        # 如果所求这个元素的first集合已经求过了，则直接返回
        if token in cur_first_dict:
            return cur_first_dict[token]

        first_elem_set = set()
        post = self.rule_set[token].post

        # 如果规则的开头就是终结符，那么first元素集合直接得到
        if isinstance(post[0], TerminalToken):
            first_elem_set.add(post[0])

        # 如果规则开头是分支形式，则进入每个分支
        elif isinstance(post[0], BranchStmt):
            for branch in post[0].branches:
                pass

        return first_elem_set

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


