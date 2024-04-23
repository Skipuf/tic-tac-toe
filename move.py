def robot_move(pole: list) -> None:
    list_y = [
        [pole[0][0], pole[1][0], pole[2][0]],
        [pole[0][1], pole[1][1], pole[2][1]],
        [pole[0][2], pole[1][2], pole[2][2]],
    ]
    list_x_y = [
        [pole[0][0], pole[1][1], pole[2][2]],
        [pole[2][0], pole[1][1], pole[0][2]]
    ]

    for i, item_pole in enumerate(pole):
        if item_pole.count('O') == 2 and '~' in item_pole:
            for j, item in enumerate(item_pole):
                if item == '~':
                    pole[i][j] = 'O'
                    return f"{i}{j}"
        if item_pole.count('X') == 2 and '~' in item_pole:
            for j, item in enumerate(item_pole):
                if item == '~':
                    pole[i][j] = 'O'
                    return f"{i}{j}"

    for i, item_y in enumerate(list_y):
        if item_y.count('O') == 2 and '~' in item_y:
            for j, item in enumerate(item_y):
                if item == '~':
                    pole[j][i] = 'O'
                    return f"{j}{i}"
        if item_y.count('X') == 2 and '~' in item_y:
            for j, item in enumerate(item_y):
                if item == '~':
                    pole[j][i] = 'O'
                    return f"{j}{i}"

    for i, item_x_y in enumerate(list_x_y):
        if item_x_y.count('O') == 2 and '~' in item_x_y:
            for j, item in enumerate(item_x_y):
                if item == '~':
                    if i == 0 or j == 1:
                        pole[j][j] = 'O'
                        return f"{j}{j}"
                    else:
                        if j:
                            pole[0][2] = 'O'
                            return "02"
                        else:
                            pole[2][0] = 'O'
                            return "20"
        if item_x_y.count('X') == 2 and '~' in item_x_y:
            for j, item in enumerate(item_x_y):
                if item == '~':
                    if i == 0 or j == 1:
                        pole[j][j] = 'O'
                        return f"{j}{j}"
                    else:
                        if j:
                            pole[0][2] = 'O'
                            return "02"
                        else:
                            pole[2][0] = 'O'
                            return "20"
    if pole[1][1] == '~':
        pole[1][1] = 'O'
        return "11"
    for i, item_pole in enumerate(pole):
        for j, item in enumerate(item_pole):
            if item == '~':
                pole[i][j] = 'O'
                return f"{i}{j}"

def player_move(move: str, pole: list) -> bool:
    try:
        move = [int(move[0]), int(move[1])]
    except BaseException:
        print("число введено неверно!")
        return False
    
    if 0 <= move[0] <= 2 and 0 <= move[1] <= 2:
        if pole[move[0]][move[1]] == '~':
            pole[move[0]][move[1]] = 'X'
            print("Успешный ход!")
            print(f'-'*17)
            return True
        else:
            print('Место занято!')
            return False
    else:
        print("число введено неверно!")
        return False