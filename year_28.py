year = int(input("Введите год: "))


#цепочка

if year % 4 != 0:
    print("Обычный")
elif year % 400 == 0:
    print("Високосный")
elif year % 100 != 0:
    print("Високосный")
else:
    print("Обычный")


#вложенность

if year % 4 == 0:
    if year % 100 != 0:
        print("Високосный")
    else:
        if year % 400 == 0:
            print("Високосный")
        else:
            print("Обычный")
else:
    print("Обычный")


#логические операторы

if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    print("Високосный")
else:
    print("Обычный")