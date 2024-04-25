def update_pole(pole: list) -> bool:
    print(f'| - | 0 | 1 | 2 |')
    print(f'-'*17)
    for num, item in enumerate(pole):
        print(f'| {num} | {" | ".join(item)} |')
        print(f'-'*17)
    return check_end(pole)

def check_win(pole: list) -> bool:
    for item_pole in pole:
        if item_pole.count('X') == 3:
            print('Победитель: Игрок')
            return True
        if item_pole.count('O') == 3:
            print('Победитель: Соперник')
            return True
    return False

def check_end(pole: list) -> bool:
    list_y = [
        [pole[0][0], pole[1][0], pole[2][0]],
        [pole[0][1], pole[1][1], pole[2][1]],
        [pole[0][2], pole[1][2], pole[2][2]],
    ]
    list_x_y = [
        [pole[0][0], pole[1][1], pole[2][2]],
        [pole[2][0], pole[1][1], pole[0][2]]
    ]

    if not pole[0].count('~') and not pole[1].count('~') and not pole[2].count('~'):
        print("Ничья!")
        return True
    
    if check_win(pole): return True
    elif check_win(list_y): return True
    elif check_win(list_x_y): return True
    
    return False