X = "X"
O = "O"
_ = " "
E = "E"

# INVALID BOARDS
board_not_2d = [
    [_, _, _],
    "Invalid row",
    [_, _, _]
]

board_3x4 = [
    [_, _, _, _],
    [_, _, _, _],
    [_, _, _, _]
]

board_4x3 = [
    [_, _, _],
    [_, _, _],
    [_, _, _],
    [_, _, _]
]

board_2x2 = [
    [_, _],
    [_, E]
]

board_valid_content = [
    [_, _, _],
    [_, X, _],
    [_, _, O]
]

board_invalid_content = [
    [_, _, _],
    [_, X, _],
    [E, _, O]
]

# EMPTY BOARD

empty_board_in = [
    [_, _, _],
    [_, _, _],
    [_, _, _]
]
empty_board_out = """
 | |
-+-+-
 | |
-+-+-
 | |
"""

init_board_out = """Game Board Creation...
 | |
-+-+-
 | |
-+-+-
 | |
Board Created.
The game will start with player X
"""

# VERTICAL WINS

x_won_board_vertical_in = [[X, _, _],
                           [X, O, _],
                           [X, _, O]]
x_won_board_vertical_out = """
X| |
-+-+-
X|O|
-+-+-
X| |O
"""

o_won_board_vertical_in = [[X, O, X],
                           [X, O, _],
                           [_, O, X]]
o_won_board_vertical_out = """
X|O|X
-+-+-
X|O|
-+-+-
 |O|X
"""

# HORIZONTAL WINS

o_won_board_horizontal_in = [[X, _, X],
                             [O, O, O],
                             [X, _, _]]
o_won_board_horizontal_out = """
X| |X
-+-+-
O|O|O
-+-+-
X| |
"""

x_won_board_horizontal_in = [[O, _, O],
                             [O, _, _],
                             [X, X, X]]
x_won_board_horizontal_out = """
O| |O
-+-+-
X|X|X
-+-+-
O| |
"""

# DIAGONAL WINS

x_won_board_diagonal_in = [[X, _, _],
                           [O, X, _],
                           [O, _, X]]
x_won_board_diagonal_out = """
X| |
-+-+-
O|X|
-+-+-
O| |X
"""

o_won_board_diagonal_in = [[X, _, O],
                           [X, O, _],
                           [O, _, X]]
o_won_board_diagonal_out = """
X| |O
-+-+-
X|O|
-+-+-
O| |X
"""

# DRAW GAME

draw_board_in = [[X, O, X],
                 [O, O, X],
                 [X, X, O]]
draw_board_out = """
X|O|X
-+-+-
O|O|X
-+-+-
X|X|O
"""

# UNFINISHED BOARD

unfinished_game_in = [[X, O, _],
                      [_, _, _],
                      [_, _, _]]
unfinished_game_out = """
X|O|
-+-+-
 | |
-+-+-
 | |
"""

x_in_center_in = [[_, _, _],
                  [_, X, _],
                  [_, _, _]]
x_in_center_out = """
 | |
-+-+-
 |X|
-+-+-
 | |
"""


# E2E SCENARIOS

sequential_moves_game_out = """Game Board Creation...
 | |
-+-+-
 | |
-+-+-
 | |
Board Created.
The game will start with player X

X| |
-+-+-
 | |
-+-+-
 | |

Player O:

X|O|
-+-+-
 | |
-+-+-
 | |

Player X:

X|O|X
-+-+-
 | |
-+-+-
 | |

Player O:

X|O|X
-+-+-
O| |
-+-+-
 | |

Player X:

X|O|X
-+-+-
O|X|
-+-+-
 | |

Player O:

X|O|X
-+-+-
O|X|O
-+-+-
 | |

Player X:

X|O|X
-+-+-
O|X|O
-+-+-
X| |

PLAYER X WON!"""

player_x_won_vertical_line_out = """Game Board Creation...
 | |
-+-+-
 | |
-+-+-
 | |
Board Created.
The game will start with player X

X| |
-+-+-
 | |
-+-+-
 | |

Player O:

X| |
-+-+-
 |O|
-+-+-
 | |

Player X:

X| |
-+-+-
X|O|
-+-+-
 | |

Player O:

X| |
-+-+-
X|O|
-+-+-
 | |O

Player X:

X| |
-+-+-
X|O|
-+-+-
X| |O

PLAYER X WON!"""

player_o_won_vertical_line_out = """Game Board Creation...
 | |
-+-+-
 | |
-+-+-
 | |
Board Created.
The game will start with player X

X| |
-+-+-
 | |
-+-+-
 | |

Player O:

X| |
-+-+-
O| |
-+-+-
 | |

Player X:

X| |
-+-+-
O| |
-+-+-
X| |

Player O:

X| |
-+-+-
O|O|
-+-+-
X| |

Player X:

X| |X
-+-+-
O|O|
-+-+-
X| |

Player O:

X| |X
-+-+-
O|O|O
-+-+-
X| |

PLAYER O WON!"""

player_x_won_diagonal_line_out = """Game Board Creation...
 | |
-+-+-
 | |
-+-+-
 | |
Board Created.
The game will start with player X

X| |
-+-+-
 | |
-+-+-
 | |

Player O:

X| |
-+-+-
O| |
-+-+-
 | |

Player X:

X| |
-+-+-
O|X|
-+-+-
 | |

Player O:

X| |
-+-+-
O|X|
-+-+-
O| |

Player X:

X| |
-+-+-
O|X|
-+-+-
O| |X

PLAYER X WON!"""

game_ends_with_draw_out = """Game Board Creation...
 | |
-+-+-
 | |
-+-+-
 | |
Board Created.
The game will start with player X

X| |
-+-+-
 | |
-+-+-
 | |

Player O:

X| |
-+-+-
O| |
-+-+-
 | |

Player X:

X| |
-+-+-
O| |X
-+-+-
 | |

Player O:

X|O|
-+-+-
O| |X
-+-+-
 | |

Player X:

X|O|
-+-+-
O| |X
-+-+-
 |X|

Player O:

X|O|
-+-+-
O| |X
-+-+-
 |X|O

Player X:

X|O|
-+-+-
O| |X
-+-+-
X|X|O

Player O:

X|O|
-+-+-
O|O|X
-+-+-
X|X|O

Player X:

X|O|X
-+-+-
O|O|X
-+-+-
X|X|O

THE GAME ENDS WITH A DRAW!"""

