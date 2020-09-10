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
