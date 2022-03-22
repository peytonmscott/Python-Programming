def show_board(board_matrix):
    """
    This function displays the Tic Tac Toe Board
    :param board_matrix:
    :return:
    """
    print('\n  1   2   3')
    for index, row in enumerate(board_matrix):
        print(str(index + 1) + ('|'.join([' ' + symbol + ' ' for symbol in row])))
        if index < 2:
            print('  --+---+--')
    print('\n')


def initialize_board():
    """
    This Function Initialize the Matrix for Tic Tac Toe
    :return:
    """
    brd_matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return brd_matrix


def get_input(player_turn, board_matrix):
    """
    This function Get Input from user and validates that input
    :param player_turn:
    :param board_matrix:
    :return:
    """
    row_column = input('Enter {} move (row,column no spaces)> '.format(player_turn))
    row, column = row_column.split(',')
    row = int(row) - 1
    column = int(column) - 1

    if 0 <= row <= 2 and 0 <= column <= 2:
        if board_matrix[row][column] in ['X', 'O']:
            print('Invalid move, try again.')
            board_matrix = get_input(player_turn, board_matrix)

        elif board_matrix[row][column] == ' ':
            board_matrix[row][column] = player_turn
    else:
        print('Invalid move, try again.')
        board_matrix = get_input(player_turn, board_matrix)

    return board_matrix


def is_winner(player_turn, board_matrix):
    """
    This function analyzes the board and check for winner
    :param player_turn:
    :param board_matrix:
    :return:
    """

    # check rows for win
    for row in board_matrix:
        if len([item for item in row if item == player_turn]) == 3:
            print('{} is the winner!'.format(player_turn))
            return True

    # check columns for win
    if 3 in [len([row[0] for row in board_matrix if row[0] == player_turn]),  # column 1
             len([row[1] for row in board_matrix if row[1] == player_turn]),  # column 2
             len([row[2] for row in board_matrix if row[2] == player_turn])]:  # column 3
        print('{} is the winner!'.format(player_turn))
        return True

    # check diagonals
    if 3 in [len([row[index] for index, row in enumerate(board_matrix) if row[index] == player_turn]),  # first diagonal
             len([row[2 - index] for index, row in enumerate(board_matrix) if
                  row[2 - index] == player_turn])]:  # second diagonal
        print('{} is the winner!'.format(player_turn))
        return True

    return False


def play():
    """
    This is the Main Function of this Game
    :return:
    """
    player_turn = 'X'
    board_matrix = initialize_board()
    show_board(board_matrix)
    while True:
        board_matrix = get_input(player_turn, board_matrix)
        show_board(board_matrix)
        if is_winner(player_turn, board_matrix):
            break
        player_turn = 'X' if player_turn == 'O' else 'O'


# Start the Game
play()
