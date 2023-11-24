import pytest
from unittest.mock import patch

from modules import tic_tac_toe_bot
from tests.doubles import boards as doubles

X = "X"
O = "O"
_ = " "


class TestPlayGameTicTacToe:
    """Should play a game, showing the progress and report the winner if any"""

    def test_player_x_won_vertical_line(self):
        """Player X won with a vertical line"""
        board_move_1 = [
            [X, _, _],
            [_, _, _],
            [_, _, _]
        ]
        board_move_2 = [
            [X, _, _],
            [_, O, _],
            [_, _, _]
        ]
        board_move_3 = [
            [X, _, _],
            [X, O, _],
            [_, _, _]
        ]
        board_move_4 = [
            [X, _, _],
            [X, O, _],
            [_, _, O]
        ]
        board_move_5 = [
            [X, _, _],
            [X, O, _],
            [X, _, O]
        ]

        with patch("modules.tic_tac_toe_bot.get_next_move") as mocked_get_next_move:
            mocked_get_next_move.side_effect = [
                board_move_1,
                board_move_2,
                board_move_3,
                board_move_4,
                board_move_5
            ]
            assert tic_tac_toe_bot.main(sleep=0) == doubles.player_x_won_vertical_line_out

    def test_player_o_won_horizontal_line(self):
        """Player O won with a horizontal line"""
        board_move_1 = [
            [X, _, _],
            [_, _, _],
            [_, _, _]
        ]
        board_move_2 = [
            [X, _, _],
            [O, _, _],
            [_, _, _]
        ]
        board_move_3 = [
            [X, _, _],
            [O, _, _],
            [X, _, _]
        ]
        board_move_4 = [
            [X, _, _],
            [O, O, _],
            [X, _, _]
        ]
        board_move_5 = [
            [X, _, X],
            [O, O, _],
            [X, _, _]
        ]
        board_move_6 = [
            [X, _, X],
            [O, O, O],
            [X, _, _]
        ]

        with patch("modules.tic_tac_toe_bot.get_next_move") as mocked_get_next_move:
            mocked_get_next_move.side_effect = [
                board_move_1,
                board_move_2,
                board_move_3,
                board_move_4,
                board_move_5,
                board_move_6
            ]
            assert tic_tac_toe_bot.main(sleep=0) == doubles.player_o_won_vertical_line_out

    def test_player_x_won_diagonal_line(self):
        """Player X won with a diagonal line"""
        board_move_1 = [
            [X, _, _],
            [_, _, _],
            [_, _, _]
        ]
        board_move_2 = [
            [X, _, _],
            [O, _, _],
            [_, _, _]
        ]
        board_move_3 = [
            [X, _, _],
            [O, X, _],
            [_, _, _]
        ]
        board_move_4 = [
            [X, _, _],
            [O, X, _],
            [O, _, _]
        ]
        board_move_5 = [
            [X, _, _],
            [O, X, _],
            [O, _, X]
        ]

        with patch("modules.tic_tac_toe_bot.get_next_move") as mocked_get_next_move:
            mocked_get_next_move.side_effect = [
                board_move_1,
                board_move_2,
                board_move_3,
                board_move_4,
                board_move_5
            ]
            assert tic_tac_toe_bot.main(sleep=0) == doubles.player_x_won_diagonal_line_out

    def test_game_ends_with_a_draw(self):
        """The game ends with a draw"""
        board_move_1 = [
            [X, _, _],
            [_, _, _],
            [_, _, _]
        ]
        board_move_2 = [
            [X, _, _],
            [O, _, _],
            [_, _, _]
        ]
        board_move_3 = [
            [X, _, _],
            [O, _, X],
            [_, _, _]
        ]
        board_move_4 = [
            [X, O, _],
            [O, _, X],
            [_, _, _]
        ]
        board_move_5 = [
            [X, O, _],
            [O, _, X],
            [_, X, _]
        ]
        board_move_6 = [
            [X, O, _],
            [O, _, X],
            [_, X, O]
        ]
        board_move_7 = [
            [X, O, _],
            [O, _, X],
            [X, X, O]
        ]
        board_move_8 = [
            [X, O, _],
            [O, O, X],
            [X, X, O]
        ]
        board_move_9 = [
            [X, O, X],
            [O, O, X],
            [X, X, O]
        ]

        with patch("modules.tic_tac_toe_bot.get_next_move") as mocked_get_next_move:
            mocked_get_next_move.side_effect = [
                board_move_1,
                board_move_2,
                board_move_3,
                board_move_4,
                board_move_5,
                board_move_6,
                board_move_7,
                board_move_8,
                board_move_9
            ]
            assert tic_tac_toe_bot.main(sleep=0) == doubles.game_ends_with_draw_out

    def test_cannot_start_game_without_valid_board(self):
        """Board init failure reports error"""
        assert tic_tac_toe_bot.main(board=doubles.board_3x4, sleep=0) == "Unexpected error: invalid board"
