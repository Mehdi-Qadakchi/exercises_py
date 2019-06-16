num = float(input('enter a number : '))

if num != int(num):
    print('you must enter an integer number')
elif num%2==0:
    print('even')
else:
    print('odd')