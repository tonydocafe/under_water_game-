
from pgzero.actor import Actor
from pgzero.loaders import sounds

class Menu:
    def __init__(self):
        self.start_button = Actor("btn-start")
        self.start_button.pos = (400, 350)

        self.exit_button = Actor("btn-quit")
        self.exit_button.pos = (400, 450)
       
        self.btn_music_on = Actor("btn-white", (30, 30))
        self.btn_music_off = Actor("white-btn", (30, 30))

        self.btn_change_music = Actor("btn-decision", (30, 100))
        self.music_enabled = True

        self.current_music = 0
        self.music_list = ["ocean","guitar","waves", "music"]
        self.active = True

   
    def draw(self,screen):
        if not self.active: return
      
        screen.blit("sean", (0, 0))
        screen.draw.text("mova o personagem seta cima/baixo ", center=(400, 650), fontsize=50, color="white")
        screen.draw.text("Jogo subquatico onde voce deve desviar das rochas e tubarões", midleft=(700, 140), angle=-90)
        screen.draw.text("UnderWater", center=(400, 150),fontsize =70, shadow=(1.0,3.0), scolor="blue")

        self.start_button.draw()
        self.exit_button.draw()
        
        if self.music_enabled:
            self.btn_music_on.draw()
        else:
            self.btn_music_off.draw()

        self.btn_change_music.draw()
        screen.draw.text("Trocar/Tocar", center=(50, 70), fontsize=20, color="white")

    def on_mouse_down(self, pos):
        if not self.active:
            return None

        if self.start_button.collidepoint(pos):
            self.active = False
            return "start"

        if self.exit_button.collidepoint(pos):
            pgzrun.quit()
            
        if self.music_enabled and self.btn_music_on.collidepoint(pos):
            self.toggle_music()

        elif not self.music_enabled and self.btn_music_off.collidepoint(pos):
            self.toggle_music()

        if self.btn_change_music.collidepoint(pos):
            self.change_music()
        return None


    def toggle_music(self):
        self.music_enabled = not self.music_enabled

        sound = getattr(sounds, self.music_list[self.current_music])

        if self.music_enabled:
            sound.play(-1)
        else:
            sound.stop()


    def change_music(self):
        if not self.music_enabled:
            return


        getattr(sounds, self.music_list[self.current_music]).stop()


        self.current_music = (self.current_music + 1) % len(self.music_list)

    
        getattr(sounds, self.music_list[self.current_music]).play(-1)
