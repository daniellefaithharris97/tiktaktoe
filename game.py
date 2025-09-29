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
        # Rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                self.winner = row[0]
                return
        # Columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                self.winner = self.board[0][col]
                return
        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.winner = self.board[0][0]
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.winner = self.board[0][2]
            return
        # Tie
        if self.is_full() and self.winner is None:
            self.winner = "Tie"

    def is_full(self):
        return all(cell != "" for row in self.board for cell in row)
