class GameStats():
    def __init__(self, sw_game):
        self.game_active = True
        self.settings = sw_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0