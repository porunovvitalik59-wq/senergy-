x = int(input()) #Минимальная сумма инвестиций 
a = int(input()) #Майкл
b = int(input()) #Иван

can_mike = a >= x
can_ivan = b >= x
together_enough = (a + b) >= x

if can_mike and can_ivan:
    print(2)
elif can_mike:
    print("Mike")
elif can_ivan:
    print("Ivan")
elif together_enough:
    print(1)
else:
    print(0)