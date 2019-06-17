total = 0
counter = 10
for i in range(10):
    num = int(input('enter a number ({0}) : '.format(counter)))
    total += num
    counter -= 1

print(total)