num = int(input('enter a number for looping : '))
total = 0

for i in range(num):
    n = int(input(f'Enter a number ({i}): '))
    total += n

print(total)
