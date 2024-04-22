list_ = [
    ['X', '~', 'X'],
    ['X', '~', 'O'],
    ['~', 'O', '~']
]

for i, item in enumerate(list_):
    if item.count('X') > 1 and '~' in item:
        print(i)