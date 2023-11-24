import copy
import random
import time

X = "X"
O = "O"
_ = " "


def main(board=None, sleep=2):
    if not board:
        board = [[_, _, _],
                 [_, _, _],
                 [_, _, _]]

    if validate(board) is False:
        print("Unexpected error: invalid board")
        return "Unexpected error: invalid board"
    output = show_init_board(board)

    game_over, winner, player = init_game()

    while not game_over:
        board = get_next_move(board, player, sleep=sleep)
        output += show_board(board)

        game_over, winner = is_game_over(board)

        if not game_over:
            player = switch_player(player)
            output += f"\nPlayer {player}:\n"

    output += "\n" + show_end_game_result(winner)
    return output


def init_game():
    return False, "", X


def validate(board) -> bool:
    return validate_board_size(board) and validate_board_content(board)


def validate_board_size(board) -> bool:
    if type(board) != list:
        return False
    if len(board) != 3:
        return False
    for row in board:
        if type(row) != list:
            return False
        if len(row) != 3:
            return False
    return True


def validate_board_content(board) -> bool:
    for row in board:
        for square in row:
            if square not in [X, O, _]:
                return False
    return True


def show_init_board(board):
    output = ""
    output += "Game Board Creation..."
    output += show_board(board)
    output += "Board Created.\n"
    output += "The game will start with player X\n"
    print(output)
    return output


def show_board(board) -> str:
    board_out = copy.deepcopy(board)
    # IDE formatting removes trailing spaces from the doubles
    # at the end of the line so deal with this + conform kata output examples
    board_out[0][2] = "" if board_out[0][2] == " " else board_out[0][2]
    board_out[1][2] = "" if board_out[1][2] == " " else board_out[1][2]
    board_out[2][2] = "" if board_out[2][2] == " " else board_out[2][2]
    output = f"""
{board_out[0][0]}|{board_out[0][1]}|{board_out[0][2]}
-+-+-
{board_out[1][0]}|{board_out[1][1]}|{board_out[1][2]}
-+-+-
{board_out[2][0]}|{board_out[2][1]}|{board_out[2][2]}
"""
    print(output)
    return output


def is_vertical_line(board) -> (bool, str):
    for col_idx in range(2):
        if board[0][col_idx] == _:
            return False, ""
        if board[0][col_idx] == board[1][col_idx] == board[2][col_idx]:
            return True, board[0][col_idx]
    return False, ""


def is_horizontal_line(board) -> (bool, str):
    for row in board:
        if row[0] == _:
            return False, ""
        if row[0] == row[1] == row[2]:
            return True, row[0]
    return False, ""


def is_diagonal_line(board) -> (bool, str):
    if board[1][1] == _:
        return False, ""
    if board[0][0] == board[1][1] == board[2][2]:
        return True, board[0][0]
    if board[2][0] == board[1][1] == board[0][2]:
        return True, board[2][0]
    return False, ""


def get_next_move(board, player, sleep=2):
    free_squares = []
    for row_idx, row in enumerate(board):
        for col_idx, square in enumerate(row):
            if square == _:
                position = (row_idx, col_idx)
                free_squares.append(position)

    if free_squares:
        free_idx = get_random_idx(len(free_squares))
        rnd_row_idx, rnd_col_idx = free_squares[free_idx]
        board[rnd_row_idx][rnd_col_idx] = player

    time.sleep(sleep)
    return board


def get_random_idx(idx_range) -> int:
    return random.randrange(idx_range)


def switch_player(player) -> str:
    next_player = O if player == X else X
    print(f"Next player: {next_player}")
    return next_player


def is_board_full(board) -> bool:
    for row in board:
        if _ in row:
            return False
    return True


def is_game_over(board) -> (bool, str):
    finished, winner = is_vertical_line(board)
    if finished:
        return True, winner

    finished, winner = is_horizontal_line(board)
    if finished:
        return True, winner

    finished, winner = is_diagonal_line(board)
    if finished:
        return True, winner

    if is_board_full(board):
        return True, ""

    return False, ""


def show_end_game_result(winner) -> str:
    if winner != "":
        print(f"PLAYER {winner} WON!")
        return f"PLAYER {winner} WON!"
    print("THE GAME ENDS WITH A DRAW!")
    return "THE GAME ENDS WITH A DRAW!"


if __name__ == "__main__":
    out = main()

