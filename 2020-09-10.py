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
