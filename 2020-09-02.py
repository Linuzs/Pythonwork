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
