import pytest
from unittest.mock import patch

from modules import tic_tac_toe_bot
from tests.doubles import boards as doubles

X = "X"
O = "O"
_ = " "


class TestGuardiansBoardSize:
    """Board should have valid dimensions"""
    def test_board_has_invalid_row(self):
        assert tic_tac_toe_bot.validate_board_size(doubles.board_not_2d) is False

    def test_string_is_invalid(self):
        assert tic_tac_toe_bot.validate_board_size("") is False

    def test_empty_list_is_invalid(self):
        assert tic_tac_toe_bot.validate_board_size([]) is False

    def test_board_size_3x4_is_invalid(self):
        assert tic_tac_toe_bot.validate_board_size(doubles.board_3x4) is False

    def test_board_size_4x3_is_invalid(self):
        assert tic_tac_toe_bot.validate_board_size(doubles.board_4x3) is False

    def test_board_size_2x2_is_invalid(self):
        assert tic_tac_toe_bot.validate_board_size(doubles.board_2x2) is False

    def test_empty_board_3x3_is_valid(self):
        assert tic_tac_toe_bot.validate_board_size(doubles.empty_board_in) is True


class TestGuardiansBoardContent:
    """Board should only contain expected content"""
    def test_board_content_is_valid(self):
        """squares should have X, O or be empty"""
        assert tic_tac_toe_bot.validate_board_content(doubles.board_valid_content) is True

    def test_board_content_is_invalid(self):
        """squares should not contain anything else"""
        assert tic_tac_toe_bot.validate_board_content(doubles.board_invalid_content) is False


class TestInitGame:
    """Set the right conditions for a new game"""

    def test_game_not_over_no_winner_player_x_starts(self):
        """- player X starts
        - there is no winner ("")
        - game is not over
        """
        assert tic_tac_toe_bot.init_game() == (False, "", X)


class TestShowInitGame:
    """Starting the game should render empty board output"""
    def test_show_init_board(self):
        """should output board creation phase and show empty board in ascii table"""
        assert tic_tac_toe_bot.show_init_board(doubles.empty_board_in) == doubles.init_board_out


class TestShowBoard:
    """Should render a proper ascii board with moves of both players"""
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

    def test_no_player_has_a_vertical_line(self):
        assert tic_tac_toe_bot.is_vertical_line(doubles.draw_board_in) == (False, "")


class TestHorizontal:
    """Should return if a horizontal line has been made and by who"""
    def test_o_has_horizontal_line(self):
        assert tic_tac_toe_bot.is_horizontal_line(doubles.o_won_board_horizontal_in) == (True, O)

    def test_x_has_horizontal_line(self):
        assert tic_tac_toe_bot.is_horizontal_line(doubles.x_won_board_horizontal_in) == (True, X)

    def test_no_player_has_a_horizontal_line(self):
        assert tic_tac_toe_bot.is_horizontal_line(doubles.draw_board_in) == (False, "")


class TestDiagonal:
    """Should return if a diagonal line has been made and by who"""
    def test_x_has_diagonal_line(self):
        assert tic_tac_toe_bot.is_diagonal_line(doubles.x_won_board_diagonal_in) == (True, X)

    def test_o_has_diagonal_line(self):
        assert tic_tac_toe_bot.is_diagonal_line(doubles.o_won_board_diagonal_in) == (True, O)

    def test_no_player_has_a_diagonal_line(self):
        assert tic_tac_toe_bot.is_diagonal_line(doubles.draw_board_in) == (False, "")


class TestGetFreeSquare:
    """Should return a random index from a list of free squares for the next move"""
    def test_get_random_free_square_for_empty_board_between_0_and_8_included(self):
        rnd_idx = tic_tac_toe_bot.get_random_idx(9)
        assert 0 <= rnd_idx < 9

    @patch('random.randrange')
    def test_get_random_free_square_for_empty_board_is_5(self, mock_randrange):
        mock_randrange.return_value = 5
        rnd_idx = tic_tac_toe_bot.get_random_idx(9)
        assert rnd_idx == 5


class TestSwitchPlayer:
    """Should switch the player"""
    def test_return_player_o_after_player_x_turn(self):
        assert tic_tac_toe_bot.switch_player(X) == O

    def test_return_player_x_after_player_o_turn(self):
        assert tic_tac_toe_bot.switch_player(O) == X


class TestBoardFull:
    """Should report if all squares are filled"""
    def test_board_is_empty_returns_false(self):
        assert tic_tac_toe_bot.is_board_full(doubles.empty_board_in) is False

    def test_board_has_some_empty_squares_returns_false(self):
        assert tic_tac_toe_bot.is_board_full(doubles.o_won_board_diagonal_in) is False

    def test_board_is_full_returns_true(self):
        assert tic_tac_toe_bot.is_board_full(doubles.draw_board_in) is True


class TestShowEndGameResult:
    """Should show message who won the game"""

    def test_x_wins(self):
        """X wins: PLAYER X WON!"""
        assert tic_tac_toe_bot.show_end_game_result(X) == "PLAYER X WON!"

    def test_o_wins(self):
        """O wins: PLAYER O WON!"""
        assert tic_tac_toe_bot.show_end_game_result(O) == "PLAYER O WON!"

    def test_draw_game(self):
        """Draw game: THE GAME ENDS WITH A DRAW!"""
        assert tic_tac_toe_bot.show_end_game_result("") == "THE GAME ENDS WITH A DRAW!"

