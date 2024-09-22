octal_number = input("Введите число в восьмеричной системе счисления (5 чисел): ")

if len(octal_number) == 5:
    decimal_number = int(octal_number, 8)
    print(f"Число в десятичной системе счисления: {decimal_number}")
else:
    print("Ошибка: Введите число, состоящее из 5 разрядов.")