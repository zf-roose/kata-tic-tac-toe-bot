import pytest

from modules import tic_tac_toe_bot
from tests.doubles import boards as doubles

X = "X"
O = "O"
_ = " "


# class TestRound:
#     def test_one_round_not_game_over(self):
#         finished, winner = tic_tac_toe_bot.play_round(doubles.unfinished_game_in, X)
#         assert finished is False
#         assert winner == ""

class TestGameOver:
    def test_game_over_x_vertical(self):
        """game over: x won vertical line"""
        finished, winner = tic_tac_toe_bot.is_game_over(doubles.x_won_board_vertical_in)
        assert finished is True
        assert winner == X

    def test_game_over_o_horizontal(self):
        """game over: o won horizontal line"""
        finished, winner = tic_tac_toe_bot.is_game_over(doubles.o_won_board_horizontal_in)
        assert finished is True
        assert winner == O

    def test_game_over_x_diagonal(self):
        """game over: x won diagonal"""
        finished, winner = tic_tac_toe_bot.is_game_over(doubles.x_won_board_diagonal_in)
        assert finished is True
        assert winner == X

    def test_game_over_draw(self):
        """game over: draw game"""
        finished, winner = tic_tac_toe_bot.is_game_over(doubles.draw_board_in)
        assert finished is True
        assert winner == ""

    def test_game_not_over(self):
        """game not over: empty board"""
        finished, winner = tic_tac_toe_bot.is_game_over(doubles.empty_board_in)
        assert finished is False
        assert winner == ""
