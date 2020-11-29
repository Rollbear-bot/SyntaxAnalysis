# -*- coding: utf-8 -*-
# @Time: 2020/11/27 9:03
# @Author: Rollbear
# @Filename: extent_tiny_syntax_rules.py

from entity.rule import *
from entity.tokens import *

# Tiny语言的扩展语法规则
EXTENT_TINY_SYNTAX_RULES = [
    Rule(
        StartToken("program"),
        [NonTerminalToken("stmt-sequence")]),
    Rule(
        NonTerminalToken("stmt-sequence"),
        [
            RepeatStmt([
                NonTerminalToken("statement"),
                TerminalToken(";")
            ])
        ]
    ),
    Rule(
        NonTerminalToken("statement"),
        [BranchStmt([
            NonTerminalToken("if-stmt"),
            NonTerminalToken("repeat-stmt"),
            NonTerminalToken("assign-stmt"),
            NonTerminalToken("read-stmt"),
            NonTerminalToken("write-stmt"),
            NonTerminalToken("While-stmt"),
            NonTerminalToken("Dowhile-stmt"),
            NonTerminalToken("for-stmt")
        ])]),
    Rule(
        NonTerminalToken("repeat-stmt"),
        [
            TerminalToken("repeat"),
            NonTerminalToken("stmt-sequence"),
            TerminalToken("until"),
            NonTerminalToken("exp")
        ]
    ),
    Rule(
        NonTerminalToken("assign-stmt"),
        [
            TerminalToken("identifier"),
            TerminalToken(":="),
            NonTerminalToken("exp")
        ]
    ),
    Rule(
        NonTerminalToken("read-stmt"),
        [
            TerminalToken("read"),
            TerminalToken("identifier")
        ]
    ),
    Rule(
        NonTerminalToken("write-stmt"),
        [
            TerminalToken("write"),
            NonTerminalToken("exp")
        ]
    ),
    Rule(
        NonTerminalToken("exp"),
        [
            NonTerminalToken("simple-exp"),
            BooleanStmt([
                NonTerminalToken("comparison-op"),
                NonTerminalToken("simple-exp")
            ])
        ]
    ),
    Rule(
        NonTerminalToken("comparison-op"),
        [BranchStmt([TerminalToken("<"), TerminalToken("="), TerminalToken(">")])]
    ),
    Rule(
        NonTerminalToken("simple-exp"),
        [
            NonTerminalToken("term"),
            RepeatStmt([
                NonTerminalToken("addop"),
                NonTerminalToken("term")
            ])
        ]
    ),
    Rule(
        NonTerminalToken("addop"),
        [BranchStmt([TerminalToken("+"), TerminalToken("-")])]
    ),
    Rule(
        NonTerminalToken("term"),
        [
            NonTerminalToken("factor"),
            RepeatStmt([
                NonTerminalToken("mulop"),
                NonTerminalToken("factor")
            ])
        ]
    ),
    Rule(
        NonTerminalToken("mulop"),
        [BranchStmt([TerminalToken("*"), TerminalToken("/")])]
    ),
    Rule(
        NonTerminalToken("factor"),
        [
            BranchStmt([
                SeqStmt([
                    TerminalToken("("),
                    NonTerminalToken("exp"),
                    TerminalToken(")")
                ]),
                TerminalToken("number"),
                TerminalToken("identifier")
            ])
        ]
    ),
    Rule(
        NonTerminalToken("While-stmt"),
        [
            TerminalToken("while"),
            TerminalToken("("),
            NonTerminalToken("exp"),
            TerminalToken(")"),
            NonTerminalToken("stmt-sequence"),
            TerminalToken("endwhile")
        ]
    ),
    Rule(
        NonTerminalToken("Dowhile-stmt"),
        [
            TerminalToken("do"),
            NonTerminalToken("stmt-sequence"),
            TerminalToken("while"),
            TerminalToken("("),
            NonTerminalToken("exp"),
            TerminalToken(")"),
            TerminalToken(";")
        ]
    ),
    # todo::for语句有两个，需要合并以及去公因子，判断分支可能会出现问题
    Rule(
        NonTerminalToken("for-stmt"),
        [
            TerminalToken("for"),
            TerminalToken("identifier"),
            TerminalToken(":="),
            NonTerminalToken("simple-exp"),
            BooleanStmt([TerminalToken("to")]),
            BooleanStmt([TerminalToken("downto")]),
            NonTerminalToken("simple-exp"),
            TerminalToken("do"),
            NonTerminalToken("stmt-sequence"),
            TerminalToken("enddo")
        ]
    ),
    # todo::+=, %, ^, <=, <> 的运算需要在文法中实现运算优先级
    # Rule(
    #     NonTerminalToken("+="),
    #     []
    # ),
    Rule(
        NonTerminalToken("if-stmt"),
        [
            TerminalToken("if"),
            TerminalToken("("),
            NonTerminalToken("exp"),
            TerminalToken(")"),
            NonTerminalToken("stmt-sequence"),
            BooleanStmt([
                TerminalToken("else"),
                NonTerminalToken("stmt-sequence")
            ])
        ]
    )
]
