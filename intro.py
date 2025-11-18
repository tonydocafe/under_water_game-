import random
from spawn import spawn_plants_red, spawn_rocks,spawn_second,spawn_bolha_up,spawn_plants,spawn_sharks,spawn_plants_green

ROCK5_THRESHOLD = 5
WIDTH = 750
HEIGHT = 685
BG_LIMIT = -1750
SPEED = 8
score = 0
BG_SPEED = 5 + score * 2   

DISTANCIA_MIN =60
timer = 0
dano_cooldown = 0
player = Actor('fexi1')

player.pos = (155, HEIGHT // 2)
frames = ['fexi1', 'fexi2', 'fexi3', 'fexi4']
current_frame = 0

game_over = False
moving_up = False
moving_down = False

bg_x = 0         
bg_y = 0
lives = 3 
sharks =[]
second =[]
rocks =[]
plants = []
plants_green = []
plants_red= []
bolhas_up = []
def draw():
    screen.clear()

    screen.blit("sean", (bg_x,bg_y + BG_LIMIT))
    screen.blit("sean", (bg_x + WIDTH,bg_y + BG_LIMIT))

    for b in sharks: b.draw()
    for pr in plants_red: pr.draw()
    for p in plants: p.draw()
    for pg in plants_green: pg.draw()
    for s in second: s.draw()
    for r in rocks: r.draw()
    for bolha in bolhas_up: bolha.draw()

    
    player.draw()
    
    draw_hearts()


    screen.draw.text(f"Score: {score}", (10, 10), fontsize=40, color="white")

    if game_over:
        screen.draw.text(
            "GAME OVER",
            center=(WIDTH//2, HEIGHT//2 - 40),
            fontsize=70,
            color="orange"
        )
        screen.draw.text(
            "Pressione UP ou DOWN para reiniciar",
            center=(WIDTH//2, HEIGHT//2 + 20),
            fontsize=35,
            color="white"
        )

def draw_hearts():
    for i in range(lives):
        screen.blit("heart", (10 + i * 40, 30)) 

def reset_game():
    global lives,score, game_over, moving_up, moving_down,bg_y,bg_x
    bg_y = 0 
    score = 0
    lives = 3
    game_over = False
    moving_up = False
    moving_down = False
    player.pos = (155, HEIGHT // 2)
   
    new_shark = spawn_sharks(WIDTH, HEIGHT, BG_LIMIT, bg_y,SPEED)
    if new_shark: sharks.extend(new_shark)
   
    new_second = spawn_second(WIDTH, HEIGHT, BG_LIMIT, bg_y)
    if new_second: second.extend(new_second) 

    new_bolha = spawn_bolha_up(WIDTH, HEIGHT, BG_LIMIT, bg_y,DISTANCIA_MIN)
    if new_bolha: bolhas_up.extend(new_bolha) 

    new_rock = spawn_rocks(WIDTH, HEIGHT, BG_LIMIT, bg_y,ROCK5_THRESHOLD)
    if new_rock: rocks.extend(new_rock)

    plant_red = spawn_plants_red(WIDTH, HEIGHT, BG_LIMIT, bg_y)
    if plant_red:plants_red.extend(plant_red)    
    
    new_plant = spawn_plants(WIDTH, HEIGHT, BG_LIMIT, bg_y)
    if new_plant: plants.extend(new_plant)
    
    new_plant_green = spawn_plants_green(WIDTH, HEIGHT, BG_LIMIT, bg_y)
    if new_plant_green: plants_green.extend(new_plant_green)

#    draw_hearts()
    

def update():
    global game_over, score, moving_up, moving_down, bg_x,bg_y
    global sharks,second,rocks,plants,plants_green,plants_red,bolhas_up 
    global lives, dano_cooldown, current_frame,timer
    if game_over:
        return

    if dano_cooldown > 0:
        dano_cooldown -= 1

    timer +=1
#move o fundo 
    bg_x -= BG_SPEED
    
    if bg_x <= -WIDTH:
        bg_x = 0

    if bg_y >= 1300:
        bg_y = 1300

#movimento do personagem
    if moving_up:
        if bg_y < 1300:

            player.y -= 10
            player.angle = 0 
            player.angle += 5
            
            bg_y += 10
            for b in sharks: b.y +=10
            for s in second: s.y += 10
            for r in rocks: r.y +=10
            for p in plants: p.y +=10
            for pg in plants_green: pg.y +=10
            for pr in plants_red: pr.y +=10
            for bolha in bolhas_up: bolha.y += 10
        
    if moving_down:
        player.y += 10
        player.angle = 0 
        if BG_LIMIT + bg_y > -1750:
            player.angle -= 15
            bg_y -= 10
            for b in sharks: b.y -=10    
            for s in second: s.y -=10 
            for r in rocks: r.y -=10      
            for p in plants: p.y -=10
            for pg in plants_green: pg.y -=10
            for pr in plants_red: pr.y -=10 
            for bolha in bolhas_up: bolha.y -= 10
   
#movimento dos blocos
    
    for b in sharks:b.x -= b.speed


    for s in second: s.x -= BG_SPEED + 1
    for r in rocks: r.x -= BG_SPEED 
    for p in plants: p.x -= BG_SPEED    
    for pg in plants_green: pg.x -= BG_SPEED
    for pr in plants_red: pr.x -= BG_SPEED 
    for bolha in bolhas_up: bolha.x -= BG_SPEED 
#quando todos os blocos passarem
    if all(b.right < 0 for b in sharks):
        if bg_y > 230: score += 1
        if bg_y >= 900: score +=0.5       
        new_shark = spawn_sharks(WIDTH, HEIGHT, BG_LIMIT, bg_y,SPEED)
        if new_shark: sharks.extend(new_shark)
    
    if all(s.right < 0 for s in second):
        new_second = spawn_second(WIDTH, HEIGHT, BG_LIMIT, bg_y)
        if new_second: second.extend(new_second)    

    if all(bolha.right < 250 for bolha in bolhas_up):
        
        new_bolha = spawn_bolha_up(WIDTH, HEIGHT, BG_LIMIT, bg_y,DISTANCIA_MIN)
        if new_bolha: bolhas_up.extend(new_bolha) 
    
    if player.y >= 342:#limite de spawn 
        
        if all(r.right < 0 for r in rocks):
            new_rock = spawn_rocks(WIDTH, HEIGHT, BG_LIMIT, bg_y,ROCK5_THRESHOLD)
            if new_rock: rocks.extend(new_rock)          
        
        
        if all(pr.right < 100 for pr in plants_red):
            plant_red = spawn_plants_red(WIDTH, HEIGHT, BG_LIMIT, bg_y)
            if plant_red:plants_red.extend(plant_red)  
      
        if all(p.right < 10 for p in plants):
            new_plant = spawn_plants(WIDTH, HEIGHT, BG_LIMIT, bg_y)
            if new_plant: plants.extend(new_plant)

        if all(pg.right < 10 for pg in plants_green):
            new_plant_green = spawn_plants_green(WIDTH, HEIGHT, BG_LIMIT, bg_y)
            if new_plant_green: plants_green.extend(new_plant_green)


#atulização de frame
    for pg in plants_green:
        pg.frame += 0.08
        if pg.frame >= len(pg.frames):
            pg.frame = 0

        pg.image = pg.frames[int(pg.frame)]
   
    for b in sharks:
        b.frame += 0.08
        if b.frame >= len(b.frames):
            b.frame = 0

        b.image = b.frames[int(b.frame)]
  
    for bolha in bolhas_up[:]:
           
            bolha.y -= bolha.speed

            bolha.frame = (bolha.frame + 0.08) % len(bolha.frames)
            bolha.image = bolha.frames[int(bolha.frame)]

           
            if bolha.y < -20:
                bolhas_up.remove(bolha)

    
    if timer % 8 == 0:  
        current_frame = (current_frame + 1) % len(frames)
        player.image = frames[current_frame]


    for r in rocks:
        if player.colliderect(r):

            if dano_cooldown == 0:
                lives -= 1
                dano_cooldown = 60  

                if lives <= 0:
                    game_over = True





    for b in sharks:

        
        colide_y = abs(player.y - b.y) < (player.height/2 + b.height/2)

        if colide_y:

            bloco_a_frente = b.x > player.x
            bate_frente = (player.x + player.width/2) > (b.x - b.width/2)

            if bloco_a_frente and bate_frente:

                
                if dano_cooldown == 0:
                    lives -= 1
                    dano_cooldown = 300  

                    if lives <= 0:
                        game_over = True

  

#limites verticais
    player.y = max(150, min(HEIGHT - 85, player.y))


def on_key_down(key):
    global moving_up, moving_down
    if game_over:
        if key in (keys.UP, keys.DOWN):
            reset_game()
        return

    if key == keys.UP:
        moving_up = True
    elif key == keys.DOWN:
        moving_down = True


def on_key_up(key):
    global moving_up, moving_down

    if key == keys.UP:
        moving_up = False
    elif key == keys.DOWN:
        moving_down = False

def on_mouse_down(pos):
    print("\n=== CLIQUE DETECTADO ===")
    print(f"Posição do clique: {pos}")
    print(f"Posição do personagem: x={player.x}, y={player.y}")
    print(f"Posição do background: x={bg_x}, y={bg_y}")
