
from pgzero.actor import Actor
from pgzero.loaders import sounds

class Menu:
    def __init__(self):
        self.start_button = Actor("btn-start")
        self.start_button.pos = (400, 350)
        self.exit_button = Actor("btn-quit")
        self.exit_button.pos = (400, 450)

        # Botões de música
        self.btn_music_on = Actor("btn-white", (30, 30))
        self.btn_music_off = Actor("white-btn", (30, 30))

        self.music_enabled = True



        
        

        self.active = True

    # --------------------
    # DESENHAR O MENU
    # --------------------
    def draw(self,screen):
        if not self.active:
            return

      
        screen.blit("sean", (0, 0))

        # Título
        screen.draw.text("Meu Jogo", center=(400, 150),
                         fontsize=70, color="white")

        # Botão Start
        self.start_button.draw()
        self.exit_button.draw()

        # Botão Música
        if self.music_enabled:
            self.btn_music_on.draw()
        else:
            self.btn_music_off.draw()

    # --------------------
    # ATUALIZAÇÃO
    # --------------------
  

    # --------------------
    # CLIQUE DO MOUSE
    # --------------------
    def on_mouse_down(self, pos):
        if not self.active:
            return None

        # Clique Start
        if self.start_button.collidepoint(pos):
            self.active = False
            return "start"

        if self.exit_button.collidepoint(pos):
            pgzrun.quit()
            

        # Clique Botão de música
        if self.music_enabled and self.btn_music_on.collidepoint(pos):
            self.toggle_music()

        elif not self.music_enabled and self.btn_music_off.collidepoint(pos):
            self.toggle_music()

        return None

    # --------------------
    # TOGGLE DA MÚSICA
    # --------------------
    def toggle_music(self):
        self.music_enabled = not self.music_enabled

        if self.music_enabled:
            sounds.music.play()
        else:
            sounds.music.stop()
