绝对值
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x

print(my_abs(-10))

随机数
import random
strlist = '0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ'

def random_code(x):
    code = ""
    for i in range(x):
        num = random.randint(0,len(strlist))
        code += strlist[num]
    return code

number = int(input("请输入位数："))
print(random_code(number))
