num_1 = float(input('enter first number : '))
num_2 = float(input('enter second number : '))
num_3 = float(input('enter third number : '))

# hard way
if num_1 > num_2 and num_1 > num_3:
    if num_2 > num_3:
        print(num_1, num_2, num_3)
    else:
        print(num_1, num_3, num_2)
elif num_2 > num_1 and num_2 > num_3:
    if num_1 > num_3:
        print(num_2, num_1, num_3)
    else:
        print(num_2, num_3, num_1)
elif num_3 > num_1 and num_3 > num_2:
    if num_1 > num_2:
        print(num_3, num_1, num_2)
    else:
        print(num_3, num_2, num_1)