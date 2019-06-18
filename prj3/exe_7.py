num = int(input('enter an integer number : '))
num_list = []

for i in range(num):
    entrance_num = int(input('enter {0} number respectively : '.format(num)))
    num -= 1
    num_list.append(entrance_num)

print(num_list)

if 0 in num_list:
    print(f'\nhow many zero in this list? {num_list.count(0)} zero(s)')