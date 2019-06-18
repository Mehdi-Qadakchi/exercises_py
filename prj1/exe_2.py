num_1 = input('Enter first number : ')
num_2 = input('Enter second number : ')
operator = input('Enter your operator (+ - * /) : ')

if operator == '+':
    print(float(num_1) + float(num_2))
elif operator == '-':
    print(float(num_1) - float(num_2))
elif operator == '*':
    print(float(num_1) * float(num_2))
elif operator == '/':
    if float(num_2) == 0.0:
        print('error zero devision')
        # Here is the situation that you can use raise stetement
    else:
        print(float(num_1) / float(num_2))
else:
    print('Please enter one of these operators * - + /') 
