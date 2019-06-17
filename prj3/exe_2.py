num_1 = int(input('enter first number : '))
num_2 = int(input('enter second number : '))

if num_1 < num_2:
    for i in range(num_1, num_2):
        print(i, end='\t')
elif num_1 >= num_2:
    for j in range(num_1, num_2, -1):
        print(j, end='\t')