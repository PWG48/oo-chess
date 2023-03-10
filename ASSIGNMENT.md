# `oo-chess`
In this assignment you will use Objected Oriented Design and Programming techniquies to implement the rules of Chess. Wikipedia 
has a pretty good summary [here](https://en.wikipedia.org/wiki/Rules_of_chess).

## What you're provided to start:
* Python container setup (docker-compose + Dockerfile);
* A few model objects:
    * Board -- Represents the chess-board;
    * Piece -- An abstract class for chess-pieces: Handles some basic identity issues.
    * Pawn -- A concrete implementation of Piece.
    * Game -- Knows the board and who's turn it is.
* A few view functions for visualizing a piece and a board in the terminal.
* A __main__.py that integrates the above pieces into a text-based app.

## What you'll need to implement
You'll need to implement the following user-stories:

As a player...
* I want to enter a move like 'e2e4' and see the piece at e2 moved to e4.
* I want to receive an error if I try to... 
    * enter an ill-formatted move -- i.e. anything not of the form `[a..h][1..8][a..h][1..8]`.
    * move a non-existent piece. 
    * move my opponent's piece.
    * move my bischop to any square not on its diagonal.
    * move my rook to any square not on its row or column.
    * move my queen to any square not on its row, column, or diagonal.
    * move my knight to any square not 3x2 squares aware.
    * move any piece other than a knight over existing pieces.
    * move any piece to a square occupied by another of my pieces.
    * move my pawn in violation of pawn-movement rules.
    * move my king in violation of king-movement rules.
    * make a move that results in my king being in check.
    * make any other moves prohibited by [movement rules](https://en.wikipedia.org/wiki/Rules_of_chess#Movement)
* I want to move my king two squares towards my rook and see the rook also moved to complete a castle.
* I want to receive an error if any of the castling conditions don't hold.
* I want to enter 'backup' and undo a move.
* I want the game to complete when either player is checkmated.


# What you'll hand in
* A link to your homework group's github repository that will contain:
   * A working chess program.
   * A DESIGN.md file that explains the design of your system to a developer wishing to use or extend your system.
   * A RETROSPECTIVE.md file summarizing the agile retrospective meeting you'll hold after you complete the work for this assignment. (Nuclino has a decent description of Agile Retrospectives [here](https://www.nuclino.com/articles/sprint-retrospective-meeting))

# How you'll get an A
* I can clone your repository, start the container, run `python -m chess`, and complete several moves in an interactive session.
* You have written functional tests to exercise each of the user-stories outlined above.
* Your code is readable: Meaningful names, comments where apropriate, keep modules, classes, and functions small, etc.
* Your code is well organized and demonstrates good use of object oriented design principles like:
    * Separation of Concerns / Single responsibility principle.
    * Favor Cohesion / Avoid Coupling.
    * Use of design patterns.
* Your code has good unit-test coverage.
* All tests pass.
* Your Design Document is a good piece of technical writing with sections, descriptive prose, etc.
* Your Design Document includes UML diagrams:
      * A class-diagram documenting the classes in the system.
      * An object-diagram depicting a chess-game after several moves;
      * An interaction diagram depicting the interaction between objects when:
         *  A user enters a valid move;
         *  A user enters an invalid move;
* Your retrospective describes: 
   *  A short narrative of how your team members collaborated.
   *  A summary of what your team did well.
   *  A summary of what your team could do better next time.

Extra Credit Stories:
* I want to enter 'resign' to resign and end the game.

