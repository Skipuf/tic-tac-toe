
def update_pole(pole: str) -> None:
    print(f'| - | 0 | 1 | 2 |')
    print(f'-'*17)
    for num, item in enumerate(pole):
        print(f'| {num} | {" | ".join(item)} |')
        print(f'-'*17)

def player_move(move: str, pole: list) -> bool:
    try:
        move = [int(move[0]), int(move[1])]
    except ValueError:
        print("число введено неверно!")
        return False
    
    if 0 <= move[0] <= 2 and 0 <= move[1] <= 2:
        if pole[move[1]][move[0]] == '~':
            pole[move[1]][move[0]] = 'X'
            print("Успешный ход!")
            return True
        else:
            print('Место занято!')
            return False
    else:
        print("число введено неверно!")
        return False
    
def robot_move(pole: list) -> None:
    for num, item in enumerate(pole):
        

def game() -> None:
    print('-'*15)
    print('Чтобы сделать ход, введи двухзначное число.')
    print('Первая цифра числа - номер столбца.')
    print('Вторая цифра числа - номер строки.')
    print('Например: 12')
    print(f'-'*17)
    end = False
    pl = [
        ['~','~','~'],
        ['~','~','~'],
        ['~','~','~']
    ]
    while not end:
        update_pole(pl)
        while not player_move(input('Твой ход: '), pl):
            print(f'-'*17)


def rules() -> None:
    print('-'*17)
    print('Правила игры:')
    print('1. Игровое поле состоит из сетки размером 3х3.')
    print('2. Соревнуются два игрока, один из которых играет за "X", а другой за "O".')
    print('3. Главная цель: выстроить три одинаковых символа подряд — вертикально, горизонтально или по диагонали.')
    print('4. Ход игры: игроки размещают свои символы на свободные ячейки.')
    print('5. Последовательность ходов: участники игры ходят поочередно, пропуск хода кем-либо недопустим.')
    print('6. Ничья: если все ячейки заняты, и никто не собрал линию из трёх символов, игра считается ничейной.')


print('Добро пожаловать!')
run_menu = True
while run_menu:
    print('-'*17)
    print('Меню: \n1 - Начать игру. \n2 - Правила игры. \n3 - Выйти.')
    print('-'*17)
    run = input('Твой выбор: ').lower()
    if run == '1': game()
    elif run == '2': rules()
    elif run == '3': run_menu = False
    else: print("Некорректный ввод!")