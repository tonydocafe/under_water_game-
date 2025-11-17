import random

ROCK5_THRESHOLD = 5
WIDTH = 750
HEIGHT = 685
BG_LIMIT = -1750
SPEED = 8
score = 0
BG_SPEED = 5 + score * 2     # velocidade do fundo

DISTANCIA_MIN =60
timer = 0
dano_cooldown = 0
bird = Actor('fexi1')

bird.pos = (155, HEIGHT // 2)
frames = ['fexi1', 'fexi2', 'fexi3', 'fexi4']
current_frame = 0

game_over = False

moving_up = False
moving_down = False

bg_x = 0          # posição inicial do fundo
bg_y = 0
lives = 3 
blocks =[]
second =[]
rocks =[]
plants = []
plants_green = []
plants_red= []
bolhas_up = []
def draw():
    screen.clear()

    # Desenha duas cópias do fundo lado a lado
    screen.blit("sean", (bg_x,bg_y + BG_LIMIT))
    screen.blit("sean", (bg_x + WIDTH,bg_y + BG_LIMIT))

    for b in blocks: b.draw()
    for pr in plants_red: pr.draw()
    for p in plants: p.draw()
    for pg in plants_green: pg.draw()
    for s in second: s.draw()
    for r in rocks: r.draw()
    for bolha in bolhas_up: bolha.draw()

    
    bird.draw()
    
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
        screen.blit("heart", (10 + i * 40, 30))  # 10px do topo, 40px entre os corações




def spawn_rocks():
    global rocks, bg_y
    rocks = []
    rock_spawn_count = {
    "rock1": 0,
    "rock2": 0,
    "rock3": 0,
    "rock4": 0,
    "rock5": 0
    }


    rock_types = ["rock1", "rock2", "rock3", "rock4", "rock5"]

    # Só spawnar se estiver na parte certa do mapa
    if not (-1840 < BG_LIMIT + bg_y < -1700):
        return
    
    # Posição X inicial, bem fora da tela
    start_x = WIDTH + random.randint(1760, 2400)

    # Espaçamento horizontal entre as rochas
    dist_x = random.randint(250, 500)

    # Quantidade de rochas no grupo
    total = random.randint(2, 10)

    # Altura de cada tipo
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

        # Escolhe o tipo permitido
        rock_type = random.choice(allowed_types)
        
        # Atualiza o contador
        rock_spawn_count[rock_type] += 1

        y = y_por_tipo[rock_type]
        rocks.append(Actor(rock_type, (spawn_x, y)))
def spawn_plants():
    global plants, bg_y
    plants = []

    plant_types = ["1purple", "2purple", "3purple", "4purple"]

    # Só spawnar se estiver na parte certa do mapa
    if not (-1840 < BG_LIMIT + bg_y < -1700):
        return

    # Posição X inicial fora da tela
    start_x = WIDTH + random.randint(200, 500)

    # Espaçamento horizontal
    dist_x = random.randint(58, 105)

    # Quantidade de plantas no grupo
    total = random.randint(1, 5)

    # Escolhe todos os tipos possíveis (nenhuma restrição aqui)
    allowed_types = plant_types  

    # Spawns
    for i in range(total):
        spawn_x = start_x + i * dist_x

        plant_type = random.choice(allowed_types)
        y = HEIGHT - 90

        plants.append(Actor(plant_type, (spawn_x, y)))

def spawn_plants_green():
    global plants_green, bg_y
    plants_green = []

    # Só spawnar se estiver na parte certa do mapa
    if not (-1840 < BG_LIMIT + bg_y < -1700):
        return

    start_x = WIDTH + random.randint(50, 100)
    dist_x = random.randint(50, 100)
    total = random.randint(1, 20)

    for i in range(total):
        spawn_x = start_x + i * dist_x
        y = HEIGHT - 40

        plant = Actor("green1", (spawn_x, y))

        # cria as animações
        plant.frames = ["green1", "green2", "green3", "green4"]
        plant.frame = 0

        plants_green.append(plant)

def spawn_plants_red():
    global plants_red, bg_y
    plants_red = []

    # Só spawnar se estiver na parte certa do mapa
    if not (-1840 < BG_LIMIT + bg_y < -1700):
        return

    start_x = WIDTH + random.randint(10, 20)
    dist_x = random.randint(10, 50)
    total = random.randint(10, 30)

    for i in range(total):
        spawn_x = start_x + i * dist_x
        y = HEIGHT - 10

        plant = Actor("red", (spawn_x, y))

        plants_red.append(plant)


def spawn_blocks():
    global blocks, bg_y

    cond = BG_LIMIT + bg_y

    # Só spawnar se estiver no mapa dos inimigos
    if not (-1550 < cond < -200):
        return
    
    blocks = []
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

                block = None

                # -------------------------------
                # ÁREA DOS TUBARÕES
                # -------------------------------
                if -1550 < cond < -1000:
                    block = Actor("tuba1", (spawn_x, y))
                    block.frames = ["tuba1", "tuba2", "tuba3", "tuba4"]
                    block.frame = 0
                    block.speed = SPEED  # velocidade dos tubarões

                # -------------------------------
                # ÁREA DOS BLOCOS
                # -------------------------------
                elif -1000 <= cond < -400:
                    block = Actor("block", (spawn_x, y))
                    block.frames = ["block","block","block","block"]
                    block.frame = 0
                    block.speed = SPEED + 10  # velocidade dos blocos

                # Se nada for válido, tenta outra posição
                if block is None:
                    continue

                blocks.append(block)
                break



def spawn_bolha_up():
    global bolhas_up
    
    # Condição onde as bolhas devem começar a spawnar
    if not (-1840 < BG_LIMIT + bg_y < -650):
        return

    # quantidade aleatória de bolhas
    total = random.randint(5, 8)

    for _ in range(total):
        tentativas = 0
        
        while tentativas < 20:
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)

            # Verifica distância da nova bolha para as existentes
            ok = True
            for b in bolhas_up:
                dx = x - b.x
                dy = y - b.y
                dist = (dx*dx + dy*dy) ** 0.5
                if dist < DISTANCIA_MIN:  # muito perto?
                    ok = False
                    break

            if ok:   # posição válida, pode criar
                bolha = Actor("bolha1", (x, y))
                bolha.frames = ["bolha1", "bolha2", "bolha3", "bolha4"]
                bolha.frame = 0
                bolha.speed = random.uniform(1.0, 3.0)
                bolhas_up.append(bolha)
                break

            tentativas += 1

