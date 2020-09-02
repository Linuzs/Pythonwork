ip = '192.168.1.3'
list = ip.split('.')
print(list)

str = 'bad luck'
new_str = str.replace('bad','good')
print(new_str)

str1 = 'bad bad luck'
list_str = str1.split()
list_str[1] = 'good'
print(" ".join(list_str))


import random
strlist = '0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ'
code = ""
for i in range(4):
    num = random.randint(0,len(strlist))
    code += strlist[num]
print(code)
