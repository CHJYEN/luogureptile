"""A demo script to showcase the Sun Valley ttk theme."""
import tkinter
from tkinter import ttk
from tkinter import scrolledtext
import sys
import requests
import sv_ttk
import time
import re
import urllib.request, urllib.error
import bs4
import os
import json
import urllib.parse
import io
import sys
import htk

from reqs_id import *
from reqs_solve import *
from reqs_title import *

list_need = 0
title_need = 0
solve_need = 0
gjc = ""
shijian = 0
difficulty = 0
suanfa = 0
data = []


class CheckBoxDemo(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="需求类型", padding=15)

        global var_1, var_2, var_3

        var_1 = tkinter.BooleanVar()

        var_2 = tkinter.BooleanVar()

        var_3 = tkinter.BooleanVar()

        # 键入特殊题型

        self.add_widgets()

    def add_widgets(self):
        self.checkbox_2 = ttk.Checkbutton(self, text="题单", variable=var_1)

        self.checkbox_2.grid(row=0, column=1, padx=90, pady=10, sticky="w")

        self.checkbox_2 = ttk.Checkbutton(self, text="题目", variable=var_2)

        self.checkbox_2.grid(row=0, column=2, padx=90, pady=10, sticky="w")

        self.checkbox_3 = ttk.Checkbutton(self, text="题解", variable=var_3)

        self.checkbox_3.grid(row=0, column=3, padx=90, pady=10, sticky="w")


class RadioButtonDemo(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, style="Card.TFrame", padding=15)

        self.columnconfigure(0, weight=1)

        self.add_widgets()

    def add_widgets(self):
        self.button = ttk.Button(self, text="给爷 爬!")
        self.button.grid(row=6, column=0, padx=5, pady=10, sticky="ew")



class InputsAndButtonsDemo(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent, style="Card.TFrame", padding=15)

        self.columnconfigure(0, weight=1)

        self.add_widgets()

    def add_widgets(self):
        self.entry = ttk.Label(self, text="条件要求：")

        self.entry.grid(row=0, column=0, padx=0, pady=10, sticky="ew")

        self.entry = ttk.Entry(self)
        self.entry.insert(0, "关键词")

        self.entry.grid(row=0, column=2, padx=(0, 200), pady=10, sticky="ew")

        self.spinbox = ttk.Spinbox(self, from_=0, to=100, increment=0.01)
        # self.spinbox.insert(0, "选择时间")

        # combo_list = ["算法选择", "Ipsum", "Dolor"]

        combo_list1 = ["难度选择", "暂未评定", "入门", "普及-", "普及/提高-", "普及+/提高", "提高+/省选-", "省选/NOI-",
                       "NOI/NOI+/CTSC"]

        self.combobox = ttk.Combobox(self, values=combo_list1)

        self.combobox.current(0)
        self.combobox.grid(row=0, column=1, padx=(100, 250), pady=10, sticky="ew")

        # self.readonly_combo = ttk.Combobox(self, state="readonly", values=combo_list)
        # self.readonly_combo.current(0)

        self.menu = tkinter.Menu(self)

        for n in range(1, 5):
            self.menu.add_command(label=f"难度选择 {n}")

        self.button = ttk.Button(self, text="开始")
        self.button.grid(row=6, column=1, padx=(250, 0), pady=10, sticky="ew")

        def on_button_click():

            print("正在慢慢爬噢")
            global list_need, title_need, solve_need, gjc, difficulty

            list_need = var_1.get()
            title_need = var_2.get()
            solve_need = var_3.get()

            gjc = self.entry.get()
            difficulty1 = self.combobox.get()
            rg = 0
            for ii in range(1, 10):
                if difficulty1 == combo_list1[ii]:
                    rg = ii-1
                    break

            # PanedDemo(self).grid(row=0, column=0, rowspan=2, padx=0, pady=(10, 0))
            time.sleep(5)
            # print("list_need: ", list_need)
            # print("title_need: ", title_need)
            # print("solve_need: ", solve_need)
            # print(difficulty1)
            if list_need:
                r_id()
            if title_need:
                main_title(rg)
            if solve_need:
                main_solve()

        self.button.config(command=on_button_click)





class PanedDemo(ttk.PanedWindow):
    def __init__(self, parent):
        super().__init__(parent)

        self.pane_1 = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.add(self.pane_1, weight=1)

        self.var = tkinter.IntVar(self, 47)

        self.add_widgets()

    def write(self, text):
        self.text_widget.insert(tkinter.END, text)
        self.text_widget.see(tkinter.END)  # 滚动到文本框底部

    def add_widgets(self):

        self.notebook = ttk.Notebook(self.pane_1)
        self.notebook.pack(expand=True, fill="both")

        for n in range(1):
            setattr(self, f"tab_{n}", ttk.Frame(self.notebook))
            self.notebook.add(getattr(self, f"tab_{n}"), text=f"界面颜色调整")

        for index in range(2):
            self.tab_0.columnconfigure(index, weight=1)
            self.tab_0.rowconfigure(index, weight=1)

        self.switch = ttk.Checkbutton(
            self.tab_0, text="Dark theme", style="Switch.TCheckbutton", command=sv_ttk.toggle_theme
        )

        self.switch.grid(row=1, column=0, columnspan=2, pady=10)


class PrintRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tkinter.END, text)
        self.text_widget.see(tkinter.END)  # 滚动到文本框底部


class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=40)

        for index in range(3):
            self.columnconfigure(index, weight=1)
            self.rowconfigure(index, weight=1)

        """
        CheckBoxDemo(self).grid(row=0, column=0, padx=(0, 10), pady=(0, 20), sticky="nsew")
        RadioButtonDemo(self).grid(row=1, column=0, padx=(0, 10), sticky="nsew")
        InputsAndButtonsDemo(self).grid(
            row=0, column=1, rowspan=2, padx=10, pady=(10, 0), sticky="nsew"
        )
        """
        InputsAndButtonsDemo(self).grid(
            row=1, column=0, rowspan=1, padx=(0, 10), pady=0, sticky="nsew"
        )
        CheckBoxDemo(self).grid(row=0, column=0, rowspan=1, padx=(0, 10), pady=0, sticky="nsew")

        # RadioButtonDemo(self).grid(row=2, column=0, padx=(0, 10), sticky="nsew")


def main():
    root = tkinter.Tk()
    # 创建带有垂直滚动条的文本框用于显示print输出
    text_widget = scrolledtext.ScrolledText(root, width=80, height=30)  # 设置文本框大小
    text_widget.pack(side=tkinter.BOTTOM, padx=10, pady=10)  # 设置文本框的位置和边距
    sys.stdout = PrintRedirector(text_widget)
    root.title("")
    sv_ttk.set_theme("light")
    App(root).pack(expand=True, fill="both")
    root.mainloop()


if __name__ == "__main__":
    main()