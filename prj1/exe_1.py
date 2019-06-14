num_1 = input('Enter first number : ')
num_2 = input('Enter second number : ')

if num_1.isnumeric() and num_2.isnumeric():
    print(int(num_1) + int(num_2))
else:
    print('you must just enter an integer number (strings/floating points NOT allowed)')