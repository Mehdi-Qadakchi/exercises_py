num_1 = int(input('enter first integer number : '))
num_2 = int(input('enter second integer number : '))

if num_1 <= num_2:
    for i in range(num_1, num_2):
        print(i, end='\t')
else:
    print('first number must be greater than second number')

