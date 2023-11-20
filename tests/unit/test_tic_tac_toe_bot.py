import pytest

from modules import tic_tac_toe_bot
from tests.doubles import boards as doubles

X = "X"
O = "O"
_ = " "


@pytest.mark.skip
class TestGuardian:
    def test_return_value(self):
        """Simple pytest test function to test pytest on the default main function"""
        assert tic_tac_toe_bot.main("test") == "test"


class TestShowInitBoard:
    def test_show_init_board(self):
        assert tic_tac_toe_bot.show_init_board(doubles.empty_board_in) == doubles.init_board_out


class TestShowBoard:
    """Should display a proper board with expected layout"""
    def test_1_empty_game_board(self):
        assert tic_tac_toe_bot.show_board(doubles.empty_board_in) == doubles.empty_board_out

    def test_2_x_won_vertical_line(self):
        assert tic_tac_toe_bot.show_board(doubles.x_won_board_vertical_in) == doubles.x_won_board_vertical_out

    def test_3_o_won_horizontal_line(self):
        assert tic_tac_toe_bot.show_board(doubles.o_won_board_horizontal_in) == doubles.o_won_board_horizontal_out

    def test_4_x_won_diagonal_line(self):
        assert tic_tac_toe_bot.show_board(doubles.x_won_board_diagonal_in) == doubles.x_won_board_diagonal_out

    def test_5_draw_game_board(self):
        assert tic_tac_toe_bot.show_board(doubles.draw_board_in) == doubles.draw_board_out


class TestVertical:
    """Should return if a vertical line has been made and by who"""
    def test_x_has_vertical_line(self):
        assert tic_tac_toe_bot.is_vertical_line(doubles.x_won_board_vertical_in) == (True, X)

    def test_o_has_vertical_line(self):
        assert tic_tac_toe_bot.is_vertical_line(doubles.o_won_board_vertical_in) == (True, O)

    def test_no_player_has_no_vertical_line(self):
        assert tic_tac_toe_bot.is_vertical_line(doubles.draw_board_in) == (False, "")


class TestHorizontal:
    """Should return if a horizontal line has been made and by who"""
    def test_o_has_horizontal_line(self):
        assert tic_tac_toe_bot.is_horizontal_line(doubles.o_won_board_horizontal_in) == (True, O)

    def test_x_has_horizontal_line(self):
        assert tic_tac_toe_bot.is_horizontal_line(doubles.x_won_board_horizontal_in) == (True, X)

    def test_no_player_has_no_horizontal_line(self):
        assert tic_tac_toe_bot.is_horizontal_line(doubles.draw_board_in) == (False, "")


class TestDiagonal:
    """Should return if a diagonal line has been made and by who"""
    def test_x_has_diagonal_line(self):
        assert tic_tac_toe_bot.is_diagonal_line(doubles.x_won_board_diagonal_in) == (True, X)

    def test_o_has_diagonal_line(self):
        assert tic_tac_toe_bot.is_diagonal_line(doubles.o_won_board_diagonal_in) == (True, O)

    def test_no_player_has_no_diagonal_line(self):
        assert tic_tac_toe_bot.is_diagonal_line(doubles.draw_board_in) == (False, "")


class TestGetNextMove:
    """Should return next random move"""
    def test_next_random_move_on_empty_board_should_not_be_empty(self):
        """should return non-empty board with the next random move"""
        empty_board_in = [[_, _, _],
                          [_, _, _],
                          [_, _, _]]
        assert tic_tac_toe_bot.get_next_random_move(doubles.empty_board_in, X) != empty_board_in

    def test_next_random_move_on_full_board_should_remain_same_board(self):
        """should return same full board after random move on full board"""
        draw_board_in = [[X, O, X],
                         [O, O, X],
                         [X, X, O]]
        assert tic_tac_toe_bot.get_next_random_move(doubles.draw_board_in, O) == draw_board_in


class TestSwitchPlayer:
    """Should switch the player"""
    def test_return_next_player_o_after_player_x_turn(self):
        assert tic_tac_toe_bot.switch_player(X) == O

    def test_return_next_player_x_after_player_o_turn(self):
        assert tic_tac_toe_bot.switch_player(O) == X


class TestBoardFull:
    """Should report if all squares are filled"""
    def test_board_is_empty(self):
        assert tic_tac_toe_bot.is_board_full(doubles.empty_board_in) is False

    def test_board_has_some_empty_squares(self):
        assert tic_tac_toe_bot.is_board_full(doubles.o_won_board_diagonal_in) is False

    def test_board_is_full(self):
        assert tic_tac_toe_bot.is_board_full(doubles.draw_board_in) is True


class TestShowEndGameResult:
    """Show message who won the game"""

    def test_x_wins(self):
        """X wins: PLAYER X WON!"""
        assert tic_tac_toe_bot.show_end_game_result(X) == "PLAYER X WON!"

    def test_o_wins(self):
        """O wins: PLAYER O WON!"""
        assert tic_tac_toe_bot.show_end_game_result(O) == "PLAYER O WON!"

    def test_draw_game(self):
        """Draw game: THE GAME ENDS WITH A DRAW!"""
        assert tic_tac_toe_bot.show_end_game_result("") == "THE GAME ENDS WITH A DRAW!"

