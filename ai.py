import random

class ComputerPlayer:
    def __init__(self, difficulty="low"):
        self.difficulty = difficulty

    def choose_move(self, board):
        # Returns (row, col) for computer's move
        if self.difficulty == "low":
            return self.random_move(board)
        elif self.difficulty == "medium":
            return self.medium_move(board)
        elif self.difficulty == "hard":
            return self.hard_move(board)

    def random_move(self, board):
        empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
        return random.choice(empty)

    def medium_move(self, board):
        # Basic blocking logic, add more later
        return self.random_move(board)

    def hard_move(self, board):
        # Implement minimax or similar here
        return self.random_move(board)
