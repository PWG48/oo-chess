import chess.model as model
import chess.view as view

game = model.Game()
game.set_up_pieces()
while not game.game_over:
    print("")
    print(view.board_to_text(game.board))
    prompt = "White to play:" if game.white_to_play else "Black to play:"
    move = input(prompt)
    game.accept_move(move)
