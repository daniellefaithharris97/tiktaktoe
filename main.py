import tkinter as tk
from tkinter import messagebox
from game import TicTacToeGame
from ai import ComputerPlayer
from stats import GameStats

class TicTacToeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.geometry("400x500")
        self.resizable(False, False)

        # Load stats and game
        self.stats = GameStats()
        self.game = TicTacToeGame()
        self.difficulty = tk.StringVar(value="low")
        self.computer = ComputerPlayer(self.difficulty.get())

        # UI widgets
        self.create_widgets()
        self.update_stats()

    def create_widgets(self):
        # Difficulty selection
        frame = tk.Frame(self)
        frame.pack(pady=10)
        tk.Label(frame, text="Difficulty:").pack(side="left")
        for lvl in ["low", "medium", "hard"]:
            tk.Radiobutton(frame, text=lvl.capitalize(), variable=self.difficulty, value=lvl, command=self.set_difficulty).pack(side="left")
        
        # Stats display
        self.stats_label = tk.Label(self, text="", font=("Arial", 12))
        self.stats_label.pack(pady=5)

        # Game board
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        board_frame = tk.Frame(self)
        board_frame.pack(pady=10)
        for r in range(3):
            for c in range(3):
                btn = tk.Button(board_frame, text="", font=("Arial", 24), width=5, height=2,
                                command=lambda row=r, col=c: self.player_move(row, col))
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn

        # Reset button
        tk.Button(self, text="Restart Game", command=self.reset_game).pack(pady=10)

    def set_difficulty(self):
        self.computer = ComputerPlayer(self.difficulty.get())

    def update_stats(self):
        s = self.stats.data
        diff = self.difficulty.get()
        self.stats_label.config(
            text=f"Player Wins ({diff.title()}): {s['player'][diff]}   Computer Wins ({diff.title()}): {s['computer'][diff]}"
        )

    def player_move(self, row, col):
        if self.game.board[row][col] != "" or self.game.winner:
            return
        self.game.make_move(row, col)
        self.update_board()
        if self.game.winner:
            self.handle_game_end()
            return
        if not self.game.is_full():
            self.after(500, self.computer_move)

    def computer_move(self):
        move = self.computer.choose_move(self.game.board)
        if move:
            self.game.make_move(*move)
            self.update_board()
            if self.game.winner:
                self.handle_game_end()

    def update_board(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text=self.game.board[r][c])

    def handle_game_end(self):
        winner = self.game.winner
        diff = self.difficulty.get()
        if winner == "X":
            self.stats.record_win("player", diff)
            messagebox.showinfo("Game Over", "You win!")
        elif winner == "O":
            self.stats.record_win("computer", diff)
            messagebox.showinfo("Game Over", "Computer wins!")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")
        self.update_stats()

    def reset_game(self):
        self.game.reset_board()
        self.update_board()

if __name__ == "__main__":
    app = TicTacToeApp()
    app.mainloop()
