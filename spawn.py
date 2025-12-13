import random
from pgzero.actor import Actor
from pgzero.keyboard import Keyboard

class RocksSpawer:
    
    def __init__(self, speed):
        self.rocks = []
        
        self.rock_types = ["rock1", "rock2", "rock3", "rock4", "rock5"]
        self.total = random.randint(2, 10)

        self.x = 750 + random.randint(1760, 2400)
        self.dist_x = random.randint(250, 500)

        self.scored = False
        self.speed = speed

    def spawn_rocks(self):
        for i in range(self.total):           
            tipo = random.choice(self.rock_types)          
            rock = Actor(tipo)
            rock.y = 665
            rock.x = self.x + i * self.dist_x
            self.rocks.append(rock)
            self.scored = False

    def update(self, y, keyboard):

        if -1840 < -1750 + y < -1700:
            if len(self.rocks) == 0: 
                self.spawn_rocks()
                self.scored = False
                    
        for rock in self.rocks: 
            rock.x -= 5
            if keyboard.up and y < 1300: rock.y += 10
            if keyboard.down and (-1750 +y ) > -1750: rock.y -= 10
        
        self.rocks = [r for r in self.rocks if r.x > -800]

    def update_score(self, score):
        if not self.scored:

            
                if all(rock.x < -50 for rock in self.rocks):
                    self.scored = True
                    return 1   

        return 0
    
    def draw(self):
        for rock in self.rocks:
            rock.draw()

    def get_items(self):
            return self.rocks



class SharksSpawer:
    
    def __init__(self, speed):
        self.sharks = []
        self.speed = speed
        self.frames = ["tuba1", "tuba2", "tuba3", "tuba4"]
        self.total = random.randint(5, 10)

        self.x = 750 + random.randint(1760, 2400)
        self.dist_x = random.randint(250, 500)
        self.scored = False

    def spawn_sharks(self):
        for i in range(self.total):                  
            shark = Actor(self.frames[0] )
            shark.y = random.randint(40, 640)
            shark.x = self.x + i * self.dist_x
          
            shark.frames = self.frames
            shark.frame = 0
            shark.frame_timer = 0 
          
            self.sharks.append(shark)


    def update(self, y, keyboard):

        if -1040 < -1550 + y < -200:
            if len(self.sharks) == 0: 
                self.spawn_sharks()
                self.scored = False    
       
        for shark in self.sharks: 
            shark.x -= 25
            if keyboard.up and y < 1300: shark.y += 10
            if keyboard.down and (-1750 +y ) > -1750: shark.y -= 10
        
            shark.frame_timer += 1
            
            if shark.frame_timer >= 7: 
                shark.frame = (shark.frame + 1) % len(shark.frames)
                shark.image = shark.frames[shark.frame]
                shark.frame_timer = 0

        self.sharks = [s for s in self.sharks if s.x > -800]

    def update_score(self, score):
        if not self.scored:
            if all(shark.x < -500 for shark in self.sharks):
                self.scored = True
                return 1   
        return 0
    
    def get_items(self):
        return self.sharks
    
    def draw(self):
        for shark in self.sharks:
            shark.draw()