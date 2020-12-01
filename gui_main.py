# -*- coding: utf-8 -*-
# @Time: 2020/11/29 16:21
# @Author: Rollbear
# @Filename: gui_main.py

import tkinter
from tkinter import *
from tkinter import messagebox

from entity.tokenizer import Tokenizer
from entity.analyzer import Analyzer
from entity.exception import TerminalMatchException, BranchMatchException

from res.tiny_syntax import TINY_SYNTAX


# 根面板
root = Tk()  # 创建窗口对象的背景色
root.geometry("1200x800")
root.title("Extent Tiny Syntax Analyzer")

# 初始化文本
CPP_PATH = ""
file_path_str_obj = StringVar()
file_path_str_obj.set("请输入源代码：")

# 初始化组件
label_file_path = Label(root, textvariable=file_path_str_obj)
entry_field = Entry(root, show=None)

# 创建滚动条
# scroll = tkinter.Scrollbar()

# 创建展示解析结果的文本框
text = tkinter.Text(root)
# 用于图片描述的label
log_describe_label = Label(root, text="Log：")
rules_describe_label = Label(root, text="已加载的文法规则：")

# 输出log与规则的区域
log_text = Text(root)
rules_text = Text(root)


def run():
    if entry_field.get() == "":
        messagebox.askokcancel("确认",
                               f"你还没有输入表达式")
    else:
        try:
            tokenizer = Tokenizer(doc=entry_field.get())
            analyzer = Analyzer(syntax=TINY_SYNTAX, tokenizer=tokenizer, debug=True)

            # 清空文本框并刷新
            text.delete(0.0, END)
            text.insert("insert", "语法解析树：\n" + analyzer.get_syntax_tree_str())

            rules_text.delete(0.0, END)
            rules_text.insert("insert", analyzer.syntax.rules_info())

            log_text.delete(0.0, END)
            log_text.insert("insert", analyzer.analyze_log)

        except TerminalMatchException as e:
            log_text.delete(0.0, END)
            log_text.insert("insert", str(TerminalMatchException) + "\n" + e.info + "\nfailed!")
        except BranchMatchException as e:
            log_text.delete(0.0, END)
            log_text.insert("insert", str(BranchMatchException) + "\n" + e.info + "\nfailed!")


if __name__ == '__main__':
    label_file_path.grid(row=0, column=0)
    entry_field.grid(row=1, column=0)

    # 开始解析的按钮
    button_run = Button(root, command=run, text="开始分析")
    button_run.grid(row=2, column=0)

    text.grid(row=3, column=0)

    log_describe_label.grid(row=0, column=1)
    log_text.grid(row=1, column=1)
    rules_describe_label.grid(row=2, column=1)
    rules_text.grid(row=3, column=1)

    root.mainloop()
