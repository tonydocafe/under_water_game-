import random
from pgzero.actor import Actor

def spawn_plants_red(WIDTH, HEIGHT, BG_LIMIT, bg_y):
    plants_red = []

    if not (-1840 < BG_LIMIT + bg_y < -1700):
        return plants_red

    start_x = WIDTH + random.randint(10, 20)
    dist_x = random.randint(10, 50)
    total = random.randint(10, 30)

    for i in range(total):
        spawn_x = start_x + i * dist_x
        y = HEIGHT - 10

        plant = Actor("red", (spawn_x, y))
        plants_red.append(plant)

    return plants_red


def spawn_rocks(WIDTH, HEIGHT, BG_LIMIT, bg_y,ROCK5_THRESHOLD):
    rocks = []
    rock_spawn_count = {
    "rock1": 0,
    "rock2": 0,
    "rock3": 0,
    "rock4": 0,
    "rock5": 0
    }


    rock_types = ["rock1", "rock2", "rock3", "rock4", "rock5"]

    if not (-1840 < BG_LIMIT + bg_y < -1700):
        return
    
    start_x = WIDTH + random.randint(1760, 2400)


    dist_x = random.randint(250, 500)

  
    total = random.randint(2, 10)

    y_por_tipo = {
        "rock1": HEIGHT - 20,
        "rock2": HEIGHT - 20,
        "rock3": HEIGHT - 20,
        "rock4": HEIGHT - 50,
        "rock5": HEIGHT - 50,
    }

    for i in range(total):
        spawn_x = start_x + i * dist_x
        if (rock_spawn_count["rock1"] >= ROCK5_THRESHOLD and
        rock_spawn_count["rock2"] >= ROCK5_THRESHOLD and
        rock_spawn_count["rock3"] >= ROCK5_THRESHOLD and
        rock_spawn_count["rock4"] >= ROCK5_THRESHOLD):
            allowed_types = rock_types
        else:
            allowed_types = ["rock1", "rock2", "rock3", "rock4"]

       
        rock_type = random.choice(allowed_types)
        
    
        rock_spawn_count[rock_type] += 1

        y = y_por_tipo[rock_type]
        rocks.append(Actor(rock_type, (spawn_x, y)))

    return rocks


def spawn_second(WIDTH, HEIGHT, BG_LIMIT, bg_y):
    
    if not (-1840 < BG_LIMIT + bg_y < -1000):
        return

    second = []
    used_y = []
    min_dist_y = 120
    start_x = WIDTH + random.randint(80, 200)
    dist_x = random.randint(90, 130)
    total = random.randint(4, 8)



    for i in range(total):
       
        for _ in range(20):
            y = random.randint(40, HEIGHT - 40)

            if all(abs(y - u) >= min_dist_y for u in used_y):
                used_y.append(y)

                
                spawn_x = start_x + i * dist_x
                fish_type = ["fish_gold","fish_black","fish_blue"]
                fish_choice = random.choice(fish_type)
                second.append(Actor(fish_choice, (spawn_x, y)))
                break
    return second



def spawn_bolha_up(WIDTH, HEIGHT, BG_LIMIT, bg_y,DISTANCIA_MIN):

    bolhas_up = []
    if not (-1840 < BG_LIMIT + bg_y < -650):
        return

    total = random.randint(5, 8)
   
    for _ in range(total):
        tentativas = 0
        
        while tentativas < 20:
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)

          
            ok = True
            for b in bolhas_up:
                dx = x - b.x
                dy = y - b.y
                dist = (dx*dx + dy*dy) ** 0.5
                if dist < DISTANCIA_MIN:  
                    ok = False
                    break

            if ok:   
                bolha = Actor("bolha1", (x, y))
                bolha.frames = ["bolha1", "bolha2", "bolha3", "bolha4"]
                bolha.frame = 0
                bolha.speed = random.uniform(1.0, 3.0)
                bolhas_up.append(bolha)
                break

            tentativas += 1
    return bolhas_up 

def spawn_plants(WIDTH, HEIGHT, BG_LIMIT, bg_y):
    
    plants = []
    plant_types = ["1purple", "2purple", "3purple", "4purple"]

    if not (-1840 < BG_LIMIT + bg_y < -1700):
        return

    start_x = WIDTH + random.randint(200, 500)
    dist_x = random.randint(58, 105)
    total = random.randint(1, 5)
    allowed_types = plant_types  


    for i in range(total):
        spawn_x = start_x + i * dist_x

        plant_type = random.choice(allowed_types)
        y = HEIGHT - 90

        plants.append(Actor(plant_type, (spawn_x, y)))
    return plants




def spawn_sharks(WIDTH, HEIGHT, BG_LIMIT, bg_y,SPEED):
   
    cond = BG_LIMIT + bg_y


    if not (-1550 < cond < -200):
        return
    
    sharks = []
    used = []
    min_dist = 120

    start_x = WIDTH + random.randint(80, 200)
    dist_x = random.randint(90, 130)
    total = random.randint(1, 3)

    for i in range(total):
        for _ in range(20):

            y = random.randint(40, HEIGHT - 40)

            if all(abs(y - u) >= min_dist for u in used):
                used.append(y)
                spawn_x = start_x + i * dist_x

                shark = None

               
                if -1550 < cond < -1000:
                    shark = Actor("tuba1", (spawn_x, y))
                    shark.frames = ["tuba1", "tuba2", "tuba3", "tuba4"]
                    shark.frame = 0
                    shark.speed = SPEED  

            
                elif -1000 <= cond < -400:
                    shark = Actor("block", (spawn_x, y))
                    shark.frames = ["block","block","block","block"]
                    shark.frame = 0
                    shark.speed = SPEED + 10  

                
                if shark is None:
                    continue

                sharks.append(shark)
                break
    return sharks


def spawn_plants_green(WIDTH, HEIGHT, BG_LIMIT, bg_y):
    plants_green = []

   
    if not (-1840 < BG_LIMIT + bg_y < -1700):
        return

    start_x = WIDTH + random.randint(50, 100)
    dist_x = random.randint(50, 100)
    total = random.randint(1, 20)

    for i in range(total):
        spawn_x = start_x + i * dist_x
        y = HEIGHT - 40

        plant = Actor("green1", (spawn_x, y))

   
        plant.frames = ["green1", "green2", "green3", "green4"]
        plant.frame = 0

        plants_green.append(plant)
    return plants_green