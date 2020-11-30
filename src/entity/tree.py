# -*- coding: utf-8 -*-
# @Time: 2020/11/27 16:54
# @Author: Rollbear
# @Filename: tree.py

class TreeNode:
    def __init__(self, data, p=None):
        self.data = data
        self._parent = p
        self._children = []

    def build_child(self, data):
        child_ptr = TreeNode(data, p=self)
        self._children.append(child_ptr)
        return child_ptr

    def get_parent(self):
        return self._parent

    def is_root(self):
        return self._parent is None

    def is_leaf(self):
        return len(self._children) == 0

    @property
    def children(self):
        return self._children
