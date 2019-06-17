num = int(input('enter a number : '))
total = 0
num_list = list(range(1, num+1))
print(num_list)

for i in range(num):
    # print(num_list[i]**3, end='\t')
    total += num_list[i]**3

print('\ncubic total of these numbers are : ', total)