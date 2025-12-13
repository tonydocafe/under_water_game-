from utils import check_collision
from pgzero.actor import Actor


def update_background(bg_x, bg_speed, width):
    bg_x -= bg_speed
    if bg_x <= -width:
        bg_x = 0
    return bg_x


def update_spawners(bg_y, keyboard, spawners):
    for spawner in spawners:
        spawner.update(bg_y, keyboard)


def handle_collisions(player, collision_sources, lives, dano_cooldown, check_hit, show_explosion):

    for enemies, sound in collision_sources:
        lives, dano_cooldown, check_hit = check_collision(
            player,
            enemies,
            lives,
            dano_cooldown,
            sound,
            check_hit
        )

        if check_hit:
            show_explosion(player.actor.x, player.actor.y)

    return lives, dano_cooldown, check_hit
