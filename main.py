import pgzrun
from player import Player
from spawn import RocksSpawer, SharksSpawer
from utils import draw_hearts, check_collision, draw_score,reset_game,draw_hit
from menu import Menu
from bg_spawn import BubbleUpSpawer,FishesSpawer
from plants_spawn import PlantsRedSpawer,PlantsGreenSpawer,PlantsPurpleSpawer

WIDTH = 750
HEIGHT = 685

bg_speed = 5
bg_x = 0
bg_y = 0

fish_spawner = FishesSpawer(0)
player = Player()
rocks_spawner = RocksSpawer(0)
sharks_spawner = SharksSpawer(0)
menu = Menu()
bubble_spawner = BubbleUpSpawer()
greenp_spawner = PlantsGreenSpawer()
red_p_spawner = PlantsRedSpawer(0)
purple_p_spawner = PlantsPurpleSpawer(0)

#sounds.music.play()

game_started = False
lives = 3
dano_cooldown = 0
game_over = False
score = 0
explosion = Actor("explosion")
explosion.visible = False
check_hit =  False
def draw():
    screen.clear()
    screen.blit("sean", (bg_x, bg_y- 1750))
    screen.blit("sean", (bg_x + WIDTH,bg_y - 1750))

    if not game_started:
        menu.draw(screen)
        return

    for f in fish_spawner.fishes: f.draw()
    for r in red_p_spawner.redplants: r.draw()
    player.draw()
    for s in sharks_spawner.sharks: s.draw()
    for pu  in purple_p_spawner.purples: pu.draw()
    for r in rocks_spawner.rocks: r.draw()
    for b in bubble_spawner.bubbles: b.draw()
    for pg in greenp_spawner.plants: pg.draw()
    
    draw_hearts(screen, lives)
    draw_score(screen, score)
   
    
    if explosion.visible:
        explosion.draw()


    if game_over:
        screen.draw.text("GAME OVER ", center=(WIDTH/2, HEIGHT/2), fontsize=64, color="red")
        screen.draw.text("\n Pressinone a tecla UP: jogar novamente\n\nPressione a tecla SPACE: ir paro o menu  ", center=(WIDTH//2, HEIGHT/4 - 40), fontsize=54, color="#FFFFFF")

def update():
    global bg_x, bg_y,lives, dano_cooldown, game_over,score,explosion,check_hit

    if game_over: return
    
    if menu.active: return


    bg_x -= bg_speed
    if bg_x <= -WIDTH: bg_x = 0

    fish_spawner.update(bg_y,keyboard)  
    sharks_spawner.update(bg_y,keyboard)
    player.update(keyboard)
    rocks_spawner.update(bg_y,keyboard)
    bubble_spawner.update(bg_y,keyboard)
    greenp_spawner.update(bg_y,keyboard)
    red_p_spawner.update(bg_y,keyboard)
    purple_p_spawner.update(bg_y,keyboard)

    if player.is_up_pressed(keyboard) and bg_y < 1300 :bg_y +=10
    if player.is_up_down(keyboard) and -1750 + bg_y > -1750 :bg_y -=10

    lives, dano_cooldown,check_hit = check_collision(player, rocks_spawner.rocks, lives, dano_cooldown,sounds.puch,check_hit)
    if check_hit:
        show_explosion(player.actor.x, player.actor.y)
        print("COLIDIU!")
   


    lives, dano_cooldown,check_hit = check_collision(player, sharks_spawner.sharks, lives, dano_cooldown,sounds.mordida,check_hit)
   
    score += rocks_spawner.update_score(score)
    score += sharks_spawner.update_score(score)
    if lives <= 0: game_over = True

def on_mouse_down(pos):
    global game_started

    result = menu.on_mouse_down(pos)
    if result == "start": game_started = True
    elif result == "music": pass  

    print("\n=== CLIQUE DETECTADO ===")
    print(f"Posição do clique: {pos}")

    print(f"Posição do background: x={bg_x}, y={bg_y}")


def hide_explosion():
    explosion.visible = False

def show_explosion(x, y):
    explosion.pos = (x, y)
    explosion.visible = True
    clock.schedule(hide_explosion, 0.3) 



def on_key_down(key):
    global bg_x, bg_y, lives, dano_cooldown, game_over, score, player, rocks_spawner,menu,game_started,sharks_spawner

    if  game_over:
        if key in (keys.UP, keys.DOWN):
            reset = reset_game()
            bg_x = reset["bg_x"]
            bg_y = reset["bg_y"]
            lives = reset["lives"]
            dano_cooldown = reset["dano_cooldown"]
            game_over = reset["game_over"]
            score = reset["score"]
            player = Player()
            red_p_spawner = PlantsRedSpawer(0)
            rocks_spawner = RocksSpawer(0)
            sharks_spawner = SharksSpawer(0)
            bubble_spawner = BubbleUpSpawer()
            greenp_spawner = PlantsGreenSpawer()
            fish_spawner = FishesSpawer(0)
            purple_p_spawner = PlantsPurpleSpawer(0)

        if key == keys.SPACE :
            game_over = False
            game_started = False
            menu.active = True
        return

