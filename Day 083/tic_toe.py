def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")


def check_win(board, player):
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][
            2] == player) \
                or (
                board[0][i] == player and board[1][i] == player and board[2][
            i] == player) \
                or (
                board[0][0] == player and board[1][1] == player and board[2][
            2] == player) \
                or (
                board[0][2] == player and board[1][1] == player and board[2][
            0] == player):
            return True
    return False


def play_game():
    board = [[' ', ' ', ' '] for _ in range(3)]
    player = 'X'
    winner = False
    print("Player 1 is X and Player 2 is 0")
    while not winner:
        print_board(board)
        row = int(input(f"{player} Enter row: "))
        col = int(input(f"{player} Enter column: "))
        if board[row][col] != ' ':
            print("Invalid move, try again!")
            continue
        if player == 'X':
            board[row][col] = 'X'
        else:
            board[row][col] = '0'
        if check_win(board, player):
            print_board(board)
            print("Player", player, "wins!")
            winner = True
        player = '0' if player == 'X' else 'X'


play_game()
