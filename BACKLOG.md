Narative:

Domain:
- game board
  - 2-dim list of 3x3
  - allowed values: X, O or _ (blank)
  - 9 positions: 0->8 (or [0-2][0-2])

- player X
- player O
- empty field = _

- player X starts

Rules:
- random move with 2s interval
  - Name of player that moves is shown
  - Show state of board

      ⚠️ random moves, so BOTs should not be smart and block:
      - 2 in a row of same player should block
      - 2 in a column of same player should block
      - 2 in a diagonal of same player should block

- 3 in a column of same player wins, eg X:
  - Output: Board
  - Output: "Player X WON!"
- 3 in row of same player wins, eg O:
  - Output: Board
  - Output: "PLAYER O WON!"
- 3 in a diagonal of same player wins, eg X:
  - Output: Board
  - Output: "PLAYER X WON!"
- all moves are done without 3 subsequent is a draw
  - Output: Board
  - Output: "THE GAME ENDS WITH A DRAW!"

---

US1: Display Game board
UAT:
- empty: list with empty strings
- vertical line, horizontal line, diagonal line, draw game
ATDD:

    IN = ["","","",
          "","","",
          "","",""]
    OUT =
            | |
           -+-+-
            | |

US2: X won a vertical line
UAT: X wins when every 3th element contains an X
ATDD:

    IN = [X,_,_,
          X,O,_,
          X,_,O]

    OUT =
          X| |
          -+-+-
          X|O|
          -+-+-
          X| |O

US3: O won a horizontal line
UAT: O wins when each block of 3 contains all O
ATDD:

    IN = [X,_,X,
          O,O,O,
          X,_,_]

    OUT =
          X| |X
          -+-+-
          O|O|O
          -+-+-
          X| |

US4: X won a diagonal line
UAT: X wins when indexes 0,4,8 or 2,4,6 are filled with O
ATDD:

    IN = [X,_,X,
          O,O,O,
          X,_,_]

    OUT =
          X| |X
          -+-+-
          O|O|O
          -+-+-
          X| |

US5: Draw game
UAT:
- No one wins with 3 in a line
- Board is full (no blanks in the grid left)
ATDD:

    IN = [X,O,X,
          O,O,X
          X,X,O]

    OUT =
         X|O|X
         -+-+-
         O|O|X
         -+-+-
         X|X|O

US6: Next move
UAT:
- takes current board and the player that will move
- returns new board with random move

US7: Switch a player
UAT:
- takes the current player and determines the next one
ATDD1:
  IN = "X"
  OUT = "O"
ATDD2:
  IN = "O"
  OUT = "X"

US7: Show end game result
UAT:
- check if board is full
- show the result: winner
ATTD1:
  IN = "X"
  OUT = "PLAYER X WON!"
ATTD2:
  IN = "O"
  OUT = "PLAYER O WON!"
ATDD3:
  IN = ""
  OUT = "THE GAME ENDS WITH A DRAW!"

US8: Determine if game is over
UAT:
- take the current board
- return bool whether game is over
- return the winner (O, X) or empty string "" when there is no winner yet
ATTD:
    IN = [X,_,X,
          O,O,O,
          X,_,_]

    OUT = (True, "O")
