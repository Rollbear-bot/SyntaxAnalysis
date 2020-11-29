# -*- coding: utf-8 -*-
# @Time: 2020/11/29 12:22
# @Author: Rollbear
# @Filename: exception.py

class TerminalMatchException(Exception):
    def __str__(self):
        return "TerminalMatchException"


class ReachEOF(Exception):
    def __str__(self):
        return "ReachEOF"


class BranchMatchException(Exception):
    def __str__(self):
        return "BranchMatchException"
