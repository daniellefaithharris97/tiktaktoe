import json
import os

class GameStats:
    def __init__(self, filename="stats.json"):
        self.filename = filename
        self.data = self.load_stats()

    def load_stats(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        else:
            return {"player": {"low": 0, "medium": 0, "hard": 0},
                    "computer": {"low": 0, "medium": 0, "hard": 0}}

    def save_stats(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f)

    def record_win(self, winner, difficulty):
        if winner in ["player", "computer"]:
            self.data[winner][difficulty] += 1
            self.save_stats()
