from entity.rule import *
from entity.tokens import *

# 基础正则表达式的文法规则
# RE运算优先级：重复>连接>分支
RE_SYNTAX_RULES = [
    # ----------------原文法（存在左递归）---------------
    # re -> {stmt}
    # stmt -> branch_stmt
    # -----------------------------------------------
    # branch_stmt -> branch_stmt "|" branch_stmt | seq_stmt
    # seq_stmt -> {seq_stmt} | repeat_stmt
    # repeat_stmt -> repeat_stmt* | prime_stmt
    # prime_stmt -> simple_char | (prime_stmt)
    # -----------------------------------------------
    # simple_char -> letter | digit
    # letter -> a | b .. | A .. | Z
    # digit -> 0 | .. | 9

    # ------------------First集合--------------------
    # first(re)
    # = first(stmt) = first(branch_stmt) = first(seq_stmt)
    # = first(repeat_stmt) = first(prime_stmt)
    # = first(simple_char) + "("
    # = letter + digit + "(

    # ----------------新文法（消除左递归）---------------
    # re -> {stmt}
    # stmt -> branch_stmt
    # -----------------------------------------------
    # branch_stmt -> seq_stmt {"|" seq_stmt}
    # seq_stmt -> repeat_stmt {repeat_stmt}
    # repeat_stmt -> prime_stmt [*]
    # prime_stmt -> simple_char | (prime_stmt)
    # -----------------------------------------------
    # simple_char -> letter | digit
    # letter -> a | b .. | A .. | Z
    # digit -> 0 | .. | 9
    Rule(
        StartToken("re"),
        [RepeatStmt([NonTerminalToken("stmt")])]
    ),
    Rule(
        NonTerminalToken("stmt"),
        [NonTerminalToken("branch_stmt")]
    ),
    Rule(
        NonTerminalToken("branch_stmt"),
        [
            NonTerminalToken("seq_stmt"),
            RepeatStmt([TerminalToken("|"),
                        NonTerminalToken("seq_stmt")])
        ]
    ),
    Rule(
        NonTerminalToken("seq_stmt"),
        [RepeatStmt([NonTerminalToken("repeat_stmt")])]
    ),
    Rule(
        NonTerminalToken("repeat_stmt"),
        [
            NonTerminalToken("prime_stmt"),
            BooleanStmt([TerminalToken("*")])
        ]
    ),
    Rule(
        NonTerminalToken("prime_stmt"),
        [BranchStmt([
            NonTerminalToken("simple_char"),
            SeqStmt([
                TerminalToken("("),
                NonTerminalToken("prime_stmt"),
                TerminalToken(")")
            ])
        ])]
    ),
    Rule(
        NonTerminalToken("simple_char"),
        [BranchStmt([
            NonTerminalToken("letter"),
            NonTerminalToken("digit")
        ])]
    ),
    Rule(
        NonTerminalToken("letter"),
        [BranchStmt(
            [TerminalToken(chr(i))
             for i in list(range(ord("A"), ord("Z") + 1))
             + list(range(ord("a"), ord("z") + 1))]
        )]
    ),
    Rule(
        NonTerminalToken("digit"),
        [BranchStmt(
            [TerminalToken(chr(i))
             for i in range(ord("0"), ord("9") + 1)]
        )]
    )
]
