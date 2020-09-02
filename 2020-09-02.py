number1 = 1
number2 = 2
operator = input("Please input operator(+ - * /):")
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Re input!")

#已知10以内3、5的倍数为3，5，6，9，和为23，计算100以内3，5倍数之和

s = 0
for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0 :
        s+=i
        print(s)

#随机数猜大小

import random

game = "y"
count = 0
rand_number = random.randint(1,100)

while game == "y":
    
    number = input("Please your number:")
    while number.isdigit() == True:
        count+=1
        if int(number) > rand_number:
            print("The number is too big!")
            break
        elif int(number) < rand_number:
            print("The number is too small!")
            break
        elif int(number) == rand_number:
            print("Good luck! Your count is %d."%count)
            game = input('Do you want to continue the game yes or no(input y or n):')
            rand_number = random.randint(1,100)
            count = 0
            break
    else:
        print("Please a number!!!")
else:
    print("Game over.")
    
    
#冰雹序列
number = input("Please your number:")

if number.isdigit() == True:
    number = int(number)
    while number > 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = (number * 3) + 1
            print(number)
else:
    print("Please a number!")
