num_1 = float(input('enter first number : '))
num_2 = float(input('enter second number : '))
num_3 = float(input('enter third number : '))

#hard way
if num_1 > num_2 and num_1 > num_3:
    print(f'maximum is {num_1}')
elif num_2 > num_1 and num_2 > num_3:
    print(f'maximum is {num_2}')
else:
    print(f'maximum is {num_3}')


# simple way
# print(f'maximum is {max(num_1, num_2, num_3)}')