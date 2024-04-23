from move import robot_move, player_move
from pole import update_pole

def game() -> None:
    print('-'*17)
    print('Чтобы сделать ход, введи двухзначное число.')
    print('Первая цифра числа - номер строки.')
    print('Вторая цифра числа - номер столбца.')
    print('Например: 12')
    print(f'-'*17)
    end = False
    pl = [
        ['~','~','~'],
        ['~','~','~'],
        ['~','~','~']
    ]
    while not end:
        end = update_pole(pl)
        if end: break
        while not player_move(input('Твой ход: '), pl):
            print(f'-'*17)
        end = update_pole(pl)
        if end: break
        print(f'Ход соперника: {robot_move(pl)}')
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