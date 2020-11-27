# -*- coding: utf-8 -*-
# @Time: 2020/11/27 9:03
# @Author: Rollbear
# @Filename: tiny_syntax_rules.py

from entity.rule import *
from entity.tokens import *

TINY_SYNTAX_RULES = [
    Rule(
        StartToken("program"),
        [NonTerminalToken("stmt-sequence")]),
    Rule(
        NonTerminalToken("stmt-sequence"),
        [NonTerminalToken("statement"),
         RepeatStmt([TerminalToken(";"), NonTerminalToken("statement")])]),
    Rule(
        NonTerminalToken("statement"),
        [BranchStmt([
            NonTerminalToken("if-stmt"),
            NonTerminalToken("repeat-stmt"),
            NonTerminalToken("assign-stmt"),
            NonTerminalToken("read-stmt"),
            NonTerminalToken("write-stmt")
        ])]),
    Rule(
        NonTerminalToken("if-stmt"),
        [
            TerminalToken("if"),
            NonTerminalToken("exp"),
            TerminalToken("then"),
            NonTerminalToken("stmt-sequence"),
            BooleanStmt([
                TerminalToken("else"),
                NonTerminalToken("stmt-sequence")
            ]),
            TerminalToken("end")
        ]
    ),
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
        [BranchStmt([TerminalToken("<"), TerminalToken("=")])]
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
    )
]
