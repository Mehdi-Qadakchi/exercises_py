num = int(input('enter a number for factorial calculation : '))
num_list = list(range(num, 0, -1))
total = 1

for i in range(num):
    # print(num_list[i], end='\t')
    total *= num_list[i]

print(total)