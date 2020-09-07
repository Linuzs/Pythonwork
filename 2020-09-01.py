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

username = input("Please input your name:")
password = input("Please input your password:")
hide_password = len(password)

if username == "":
    username = "Player1"
if password == "":
    print("Please input your password!!!")
    exit()

print("########################################")
print("#Welcome to the invincible Heroes game!#")
print("#Your username is %s!"%(username))
print("#Your password is %s!"%(hide_password * "*"))
print("########################################")

https://www.cloudflare.com/
    
    
    
    
    
    
    username = input("Please input your name:")
password = input("Please input your password:")
repeat_password = input("Please input your repeat password:")

error_password = 0
while error_password < 3:
    if username.strip() == "":
        username = "Player1"
    elif password.strip() != "" and repeat_password.strip() != "" and repeat_password.strip() == password.strip():
        print("register success")
        f = open("info.txt", 'a+')
        f.write(username + ' ' + password + '\n')
        f.close()
        print("Please login")
        username = input("username:")
        password = input("password:")
        f2 = open("info.txt",'r')
        res = f2.read()
        #res.close()
        user_list = res.split()
        user_dict = {}
        for i in user_list:
            username = i.split(',')[0]
            password = i.split(',')[1]
            user_dict[username] = password
            print(user_dict)
        break
    else:
        print("error pass")
        break
'''


info = {}
        info['username'] = username
        info['password'] = password
        print(info)
        break
    
    
    
info = {}
info['username'] = username
info['password'] = password
print(info)
 
 '''   
'''
print("########################################")
print("#Welcome to the invincible Heroes game!#")
print("#Your username is %s!"%(username))
print("#Your password is %s!"%(len(password) * "*"))
print("########################################")

info = {}
info['username'] = username
info['password'] = password
print(info)


dict = {'username':'admin','password':'123456'}
username = 'admin'
if username in dict:
    print("x")
else:
    print("dui")
    '''
