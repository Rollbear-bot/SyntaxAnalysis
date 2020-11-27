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
        self.ll_1_table = {}  # LL1分析表

        self.build_first()
        self.build_ll_1_table()
        # self.follow = self.build_follow()  # follow元素集合

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

        # 当前规则段就是单个符号（终结符/非终结符）的情况
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

    def build_ll_1_table(self):
        """建立LL1分析表"""
        for token in self.non_terminal_set:
            table_row = {}
            post = self.rule_set[token.token_content].post

            # 多路分支规则另外处理，需要关联每个分支的first与执行的子规则
            if isinstance(post[0], BranchStmt):
                for branch in post[0].branches:
                    f_set = self.get_first_single_stmt(branch)
                    for f in f_set:
                        if f in table_row:
                            print("Error: multiple stmt link to a first element!",
                                  str(table_row[f]), str(branch))
                        table_row[f.token_content] = branch
            else:
                for f in self.first[token]:
                    table_row[f.token_content] = post

            self.ll_1_table[token.token_content] = table_row

    def rules_info(self):
        """打印该语法包含的规则"""
        res = ""
        for rule in self.rule_set.values():
            res += (str(rule) + "\n")
        return res

    def print_ll_1_table_info(self):
        """打印LL1分析表"""
        json_like = {}
        for key, row in self.ll_1_table.items():
            r = {str(k): str(v) for k, v in row.items()}
            json_like[str(key)] = r
        print("="*20 + "LL1" + "="*20)
        for forward, rule_table in json_like.items():
            print(f"\n{forward}\n" + "\n".join([f"{f}: {rule}" for f, rule in rule_table.items()]))
