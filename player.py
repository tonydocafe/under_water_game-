import pgzrun
from pgzero.actor import Actor

class Player:

    def __init__(self):
        self.actor = Actor("fexi1")
        self.actor.pos = (155, 342.5)

        self.images = ["fexi1", "fexi2", "fexi3", "fexi4"]
        self.images_up = ["fexi1_up", "fexi2_up", "fexi3_up","fexi4_up"]
        self.images_down = ["fexi1_down", "fexi2_down", "fexi3_down","fexi4_down"]
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