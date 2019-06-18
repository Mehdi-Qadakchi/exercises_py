num_1 = input('Enter first integer number : ')
num_2 = input('Enter second integer number : ')

if num_1.isnumeric() and num_2.isnumeric():
    print(int(num_1) + int(num_2))
else:
    print('you must just enter an integer number (strings/floating points NOT allowed)')
