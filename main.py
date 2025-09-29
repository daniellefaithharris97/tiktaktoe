import tkinter as tk
from game import TicTacToeGame
from ai import ComputerPlayer
from stats import GameStats

class TicTacToeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.geometry("400x500")
        # Load stats
        self.stats = GameStats()
        # Set up UI elements here (difficulty selection, board, stats, etc.)
        # You’ll implement the rest as you go!

if __name__ == "__main__":
    app = TicTacToeApp()
    app.mainloop()
