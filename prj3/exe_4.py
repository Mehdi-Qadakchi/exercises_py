num = int(input('enter a number for looping : '))
total = 0

for i in range(num):
    x = int(input('enter a number ({}): '.format(num)))
    num -= 1
    total += x

print(total)