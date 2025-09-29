class TicTacToeGame:
    def __init__(self):
        self.reset_board()

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # Player always 'X'
        self.winner = None

    def make_move(self, row, col):
        if self.board[row][col] == "" and self.winner is None:
            self.board[row][col] = self.current_player
            self.check_winner()
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows, columns, diagonals for a winner
        # Set self.winner = "X" or "O"
        pass  # Fill in logic here!

    def is_full(self):
        return all(cell != "" for row in self.board for cell in row)