def spawn_second():
    global second, bg_y
    if not (-1840 < BG_LIMIT + bg_y < -1000):
        return

    second = []
    used_y = []
    min_dist_y = 120

    # Posição X inicial bem fora da tela (entre 80 e 200 px fora)
    start_x = WIDTH + random.randint(80, 200)

    # Espaçamento horizontal entre os peixes
    dist_x = random.randint(90, 130)

    # Número total de peixes no grupo
    total = random.randint(4, 8)



    for i in range(total):
        # Encontrar Y com espaçamento mínimo
        for _ in range(20):
            y = random.randint(40, HEIGHT - 40)

            if all(abs(y - u) >= min_dist_y for u in used_y):
                used_y.append(y)

                # Cada peixe fica atrás do outro (para a direita)
                spawn_x = start_x + i * dist_x
                fish_type = ["fish_gold","fish_black","fish_blue"]
                fish_choice = random.choice(fish_type)
                second.append(Actor(fish_choice, (spawn_x, y)))
                break

def reset_game():
    global lives,score, game_over, moving_up, moving_down,bg_y,bg_x
    bg_y = 0 
    score = 0
    lives = 3
    game_over = False
    moving_up = False
    moving_down = False
    bird.pos = (155, HEIGHT // 2)
    spawn_blocks()
    spawn_second()
    spawn_blocks()
    spawn_plants()
    spawn_plants_green()
    spawn_plants_red()
    spawn_bolha_up()
    draw_hearts()
    

def update():
    global game_over, score, moving_up, moving_down, bg_x,bg_y,blocks,second,rocks,plants,plants_green,plants_red,bolhas_up, current_frame,timer 
    global lives, dano_cooldown
    if game_over:
        return


 

    if dano_cooldown > 0:
        dano_cooldown -= 1


    timer +=1
  # move o fundo para a esquerda
    bg_x -= BG_SPEED

    # quando a primeira imagem sair, reinicia a posição
    if bg_x <= -WIDTH:
        bg_x = 0

    if bg_y >= 1300:
        bg_y = 1300

    # Movimento do personagem
    if moving_up:
        if bg_y < 1300:

            bird.y -= 10
            bird.angle = 0 
            bird.angle += 5
            
            bg_y += 10
            for b in blocks: b.y +=10
            for s in second: s.y += 10
            for r in rocks: r.y +=10
            for p in plants: p.y +=10
            for pg in plants_green: pg.y +=10
            for pr in plants_red: pr.y +=10
            for bolha in bolhas_up: bolha.y += 10
        
    if moving_down:
        bird.y += 10
        bird.angle = 0 
        if BG_LIMIT + bg_y > -1750:
            bird.angle -= 15
            bg_y -= 10
            for b in blocks: b.y -=10    
            for s in second: s.y -=10 
            for r in rocks: r.y -=10      
            for p in plants: p.y -=10
            for pg in plants_green: pg.y -=10
            for pr in plants_red: pr.y -=10 
            for bolha in bolhas_up: bolha.y -= 10
   
    # Movimento dos blocos
    
    for b in blocks:b.x -= b.speed


    for s in second: s.x -= BG_SPEED + 1
    for r in rocks: r.x -= BG_SPEED 
    for p in plants: p.x -= BG_SPEED    
    for pg in plants_green: pg.x -= BG_SPEED
    for pr in plants_red: pr.x -= BG_SPEED 
    for bolha in bolhas_up: bolha.x -= BG_SPEED 
    # Quando todos os blocos passarem
    if all(b.right < 0 for b in blocks):
        if bg_y > 230:
            score += 1
        if bg_y >= 900:
            score +=0.5       
        spawn_blocks()
    if all(s.right < 0 for s in second):spawn_second()
    if all(bolha.right < 250 for bolha in bolhas_up):spawn_bolha_up()
    if bird.y >= 342:
        if all(r.right < 0 for r in rocks):spawn_rocks()
        if all(pr.right < 100 for pr in plants_red):spawn_plants_red()
        if all(p.right < 10 for p in plants):spawn_plants()
        if all(pg.right < 10 for pg in plants_green):spawn_plants_green()
   
   
   #atulização de frame
    for pg in plants_green:
        pg.frame += 0.08
        if pg.frame >= len(pg.frames):
            pg.frame = 0

        pg.image = pg.frames[int(pg.frame)]
   
    for b in blocks:
        b.frame += 0.08
        if b.frame >= len(b.frames):
            b.frame = 0

        b.image = b.frames[int(b.frame)]
  
    for bolha in bolhas_up[:]:
            # movimentação para cima
            bolha.y -= bolha.speed

            # animação
            bolha.frame = (bolha.frame + 0.08) % len(bolha.frames)
            bolha.image = bolha.frames[int(bolha.frame)]

            # remove quando sai da tela
            if bolha.y < -20:
                bolhas_up.remove(bolha)

    
    if timer % 8 == 0:  # muda o frame a cada 8 updates
        current_frame = (current_frame + 1) % len(frames)
        bird.image = frames[current_frame]


    for r in rocks:
        if bird.colliderect(r):

            if dano_cooldown == 0:
                lives -= 1
                dano_cooldown = 60   # 1 segundo de invencibilidade

                if lives <= 0:
                    game_over = True





    for b in blocks:

        # bird alinhado verticalmente?
        colide_y = abs(bird.y - b.y) < (bird.height/2 + b.height/2)

        if colide_y:

            bloco_a_frente = b.x > bird.x
            bate_frente = (bird.x + bird.width/2) > (b.x - b.width/2)

            if bloco_a_frente and bate_frente:

                # só tomar dano se cooldown == 0
                if dano_cooldown == 0:
                    lives -= 1
                    dano_cooldown = 300  # ~0.5 segundos (se update = 60fps)

                    if lives <= 0:
                        game_over = True

  

    # BG_Limites verticais
    bird.y = max(150, min(HEIGHT - 85, bird.y))


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
    print(f"Posição do personagem: x={bird.x}, y={bird.y}")
    print(f"Posição do background: x={bg_x}, y={bg_y}")
