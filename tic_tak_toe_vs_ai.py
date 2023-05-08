import time

crosses = 'X'
zeros = 'O'
EMPTY = ' '
TIE = 'Ничья'
NUM_SQUARES = 9


def display_instruct():
    """
    Выводит на экран инструкцию для игрока
    """
    print("""
    Добро пожаловать в игру 'Крестики нолики'! Попробуй сыграть против компьютера и победить...
    Чтобы сделать ход, введи число от 0 до 8. Числа соответствуют полям доски - так, как показано ниже:
    
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    
    Удачи мой друг!!\n""")


def ask_yes_no(question):
    """
    Задает вопрос с ответом 'да' или 'нет'
    """
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """
    Просит ввести число из диапазона
    """
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """
    Определяет кто будет ходить первым.
    """
    go_first = ask_yes_no('Хочешь оставить первый ход за собой? (y/n): ')
    if go_first == 'y':
        print('Выбор сделан, ты играешь крестиками и ходишь первым!')
        human = crosses
        computer = zeros
    else:
        print('Выбор сделан, ты играешь ноликами и первый ход за мной!')
        human = zeros
        computer = crosses

    return computer, human


def new_board():
    """
    Создает новую игровую доску
    """
    board = []
    for _ in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """
    Отображает игровую доску на экране
    """
    print(f"""
        {board[0]} | {board[1]} | {board[2]}
       -----------
        {board[3]} | {board[4]} | {board[5]}
       -----------
        {board[6]} | {board[7]} | {board[8]}
        """)


def legal_moves(board):
    """
    Создает список доступных ходов.
    """
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """
    Определяет победителя в игре
    """
    ways_to_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),
                   (0, 4, 8), (2, 4, 6),
                   )

    for row in ways_to_win:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            return board[row[0]]

        if EMPTY not in board:
            return TIE

    return None


def computer_move(board, computer, human):
    """
    Делает ход за компьютерного противника
    """
    time.sleep(2)
    # создаем копию доски так как функцию будет ее менять
    board = board[:]

    # поля от лучшего к худшему
    best_movies = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выбираю поле номер", end=" ")

    for move in legal_moves(board):
        board[move] = computer

        # если следующим ходом может победить компьютер, выбираем этот ход
        if winner(board) == computer:
            print(move)
            return move

        # Выполнив проверку отменим изменения
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human

        # если следующим ходом может победить человек, блокируем этот ход
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    # поскольку ни одна из сторон не может выиграть на следующем ходу
    # выбираем лучший ход из доступных
    for move in best_movies:
        if move in legal_moves(board):
            print(move)
            return move


def human_move(board):
    """
    Получает ход человека
    """
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0-8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nСмешной человек...Это поле уже занято, выбери другое.\n")
            print("Ладненько...")
    return move


def next_turn(turn):
    """
    Осуществляет переход хода. (чередует)
    """
    if turn == crosses:
        return zeros
    else:
        return crosses


def congrat_winner(the_winner, computer, human):
    """
    Поздравляет победителя игры.
    """
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")

    if the_winner == computer:
        print("Как я и предсказывал, ты просто мешок с костями, а я победил ха-ха-ха(смеется по роботски)!!!")
    elif the_winner == human:
        print("А ты уверен что ты человек? Ты только что победил мощнейший компьютер...Поздравляю!!!")
    elif the_winner == TIE:
        print("Тебе повезло человечишка и ты смог вывести игру в ничью...")


def main():
    display_instruct()
    computer, human = pieces()
    turn = crosses
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer

        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


if __name__ == '__main__':
    main()
    input("\nНажмите Enter что бы выйти.")
