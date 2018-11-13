import os
import platform
import subprocess
from builtins import staticmethod
from tkinter import *
import tkinter.messagebox
from Auth import Auth
from PathMgr import PathMgr
from Logger import Logger


class ReaderGUI(Frame):
    current_panel = 0
    version = "0.1"
    auth = None
    passwordButton = None  # type: Button
    passwordEntry = None  # type: Entry

    log = None
    auth = None

    def __init__(self, master=None):
        Frame.__init__(self, master)

        # Auth
        auth = Auth()

        # 窗口自定义初始化
        self.init()

    def init(self):
        width = 800
        height = 640
        # 窗口标题
        title = "EE V%s" % self.version
        self.master.title(title)

        # 窗口居中
        self.center_window(width, height)
        # 窗口大小
        self.master.maxsize(width, height)
        self.master.minsize(width, height)

        self.create_widgets()

        self.pack()

        # 顶层显示
        self.raise_app()

    def callback_after_idle(self):
        print("callbackAfterIdle")
        self.master.attributes('-topmost', False)
        self.passwordEntry.focus_force()

    def create_widgets(self):
        block1 = Frame(height=2, bd=1, relief="flat")
        block1.pack(fill=X, padx=15, pady=15)
        Label(block1, text='密码:', width=8, anchor="w").pack(side='left')
        self.passwordEntry = Entry(block1)
        self.passwordEntry.pack(side='left')
        self.passwordEntry.bind("<Return>", lambda x: self.on_click_password_button())

        block2 = Frame(height=2, bd=1, relief="flat")
        block2.pack(fill=X, padx=5, pady=5)
        self.passwordButton = Button(block2, width=8, text='确定', command=self.on_click_password_button)
        self.passwordButton.pack()

    def on_click_password_button(self):
        password = self.passwordEntry.get() or ''
        if password == '':
            msg = "请输入密码或向管理者索取密码."
            self.info(msg)
            with os.open("x.txt") as f:
                for line in f.readlines():
                    Logger.info(line)
            return
        self.check_password(password)

    @staticmethod
    def info(msg):
        tkinter.messagebox.showinfo('Message', '%s' % msg)

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
        Logger.info("raise app")
        self.master.lift()
        self.master.attributes("-topmost", True)
        self.master.after(0, lambda: self.master.wm_attributes("-topmost", False))
        if platform.system() == 'Darwin':
            tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
            script = tmpl.format(os.getpid())
            output = subprocess.check_call(['/usr/bin/osascript', '-e', script])
        self.master.after_idle(self.callback_after_idle)


app = ReaderGUI()
# 主消息循环:
app.mainloop()
