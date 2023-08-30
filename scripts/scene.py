import pygame


class Scene:
    def __init__(self):
        pygame.display.set_caption('NomeScene')

        self.display = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()  # um tipo de array

        self.active = True

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.active = False
                # pygame.quit()

    def draw(self):
        self.all_sprites.draw(self.display)

    def update(self):
        self.all_sprites.update()
