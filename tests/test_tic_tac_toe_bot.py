#!/usr/bin/env python

"""Tests for `tic_tac_toe_bot` package."""

import pytest

from modules import tic_tac_toe_bot


class TestClass:
    def test_return_value(self):
        """Simple pytest test function to test pytest on the default main function"""
        assert tic_tac_toe_bot.main("test") == "test"

