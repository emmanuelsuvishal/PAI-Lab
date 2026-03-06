class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        print()
        for i in range(0, 9, 3):
            print(self.board[i] + " | " + self.board[i+1] + " | " + self.board[i+2])
            if i < 6:
                print("--+---+--")
        print()

    def is_winner(self, player):
        # rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player:
                return True

        # columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] == player:
                return True

        # diagonals
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True

        return False

    def is_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_full()

    def get_available_moves(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def make_move(self, move):
        self.board[move] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def undo_move(self, move):
        self.board[move] = ' '
        self.current_player = 'O' if self.current_player == 'X' else 'X'


def minimax(game, maximizing, alpha, beta):
    if game.is_game_over():
        if game.is_winner('O'):
            return 1
        elif game.is_winner('X'):
            return -1
        else:
            return 0

    if maximizing:  # AI (O)
        best = float('-inf')

        for move in game.get_available_moves():
            game.make_move(move)
            score = minimax(game, False, alpha, beta)
            game.undo_move(move)

            best = max(best, score)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:  # Human (X)
        best = float('inf')

        for move in game.get_available_moves():
            game.make_move(move)
            score = minimax(game, True, alpha, beta)
            game.undo_move(move)

            best = min(best, score)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


def get_best_move(game):
    best_score = float('-inf')
    best_move = None

    for move in game.get_available_moves():
        game.make_move(move)
        score = minimax(game, False, float('-inf'), float('inf'))
        game.undo_move(move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# Game Start
game = TicTacToe()

print("Positions are numbered from 0 to 8 as below:")
print("0 | 1 | 2")
print("--+---+--")
print("3 | 4 | 5")
print("--+---+--")
print("6 | 7 | 8")

while not game.is_game_over():
    game.print_board()

    if game.current_player == 'X':
        try:
            move = int(input("Enter your move (0-8): "))
        except ValueError:
            print("Invalid input!")
            continue

        if move not in game.get_available_moves():
            print("Invalid move! Try again.")
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
    print("It's a draw!")
