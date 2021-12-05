from random import randint

print('*****************************************\n'  # приветствуем игрока
      '      Приветвую тебя Авантюрист\n'
      ' *БАМ* в увелекательнейшей игре *БАМ*\n'
      '         КРЕСТИКИ -VS- НОЛИКИ\n'
      '*****************************************')

play = input('\nБудем играть с Мегамозгом или другом?\n'
             'Мегамозг - нажми "M", друг - нажми "D":').upper()
type_play = ''  # определяем играем с мегамозгом или другом
while True:
    if play == 'M':
        type_play = 'M'
        break
    if play == 'D':
        type_play = 'D'
        break
    else:
        play = input('Выбери Мегамозг - М, друг - D:').upper()

player = input('\nВыбирай за кого будешь побеждать Х или 0:').upper()  # выбрали за кого будем играть X или О
sign_player1 = ''
while True:
    if player == 'X':
        sign_player1 = 'X'
        break
    if player == '0':
        sign_player1 = '0'
        break
    else:
        print('Cегодня за них нельзя играть! Выбери что-то из списка:')
        player = input('Х или 0:').upper()

sign_player2 = '0' if sign_player1 == 'X' else 'X'

print('\nОтличный выбор! Последние 100 лет только они и побеждали!\n'
      'А теперь запоминай как обращаться к каждой клетке\n')  # показываем как делать ходы
print('1 | 2 | 3\n'
      '--|---|---\n'
      '4 | 5 | 6 \n'
      '--|---|---\n'
      '7 | 8 | 9\n')
print('Запомнил? Ну давай играть!')
field = [' '] * 9  # создаём поле


def beautiful_field(x):  # делаем вывод поля красиво
    global field
    field_out = field[0] + ' | ' + field[1] + ' | ' + field[2] + '\n' + \
                '--|---|---\n' + \
                field[3] + ' | ' + field[4] + ' | ' + field[5] + '\n' + \
                '--|---|---\n' + \
                field[6] + ' | ' + field[7] + ' | ' + field[8] + '\n'
    print(field_out)


def step_player1(x):  # функция на ходы первого игрока с проверками
    step = input('Авантюрист, твой ход: ')
    if not step.isdigit():
        print('Введите число')
        return step_player1(x)
    step = int(step)
    if step > 9 or step < 1:
        print('В таком диапазоне клеток мы не играем! Выбери от 1 до 9')
        return step_player1(x)
    elif field[step - 1] != ' ':
        print('Эта клетка занята')
        return step_player1(x)
    else:
        field[step - 1] = sign_player1
    return field


def step_player2(x):  # функция на ходы мегамозга или же второго игрока
    if type_play == 'M':
        step = randint(1, 9)
        if field[step - 1] == ' ':
            print('А теперь ход Мегамозга!')
            field[step - 1] = sign_player2
        else:
            return step_player2(x)
    else:
        step = input('Друг Авантюриста, твой ход: ')
        if not step.isdigit():
            print('Введите число')
            return step_player2(x)
        step = int(step)
        if step > 9 or step < 1:
            print('В таком диапазоне клеток мы не играем! Выбери от 1 до 9')
            return step_player2(x)
        elif field[step - 1] != ' ':
            print('Эта клетка занята')
            return step_player2(x)
        else:
            field[step - 1] = sign_player2
    return field


# выводы победы или поражения
winner_player_pc_out = '*****************************************\n' \
                       '                ПОБЕДА!!!\n' \
                       'Авантюрист на порядок сильнее Мегамозга!\n' \
                       '*****************************************'
winner_pc_player_out = '*****************************************\n' \
                       '      Похоже на ПОРАЖЕНИЕ!..\n' \
                       ' Минутная слабость.. Мегамозгу повезло..\n' \
                       '     Авантюрист, попытайся ещё раз!\n' \
                       '*****************************************'
winner_player1_2_out = '*****************************************\n' \
                       'Авантюрист на порядок сильнее друга!\n' \
                       '*****************************************'
winner_player2_1_out = '*****************************************\n' \
                       'Друг на порядок сильнее Авантюриста!\n' \
                       '*****************************************'


def winner_player1(x):  # функция на победу первого игрока
    i = sign_player1
    if (i == field[0] == field[1] == field[2]) or \
            (i == field[3] == field[4] == field[5]) or \
            (i == field[6] == field[7] == field[8]) or \
            (i == field[0] == field[3] == field[6]) or \
            (i == field[1] == field[4] == field[7]) or \
            (i == field[2] == field[5] == field[8]) or \
            (i == field[0] == field[4] == field[8]) or \
            (i == field[2] == field[4] == field[6]):
        if type_play == 'M':
            print(winner_player_pc_out), exit()
        else:
            print(winner_player1_2_out), exit()


def winner_player2(x):  # функция на победу второго игрока
    i = sign_player2
    if (i == field[0] == field[1] == field[2]) or \
            (i == field[3] == field[4] == field[5]) or \
            (i == field[6] == field[7] == field[8]) or \
            (i == field[0] == field[3] == field[6]) or \
            (i == field[1] == field[4] == field[7]) or \
            (i == field[2] == field[5] == field[8]) or \
            (i == field[0] == field[4] == field[8]) or \
            (i == field[2] == field[4] == field[6]):
        if type_play == 'M':
            print(winner_pc_player_out), exit()
        else:
            print(winner_player2_1_out), exit()


while True:  # сама игра в цикле
    if field.count(' ') > 0:
        @winner_player1
        @beautiful_field
        @step_player1
        def out():
            return
    if field.count(' ') > 0:
        @winner_player2
        @beautiful_field
        @step_player2
        def out():
            return
    else:
        if type_play == 'M':
            print('*****************************************\n'
                  '                НИЧЬЯ!\n'
                  '    Силы Авантюриста и Мегамозга равны\n'
                  '           Сыграй ещё раз :)\n'
                  '*****************************************')
        else:
            print('*****************************************\n'
                  '                НИЧЬЯ!\n'
                  '    Силы Авантюриста и друга равны\n'
                  '           Сыграй ещё раз :)\n'
                  '*****************************************')
        break