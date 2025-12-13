import pgzrun

from player import Player
from spawn import RocksSpawer, SharksSpawer
from bg_spawn import BubbleUpSpawer, FishesSpawer
from plants_spawn import (
    PlantsRedSpawer,
    PlantsGreenSpawer,
    PlantsPurpleSpawer
)

from utils import draw_hearts, draw_score, reset_game
from menu import Menu
from effects import explosion, show_explosion
from game_logic import update_background, handle_collisions
from game_state import GameState

WIDTH = 750
HEIGHT = 685

# =========================
# ESTADO CENTRAL
# =========================
state = GameState()
menu = Menu()
player = Player()


# =========================
# FÁBRICA DE SPAWNERS
# =========================
def create_spawners():
    return {
        "fish": FishesSpawer(0),
        "rocks": RocksSpawer(0),
        "sharks": SharksSpawer(0),
        "bubbles": BubbleUpSpawer(),
        "green_plants": PlantsGreenSpawer(),
        "red_plants": PlantsRedSpawer(0),
        "purple_plants": PlantsPurpleSpawer(0),
    }


spawners = create_spawners()


# =========================
# DRAW
# =========================
def draw_background():
    screen.blit("sean", (state.bg_x, state.bg_y - 1750))
    screen.blit("sean", (state.bg_x + WIDTH, state.bg_y - 1750))


def draw_entities():
    for spawner in spawners.values():
        spawner.draw()

    player.draw()


def draw_ui():
    draw_hearts(screen, state.lives)
    draw_score(screen, state.score)

    if explosion.visible:
        explosion.draw()

    if state.game_over:
        screen.draw.text(
            "GAME OVER",
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=64,
            color="red",
        )
        screen.draw.text(
            "\nPressione UP: jogar novamente\n\nPressione SPACE: menu",
            center=(WIDTH // 2, HEIGHT // 4 - 40),
            fontsize=54,
            color="#FFFFFF",
        )


def draw():
    screen.clear()
    draw_background()

    if not state.game_started:
        menu.draw(screen)
        return

    draw_entities()
    draw_ui()


# =========================
# UPDATE
# =========================
def update_spawners_all():
    for spawner in spawners.values():
        spawner.update(state.bg_y, keyboard)


def update_player_movement():
    player.update(keyboard)

    if player.is_up_pressed(keyboard) and state.bg_y < 1300:
        state.bg_y += 10

    if player.is_up_down(keyboard) and -1750 + state.bg_y > -1750:
        state.bg_y -= 10


def update():
    if state.game_over or menu.active:
        return

    state.bg_x = update_background(state.bg_x, state.bg_speed, WIDTH)

    update_spawners_all()
    update_player_movement()

    state.lives, state.dano_cooldown, state.check_hit = handle_collisions(
        player,
        [
            (spawners["rocks"].get_items(), sounds.puch),
            (spawners["sharks"].get_items(), sounds.mordida),
        ],
        state.lives,
        state.dano_cooldown,
        state.check_hit,
        show_explosion,
    )

    state.score += spawners["rocks"].update_score(state.score)
    state.score += spawners["sharks"].update_score(state.score)

    if state.lives <= 0:
        state.game_over = True


# =========================
# INPUT
# =========================
def on_mouse_down(pos):
    result = menu.on_mouse_down(pos)
    if result == "start":
        state.game_started = True


def restart_game():
    global player, spawners

    reset = reset_game()
    state.apply_reset(reset)

    player = Player()
    spawners = create_spawners()


def on_key_down(key):
    if state.game_over and key in (keys.UP, keys.DOWN):
        restart_game()

    if state.game_over and key == keys.SPACE:
        state.game_over = False
        state.game_started = False
        menu.active = True
