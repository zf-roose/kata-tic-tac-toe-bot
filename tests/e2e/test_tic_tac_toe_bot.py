import pytest

from modules import tic_tac_toe_bot
from tests.doubles import boards as doubles

X = "X"
O = "O"
_ = " "


class TestEndToEnd:

    def test_end_to_end(self):
        """Sequentially filling the board: X starts and wins at step 7 with diagonal line on [2][0], [1][1], [0][2]"""
        assert tic_tac_toe_bot.main(testing=True) == doubles.non_random_moves_game_out
