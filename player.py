import pgzrun
from pgzero.actor import Actor

class Player:

    def __init__(self):
        self.actor = Actor("1_player")
        self.actor.pos = (155, 342.5)

        self.images = ["1_player", "2_player", "3_player", "4_player"]
        self.images_up = ["1up_player", "2up_player", "3up_player","4up_player"]
        self.images_down = ["1down_player", "2down_player", "3down_player","4down_player"]
        self.current_images = self.images
        self.frame = 0
        self.animation_speed = 5
        self.animation_counter = 0 
        self.speed = 3


    def update(self, keyboard):
       
        if keyboard.up:
            self.current_images = self.images_up
        elif keyboard.down:
            self.current_images = self.images_down
        else:
            self.current_images = self.images

        if keyboard.up:
            self.actor.y -= self.speed
        elif keyboard.down:
            self.actor.y += self.speed

        self.actor.y = max(150, min(685 - 85, self.actor.y))

        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.frame = (self.frame + 1) % len(self.current_images)
            self.actor.image = self.current_images[self.frame]
            self.animation_counter = 0

    def draw(self):
        self.actor.draw()   

    def is_up_pressed(self,keyboard):
        return keyboard.up 
    def is_up_down(self,keyboard):
        return keyboard.down