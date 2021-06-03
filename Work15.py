# 图形界面
# tkinter
from tkinter import *
import tkinter.messagebox as messagebox

class App1(Frame):
    def __init__(self,master=None): 
        Frame.__init__(self,master)
        self.pack() 
        self.makeup()
    
    def makeup(self):
        self.label1 = Label(self,text='Hello,world!') # self指定这个控件的master，即这个控件属于哪一个
        self.label1.pack() #pack()方法把Widget加入到父容器中，并实现布局
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='Hello',command=self.sayhi)
        self.alertButton.pack()
        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()
    
    def sayhi(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s' % name)
    
app1 = App1()
#设置窗口标题
app1.master.title('Hello World')
#设置窗口宽、高、位置
app1.master.geometry('400x300+600+450')
#开启主消息循环
app1.mainloop()

# Turtle Graphics (海龟绘图)
from turtle import *

def drawRect(w=200,h=200):

    # 设置笔刷宽度:
    width(4)
    # 前进:
    forward(w)
    # 右转90度:
    right(90)
    # 笔刷颜色:
    pencolor('red')
    forward(h)
    right(90)

    pencolor('green')
    forward(w)
    right(90)

    pencolor('blue')
    forward(h)
    right(90)

    # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
    done()

drawRect(300,300)