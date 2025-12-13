import random
from pgzero.actor import Actor

class BubbleUpSpawer:

    def __init__(self):
        self.bubbles = []
        self.frames = ["bolha1", "bolha2", "bolha3", "bolha4"]
        self.total = random.randint(80, 100)
        self.dist_min = 60

    def _new_bubble(self, x, y):
        bubble = Actor(self.frames[0], (x, y))
        bubble.frames = self.frames
        bubble.frame_index = 0
        bubble.frame_timer = 0
        bubble.speed = random.uniform(1.0, 2.5)
        return bubble

    def spawn_bubbles(self):
        for _ in range(self.total):

            for _ in range(5):  
                x = random.randint(0, 750)
                y = random.randint(0, 685)

                if all((x-b.x)**2 + (y-b.y)**2 >= self.dist_min**2 for b in self.bubbles):
                    self.bubbles.append(self._new_bubble(x, y))
                    break

    def update(self, bg_y, keyboard):

        if -1840 < -1750 + bg_y < -650 and not self.bubbles: self.spawn_bubbles()

        for b in self.bubbles:

            b.y -= b.speed
            b.x -= 5

           
            if keyboard.up and bg_y < 1300:  
                b.y += 10
            if keyboard.down and (-1750 + bg_y) > -1750:  
                b.y -= 10

           
            b.frame_timer += 1
            if b.frame_timer >= 7:
                b.frame_index = (b.frame_index + 1) % 4
                b.image = b.frames[b.frame_index]
                b.frame_timer = 0

           
            if b.y < -20:
                b.x = random.randint(0, 1050)
                b.y = random.randint(0, 650)
                b.speed = random.uniform(1.0, 2.5)

       
        self.bubbles = [b for b in self.bubbles if b.y > -200]
    
    def get_items(self):
        return self.bubbles

    def draw(self):
        for b in self.bubbles:
            b.pos = (int(b.x), int(b.y))
            b.draw()


class FishesSpawer:
    
    def __init__(self, y):
        self.fishes = []
        
        self.fish_types = ["fish1", "fish2", "fish3"]
        self.total = random.randint(2, 10)

        self.x = 750 + random.randint(1760, 2400)
        self.dist_x = random.randint(250, 500)

    def spawn_fishes(self):
        for i in range(self.total):           
            tipo = random.choice(self.fish_types)          
            fish = Actor(tipo)
            fish.y = random.randint(40,640)
            fish.x = self.x + i * self.dist_x
            self.fishes.append(fish)

    def update(self, y, keyboard):

        if -1840 < -1750 + y < -1000:
            if len(self.fishes) == 0: self.spawn_fishes()    
        for fish in self.fishes: 
            fish.x -= 10
            if keyboard.up and y < 1300: fish.y += 10
            if keyboard.down and (-1750 +y ) > -1750: fish.y -= 10
        
        self.fishes = [f for f in self.fishes if f.x > -800]

    def get_items(self):
        return self.fishes

    def draw(self):
        for fish in self.fishes:
            fish.draw()