# -*- coding: utf-8 -*-
# @Time: 2020/11/27 10:13
# @Author: Rollbear
# @Filename: analyzer.py

from entity.syntax import Syntax
from entity.tokenizer import Tokenizer
from entity.tree import TreeNode
from entity.tokens import TerminalToken, NonTerminalToken, Token
from entity.rule import *
from entity.exception import *


class Analyzer:
    """文法分析器"""

    def __init__(self, syntax: Syntax, tokenizer: Tokenizer, debug=False):
        self.syntax = syntax
        self.tokenizer = tokenizer
        self.tree_root = None
        self._cur_word = None

        self._analyze(debug)

    def _get_token(self):
        """获取下一个单词"""
        return self.tokenizer.__next__()

    def _analyze(self, debug):
        """
        解析文本语法，生成解析树
        1. 每遇到一个新的非终结符，开启一个子节点，节点指针移动到子节点上
        2. 遇到终结符时，为当前节点挂载一个子节点（该终结符），节点指针不移动
        3. 当前匹配的规则到达尾部后，节点指针返回父节点
        4. 匹配规则到达尾部，且没有父节点（到达root）时，结束
        :return: None
        """
        # 从文法的开始符号开始匹配
        cur_stmt = self.syntax.start_token[0]
        self.tree_root = TreeNode(cur_stmt)

        # 递归建立解析树
        try:
            self._cur_word = self._get_token()
            self._analyze_recursion(self.tree_root, debug)
        except ReachEOF:
            if debug:
                print("succeed!")

    def _analyze_recursion(self, cur_node, debug):
        """
        利用递归来实现树的前序伸展与回退
        :param cur_node: 当前指向的树节点
        :return: None
        """
        if isinstance(cur_node.data, TerminalToken):
            stmt = SeqStmt([cur_node.data])
        else:
            stmt = self.syntax.get_stmt_by_token(cur_node.data).post

        for token in stmt:
            # 若当前符号是非终结符，则开启一个子节点，指针移动到新节点
            if isinstance(token, NonTerminalToken):
                if debug:
                    print("-" * 20)
                    print(f"current node: {token.token_content}")
                self._analyze_recursion(cur_node=cur_node.build_child(token), debug=debug)

            # 是终结符，则match它，并挂载到子节点
            elif isinstance(token, TerminalToken):
                if token.match(self._cur_word):
                    if debug:
                        print(f"Terminal token \"{token.token_content}\" matched.")
                    cur_node.build_child(self._cur_word)
                else:
                    # 无法匹配时，报错并退出
                    if debug:
                        print(f"Error in terminal-token matching! "
                              f"expected: \"{token.token_content}\", got: \"{self._cur_word}\"")
                    raise TerminalMatchException

                self._cur_word = self._get_token()  # 获取解析文档的下一个单词
                if self._cur_word == "EOF":
                    if debug:
                        print("reach 'EOF'!")
                    raise ReachEOF

            # 是条件分支时，将当前读到的单词在LL-1中匹配，找出可执行的分支，挂载到子节点，节点指针移动
            # 若没有分支满足条件，则报错并退出
            elif isinstance(token, BranchStmt):
                try:
                    next_stmt = self.syntax.ll_1_table[cur_node.data.token_content][self._cur_word]
                    self._analyze_recursion(cur_node=cur_node.build_child(next_stmt), debug=debug)
                except KeyError:
                    if debug:
                        print(f"Error in branch finding! "
                              f"cur_word: \"{self._cur_word}\"; cur stmt: \"{str(cur_node.data)}\"")
                    raise BranchMatchException

            # 是选择出现语句时
            elif isinstance(token, BooleanStmt):
                # 如果当前单词已经是[]语句末尾的follow，则说明该语句段没有出现，直接匹配下一个语句段
                if self._cur_word in self.syntax.follow[" ".join([str(e) for e in token.tokens])]:
                    continue
                # 否则按照常规的顺序语句匹配
                else:
                    for t in token.tokens:
                        self._analyze_recursion(cur_node.build_child(t), debug=debug)

            # 是循环出现语句时
            elif isinstance(token, RepeatStmt):
                # todo::需要求follow集合，follow元素出现时表示循环出现语句结束
                # 循环直到语句段末尾token的follow出现
                while self._cur_word not in self.syntax.follow[" ".join([str(e) for e in token.tokens])]:
                    # 循环内按照顺序语句匹配
                    for t in token.tokens:
                        self._analyze_recursion(cur_node.build_child(t), debug=debug)

        return  # 当前语句匹配完成后，回退到父节点（递归回溯）

    def get_syntax_tree_str(self):
        """打印语法树"""
        output = "="*10 + "Syntax Tree" + "="*10 + "\n"
        output = self._get_tree_recursion(self.tree_root, depth=0, indent_unit="-", out=output)
        return output

    def _get_tree_recursion(self, cur_node: TreeNode, depth, indent_unit, out):
        """递归实现前序打印语法树"""
        out += indent_unit * depth + str(cur_node.data) + "\n"

        if len(cur_node.children) != 0:
            for child in cur_node.children:
                out = self._get_tree_recursion(child, depth + 1, indent_unit, out)
        return out
