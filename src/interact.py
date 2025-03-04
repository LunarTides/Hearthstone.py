import os


class Interact:
    def __init__(self, game):
        self.game = game

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def watermark(self):
        return "Hearthstone.py"
