import math

num_1 = float(input('enter first number : '))
num_2 = float(input('enter second number : '))

num1_pow_num2 = math.pow(num_1, num_2)
num2_pow_num1 = math.pow(num_2, num_1)

print(f'first number power of second number is {num1_pow_num2}')
print(f'second number power of first number is {num2_pow_num1}')