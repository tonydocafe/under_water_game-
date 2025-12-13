import random
from pgzero.actor import Actor

class PlantsGreenSpawer:
    
    def __init__(self):
        self.plants = []
        self.frames = ["green1", "green2", "green3", "green4"]
        

    def spawn_greenp(self, bg_y):
        if not (-1840 < -1750 + bg_y < -1700):
            return

        start_x = 850 + random.randint(25, 50)
        dist_x = random.randint(40, 100)
        total = random.randint(10, 15)

        for i in range(total):
            x = start_x + i * dist_x
            y = 675

            plant = Actor(self.frames[0], (x, y))
            plant.frames = self.frames
            plant.frame = 0
            plant.frame_timer = 0
            self.plants.append(plant)

    def update(self, y, keyboard):
        if -1840 < -1750 + y < -1700 and not self.plants:
            self.spawn_greenp(y)

        for p in self.plants:
            p.x -= 5
            if keyboard.up and y < 1300:
                p.y += 10
            if keyboard.down and (-1750 + y) > -1750:
                p.y -= 10

            p.frame_timer += 1
            if p.frame_timer >= 15:
                p.frame = (p.frame + 1) % len(p.frames)
                p.image = p.frames[p.frame]
                p.frame_timer = 0

        self.plants = [p for p in self.plants if p.x > -50]

    def draw(self):
        for plant in self.plants:
            plant.draw()

    def get_items(self):
        return self.plants

class PlantsRedSpawer:
    def __init__(self, y):
        self.redplants = []
        self.total = random.randint(20, 30)
        self.x = 750 + random.randint(10, 20)
        self.dist_x = random.randint(10, 50)

    def spawn_redplants(self):
        for i in range(self.total):
            redplant = Actor("red")
            redplant.y = 675
            redplant.x = self.x + i * self.dist_x
            self.redplants.append(redplant)

    def update(self, y, keyboard):
        if -1840 < -1750 + y < -1700 and not self.redplants:
            self.spawn_redplants()

        for redplant in self.redplants:
            redplant.x -= 5
            if keyboard.up and y < 1300:
                redplant.y += 10
            if keyboard.down and (-1750 + y) > -1750:
                redplant.y -= 10

        self.redplants = [r for r in self.redplants if r.x > -800]

    def draw(self):
        for redplant in self.redplants:
            redplant.draw()

    def get_items(self):
        return self.redplants


class PlantsPurpleSpawer:
    def __init__(self, y):
        self.purples = []
        self.purple_types = ["1purple", "2purple", "3purple", "4purple"]
        self.total = random.randint(1, 5)
        self.x = 750 + random.randint(200, 500)
        self.dist_x = random.randint(58, 105)

    def spawn_purples(self):
        for i in range(self.total):
            tipo = random.choice(self.purple_types)
            purple = Actor(tipo)
            purple.y = 595
            purple.x = self.x + i * self.dist_x
            self.purples.append(purple)

    def update(self, y, keyboard):
        if -1840 < -1750 + y < -1700 and not self.purples:
            self.spawn_purples()

        for purple in self.purples:
            purple.x -= 5
            if keyboard.up and y < 1300:
                purple.y += 10
            if keyboard.down and (-1750 + y) > -1750:
                purple.y -= 10

        self.purples = [p for p in self.purples if p.x > -800]

    def draw(self):
        for purple in self.purples:
            purple.draw()

    def get_items(self):
        return self.purples
