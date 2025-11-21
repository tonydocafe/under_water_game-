import random
from pgzero.actor import Actor
from player import Player
from spawn import RocksSpawer


def draw_hearts(screen, lives):
    for i in range(lives):
        screen.blit("heart", (10 + i * 40, 30))


def draw_score(screen, score):
    screen.draw.text( f"Score: {score}",(10, 10), fontsize=40, color="white" )

def update_score(score, amount): return score + amount

def check_collision(player, rocks, lives, cooldown, sound):
    
    if cooldown > 0:
        return lives, cooldown - 1


    
    for r in rocks:
        if player.actor.colliderect(r):
            sound.stop()
            sound.play()    
            lives -= 1
            cooldown = 60  
            break

    return lives, cooldown

def reset_game(player, rocks_spawner):
    player.actor.pos = (100, 300)
    rocks_spawner.rocks.clear()
    rocks_spawner.spawn_timer = 0


def reset_game():

    return {
        "bg_x": 0,
        "bg_y": 0,
        "lives": 3,
        "dano_cooldown": 0,
        "game_over": False,
        "score": 0
    }
