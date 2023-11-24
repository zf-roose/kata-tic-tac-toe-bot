import copy

import pytest
from unittest.mock import patch

from modules import tic_tac_toe_bot
from tests.doubles import boards as doubles

X = "X"
O = "O"
_ = " "


class TestGuardians:
    def test_empty_3x3_board_is_valid(self):
        assert tic_tac_toe_bot.validate(doubles.empty_board_in) is True

    def test_empty_3x4_board_is_invalid(self):
        assert tic_tac_toe_bot.validate(doubles.board_3x4) is False

    def test_3x3_board_and_wrong_content_is_invalid(self):
        assert tic_tac_toe_bot.validate(doubles.board_invalid_content) is False

    def test_board_2x2_and_wrong_content_is_invalid(self):
        assert tic_tac_toe_bot.validate(doubles.board_2x2) is False


class TestGetNextMove:
    """Should return board with next random move"""
    def test_next_random_x_move_on_empty_board_should_not_be_empty(self, monkeypatch):
        """should return non-empty board with next random move starting from empty board"""
        empty_board_in = copy.deepcopy(doubles.empty_board_in)
        assert tic_tac_toe_bot.get_next_move(empty_board_in, X, sleep=0) != doubles.empty_board_in

    def test_next_random_o_move_on_full_board_should_remain_same_board(self):
        """should return same full board after trying a random move on a full board"""
        draw_board_in = copy.deepcopy(doubles.draw_board_in)
        assert tic_tac_toe_bot.get_next_move(draw_board_in, O, sleep=0) == doubles.draw_board_in

    @patch('modules.tic_tac_toe_bot.get_random_idx')
    def test_next_random_x_move_on_empty_board_is_the_middle_square(self, mock_get_random_idx):
        """should return only x in the middle of the board after X starts in the center"""
        empty_board_in = copy.deepcopy(doubles.empty_board_in)
        mock_get_random_idx.return_value = 4
        assert tic_tac_toe_bot.get_next_move(empty_board_in, X, sleep=0) == doubles.x_in_center_in


class TestGameOver:
    """Should report game is over if draw game or there is a winner"""
    def test_game_over_x_vertical(self):
        """X won vertical line"""
        finished, winner = tic_tac_toe_bot.is_game_over(doubles.x_won_board_vertical_in)
        assert finished is True
        assert winner == X

    def test_game_over_o_horizontal(self):
        """O won horizontal line"""
        finished, winner = tic_tac_toe_bot.is_game_over(doubles.o_won_board_horizontal_in)
        assert finished is True
        assert winner == O

    def test_game_over_x_diagonal(self):
        """X won diagonal line"""
        finished, winner = tic_tac_toe_bot.is_game_over(doubles.x_won_board_diagonal_in)
        assert finished is True
        assert winner == X

    def test_game_over_draw(self):
        """Draw game, no winner"""
        finished, winner = tic_tac_toe_bot.is_game_over(doubles.draw_board_in)
        assert finished is True
        assert winner == ""

    def test_game_not_over(self):
        """Empty board, game is not over"""
        finished, winner = tic_tac_toe_bot.is_game_over(doubles.empty_board_in)
        assert finished is False
        assert winner == ""
