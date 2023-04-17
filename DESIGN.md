# Class Diagram
![Class Diagram](images/Chess_Class_Diagram.png)

# Object Diagram
![Object Diagram](images/Chess_Object_Diagram.png)

# Interface Diagram
![Interface Diagram](images/Chess_Interaction_Diagram.png)

# Interface Error Diagram
![Interface Error Diagram](images/Error_Interface_Diagram.png)

# Description
To start a chess game in the terminal enter: "python -m chess".
The board will be displayed and white is to move.
Once the player on the white side moves and the move is valid, it will be the player on the black side's turn to move.
After each move, the terminal will update the board based on the previously entered move. If a move is invalid, that player will be asked to enter a different move.
The game will end once there is a checkmate.

Each player has the ability to recall a move. After making a move, the player can enter "backup" to undo their previous move. This must be done prior to the opponent playing their next move. The backup functionality cannot be done consecutively. The player can only backup one move at a time. The undo only applies to that side's move.

# Moves
Moves shall be entered in sourcePositionDestinationPosition format.
Examples:
    "e2e4" - moving a piece at e2 two squares ahead to e4.
    "g7b7" - moving a piece along the same row from g7 to b7.
    "c1h6" - moving a piece diagonally from c1 to h6
    "b1c3" - moving the knight on b1 to c3
All movement rules of chess apply to this program.
A player will not be able to pass through any piece unless the moving piece is a knight. Since the knight moves in a 3x2 area, the only movement condition is that the destination location does not contain a piece of the same color as the knight.

#Tests
The test cases include all of the following which can be found in /tests:
    test_board
    test_castle
    test_checkmate
    test_errors
    test_move
    test_pieces
    test_undo
    test_view

test_board
    Tests when pieces are set that they exist in those places

test_castle
    Tests castling for both white and black as well as instances where castling is invalid (ex. king has already moved)

test_checkmate
    Tests the detection of a checkmate for both white and black kings

test_errors
    Tests types of movement errors that can occurr in the program
        -Move Syntax
        -Moving a non-existent piece
        -Moving the oppenents pieces
        -Moving the Bishop
        -Moving the Rook
        -Moving the Queen
        -Moving the Knight
        -Moving the Pawn
        -Moving the King/checking itself
        -Moving pieces over/through existing pieces
        -Moving to occupied squares of the same color pieces

test_move
    Tests valid move correctly moves the piece

test_undo
    Tests the playering being able to undo the previous move

test_view
    Tests the unicode display of each piece is correct
