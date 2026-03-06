class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-----")

    def is_winner(self, player):
        
        for i in range(0, 9, 3):
            if all(self.board[j] == player for j in range(i, i+3)):
                return True

        
        for i in range(3):
            if all(self.board[j] == player for j in range(i, 9, 3)):
                return True

        
        if all(self.board[i] == player for i in [0,4,8]):
            return True
        if all(self.board[i] == player for i in [2,4,6]):
            return True

        return False

    def is_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_full()

    def get_available_moves(self):
        return [i for i,v in enumerate(self.board) if v == ' ']

    def make_move(self, move):
        self.board[move] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def undo_move(self, move):
        self.board[move] = ' '
        self.current_player = 'O' if self.current_player == 'X' else 'X'


def minimax(game, maximizing):
    if game.is_game_over():
        if game.is_winner('O'):
            return 1
        elif game.is_winner('X'):
            return -1
        else:
            return 0

    if maximizing:
        best = float('-inf')
        for move in game.get_available_moves():
            game.make_move(move)
            score = minimax(game, False)
            game.undo_move(move)
            best = max(best, score)
        return best
    else:
        best = float('inf')
        for move in game.get_available_moves():
            game.make_move(move)
            score = minimax(game, True)
            game.undo_move(move)
            best = min(best, score)
        return best


def get_best_move(game):
    best_score = float('-inf')
    best_move = None

    for move in game.get_available_moves():
        game.make_move(move)
        score = minimax(game, False)
        game.undo_move(move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


game = TicTacToe()

while not game.is_game_over():
    game.print_board()

    if game.current_player == 'X':
        try:
            move = int(input("Enter move (0-8): "))
        except ValueError:
            print("Invalid input!")
            continue

        if move not in game.get_available_moves():
            print("Invalid move!")
            continue

        game.make_move(move)

    else:
        print("AI is thinking...")
        move = get_best_move(game)
        print("AI plays:", move)
        game.make_move(move)

game.print_board()

if game.is_winner('X'):
    print("You win!")
elif game.is_winner('O'):
    print("AI wins!")
else:
    print("Draw!")
