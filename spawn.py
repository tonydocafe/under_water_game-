import random
from pgzero.actor import Actor
from pgzero.keyboard import keys

class RocksSpawer:
    
    def __init__(self, y):
        self.rocks = []
        
        self.rock_types = ["rock1", "rock2", "rock3", "rock4", "rock5"]
        self.total = random.randint(2, 10)

        self.x = 750 + random.randint(1760, 2400)
        self.dist_x = random.randint(250, 500)

    def spawn_rocks(self):
        for i in range(self.total):           
            tipo = random.choice(self.rock_types)          
            rock = Actor(tipo)
            rock.y = 665
            rock.x = self.x + i * self.dist_x
            self.rocks.append(rock)

    def update(self, y, keyboard):

        if -1840 < -1750 + y < -1700:
            if len(self.rocks) == 0: self.spawn_rocks()    
        for rock in self.rocks: 
            rock.x -= 5
            if keyboard.up and y < 1300: rock.y += 10
            if keyboard.down and (-1750 +y ) > -1750: rock.y -= 10
        
        self.rocks = [r for r in self.rocks if r.x > -800]

    def update_score(self, score):
            pontos = 0
            for rock in self.rocks:
                if rock.x < -50:
                    pontos += 1 
            return score + pontos