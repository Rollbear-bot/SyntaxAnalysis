# -*- coding: utf-8 -*-
# @Time: 2020/11/29 12:22
# @Author: Rollbear
# @Filename: exception.py

class TerminalMatchException(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return self.info


class ReachEOF(Exception):
    def __str__(self):
        return "ReachEOF"


class BranchMatchException(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return self.info
