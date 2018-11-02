# -*- coding: utf-8 -*- 
from Tkinter import *
import tkMessageBox
import os,subprocess,platform

class Application(Frame):
    version="0.1"
    def __init__(self, master=None):
        Frame.__init__(self, master)

        #自定义初始化
        self.init()

    def init(self):
        #窗口标题
        title="EE V%s" % self.version
        self.master.title(title)

        #窗口居中
        self.center_window(300, 240)
        #窗口大小
        self.master.maxsize(600, 400)
        self.master.minsize(300, 240)

        self.createWidgets()
        #顶层显示
        self.raiseApp()

        self.pack()

    def callbackAfterIdle(self):
        print "callbackAfterIdle"
        self.master.attributes('-topmost', False)
        self.passwordEntry.focus_force()


    def createWidgets(self):
        block1 = Frame(height=2, bd=1, relief="flat")
        block1.pack(fill=X, padx=15, pady=15)
        Label(block1,text = '密码:', width=8, anchor="w").pack(side = 'left')
        self.passwordEntry = Entry(block1)
        self.passwordEntry.pack(side = 'left')
        self.passwordEntry.bind("<Return>", lambda x : self.onClickPasswordButton()) 

        block2 = Frame(height=2, bd=1, relief="flat")
        block2.pack(fill=X, padx=5, pady=5)
        self.passwordButton = Button(block2, width=8, text='确定', command=self.onClickPasswordButton)
        self.passwordButton.pack()


    def onClickPasswordButton(self):
        password = self.passwordEntry.get() or ''
        if password == '':
            msg = "请输入密码或向管理者索取密码."
            self.Info(msg)
            return
        self.CheckPassword(password)

    def Info(self, msg):
        tkMessageBox.showinfo('Message', '%s' % msg)

    #居中窗口封装
    def center_window(self, width, height):
	    screenwidth = self.winfo_screenwidth()
	    screenheight = self.winfo_screenheight()
	    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
	    self.master.geometry(size)

    def CheckPassword(self, password):
        print password

    def raiseApp(self):
        self.master.attributes("-topmost", True)
        if platform.system() == 'Darwin':
            tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
            script = tmpl.format(os.getpid())
            output = subprocess.check_call(['/usr/bin/osascript', '-e', script])
        # self.master.after(0, lambda: self.master.attributes("-topmost", False))
        self.master.after_idle(self.callbackAfterIdle)



app = Application()
# 主消息循环:
app.mainloop()
