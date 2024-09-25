some_num = float (input ("Введіть перше число>>"))
some_nun_2 = float (input ("Введіть друге число>>"))
oper = input("Введіть операцію(+,-,*,/)")
if oper == '+':
    print(some_num + some_nun_2 )
elif oper == '-':
    print(some_num - some_nun_2 )
elif oper == '*':
    print(some_num * some_nun_2 )
elif oper == '/':
    if some_nun_2 == 0:
        print("на нуль ділити не можна")
    else:
        print(some_num / some_nun_2 )
else:
    print(" Не вірна операція")

