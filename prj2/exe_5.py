food_list = ['Hot Dog', 'Pizza', 'Hamburger', 'Bread', 'Cheese']

print('''
1.\tHot Dog
2.\tPizza
3.\tHamburger
4.\tBread
5.\tCheese
''')
food_id = int(input('enter your food id : '))


if food_id in range(1, len(food_list)+1):
    print(f'you choose {food_list[food_id - 1]}')
else:
    print('\nthis id is not in food list')
