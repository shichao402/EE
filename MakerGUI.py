import json
import os
import platform
import subprocess
from builtins import staticmethod
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox

import PathType
from Auth import Auth
from PathMgr import PathMgr
from Logger import Logger


class MakerGUI(Frame):
    progress: ttk.Progressbar
    version: str = "0.1"
    select_file_path: str
    select_file_path_entry: Entry

    # obj
    auth: Auth = None
    log = None

    # tk
    select_file_button = None  # type: Button
    passwordEntry = None  # type: Entry

    def __init__(self, master=None):
        Frame.__init__(self, master)


        # Auth
        auth = Auth()

        # 窗口自定义初始化
        self.init()

    def init(self):
        # 窗口标题
        title = "EE V%s" % self.version
        self.master.title(title)

        # 窗口居中
        self.center_window(800, 640)
        # 窗口大小
        self.master.maxsize(800, 640)
        self.master.minsize(800, 640)

        self.create_widgets()

        # 顶层显示
        self.raise_app()
        self.pack()

    def callback_after_idle(self):
        print("callbackAfterIdle")
        self.master.attributes('-topmost', False)

    def create_widgets(self):
        # update cache
        with open(PathMgr.get_path(PathType.PathType.CacheConfigPath), "w") as f:
            f.write(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))


        label = Label(self, text='选择要拆分的Excel文件:')
        label.grid(row=0, column=0)

        self.select_file_path_entry = Entry(self)
        self.select_file_path_entry.insert(0, self.select_file_path)
        self.select_file_path_entry.configure(state='readonly')
        self.select_file_path_entry.grid(row=0, column=1)

        self.select_file_button = Button(self, text="确定", command=self.on_click_file_select)
        self.select_file_button.grid(row=0, column=2)

        # self.progress = ttk.Progressbar(orient="horizontal", length=200, mode="determinate")
        # self.progress.pack()
        # self.progress["value"] = 0
        # self.progress["maximum"] = 500
        # self.update_progress()

    def on_click_file_select(self):
        self.select_file_path = tkinter.filedialog.askopenfilename(
            initialdir=".",
            title="选择要制作的Excel文件",
            filetypes=(
                ("test", "*.py"),
                ("Excel", "*.xlsx"),
                ("all files", "*.*")
            )
        )
        Logger.info("select file path: %s" % self.select_file_path)
        self.select_file_path_entry.insert(0, "fdasfdsafsda")
        pass

    # 居中窗口封装
    def center_window(self, width, height):
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.master.geometry(size)

    def check_password(self, password):
        print(password)
        pass

    def raise_app(self):
        self.master.lift()
        self.master.attributes("-topmost", True)
        if platform.system() == 'Darwin':
            tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
            script = tmpl.format(os.getpid())
            output = subprocess.check_call(['/usr/bin/osascript', '-e', script])
        self.master.after(0, lambda: self.master.attributes("-topmost", False))
        self.master.after_idle(self.callback_after_idle)

    def update_progress(self):
        self.progress["value"] = self.progress["value"] + 1
        if self.progress["value"] < self.progress["maximum"]:
            self.after(100, self.update_progress)
        pass


app = MakerGUI()
# 主消息循环:
app.mainloop()
