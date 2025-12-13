class GameState:
    def __init__(self):
        self.bg_x = 0
        self.bg_y = 0
        self.bg_speed = 2

        self.lives = 3
        self.score = 0

        self.dano_cooldown = 0
        self.check_hit = False

        self.game_started = False
        self.game_over = False

    def apply_reset(self, data):
        self.bg_x = data["bg_x"]
        self.bg_y = data["bg_y"]
        self.lives = data["lives"]
        self.score = data["score"]
        self.dano_cooldown = data["dano_cooldown"]
        self.game_over = False
        self.check_hit = False
