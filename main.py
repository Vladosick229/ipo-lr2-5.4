numbers_input = input("Введите восьмиричное число через пробел: ")

n1 = int(numbers_input[0])
n2 = int(numbers_input[1])
n3 = int(numbers_input[2])
n4 = int(numbers_input[3])
n5 = int(numbers_input[4])

res = (n1 * 8 ** 4) + (n2 * 8 ** 3) + (n3 * 8 ** 2) + (n4 * 8 ** 1) + (n5 * 8 ** 0)

print(f"Число в десятичной системе счисления: {res}")