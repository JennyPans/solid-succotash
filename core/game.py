import pygame
from constants import Constants


class Game:
    """
    Gère la fenêtre ainsi que la boucle de jeu.
    La boucle de jeu comprends le traitement des événéments, le moteur physique et le moteur graphique.
    """

    def __init__(self):
        self.is_running = True
        self.screen = pygame.display.set_mode(Constants.SIZE, Constants.FLAGS, vsync=True)
        pygame.init()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(pygame.Color(80, 50, 180))
        pygame.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
