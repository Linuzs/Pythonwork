class Hero():
    def __init__(self, name='Player1', hp=100, atk=10):
        self.name = name
        self.hp = hp
        self.atk = atk
        
    def hit(self, gongji):
        return gongji.hp - self.atk
        
import temp
zhang = temp.Hero('zhangsan')
li = temp.Hero('lisi')

print(li.hit(zhang))


try:
    a = input("输入被除数：")
    b = input("输入除数：")
    c = int(a) / int(b)
except ValueError:
    print("请输入数字")
except ZeroDivisionError:
    print("不能为0")
else:
    print(c)

    
    import tkinter
import turtle
root = tkinter.Tk()
label = tkinter.Label(root,text="你好")
label.pack()
button1 = tkinter.Button(root,text="五角星")
button1.pack()
def wjx(envent):
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
button1.bind('<Button-1>',wjx)
root.mainloop()



import wx
import time

class ChatRoom(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,
                         title = "小小聊天室",
                         size = (520,450),
                         pos = (800,300))
        panel = wx.Panel(frame,-1)
        labelAll = wx.StaticText(panel,-1,'所有聊天内容',
                                 pos = (210,5))
        self.textAll = wx.TextCtrl(panel, -1,
                                   size = (480,200),
                                   pos = (10,30),
                                   style = wx.TE_READONLY|wx.TE_MULTILINE)
        labelIn = wx.StaticText(panel, -1,'输入你想说的话',
                                pos = (230,230))
        self.textIn = wx.TextCtrl(panel,-1,
                                  size = (480,100),
                                  pos = (10,260),
                                  style = wx.TE_MULTILINE)
        
        self.buttonSent = wx.Button(panel,-1,"发送",
                                    size = (75,25),pos = (175,370))
        self.Bind(wx.EVT_BUTTON,
                  self.OnButtonSent,self.buttonSent)
        self.buttonClear = wx.Button(panel,-1,"清空",
                                     size = (75,25),
                                     pos = (260,370))
        self.Bind(wx.EVT_BUTTON,
                  self.OnButtonClear,self.buttonClear)
        
        frame.Show()
        return True
    
    def OnButtonSent(self,event):
        userinput = self.textIn.GetValue()
        self.textIn.Clear()
        nowtime = time.ctime()
        inmsg = "You (%s) :\n%s \n" % (nowtime,userinput)
        self.textAll.AppendText(inmsg)
        
    def OnButtonClear(self,event):
        self.textAll.Clear()

if __name__=="__main__":
    app = ChatRoom()
    app.MainLoop()
