import pygame

from constants import Constants
from game_object import GameObject


class Game:
    """
    Gère la fenêtre ainsi que la boucle de jeu.
    La boucle de jeu comprends le traitement des événéments, le moteur physique et le moteur graphique.
    """

    def __init__(self):
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(Constants.SIZE, Constants.FLAGS)
        self.player = GameObject()
        self.player.velocity.x = 0.001
        pygame.init()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        self.player.update()

    def draw(self, interpolation):
        self.screen.fill(Constants.BG_COLOR)
        self.player.draw(self.screen, interpolation)
        pygame.display.flip()

    def run(self):
        lag = 0.0
        while self.is_running:
            lag += self.clock.tick()
            self.handle_events()
            while lag >= Constants.MS_PER_TICK:
                self.update()
                lag -= Constants.MS_PER_TICK
            self.draw(lag / Constants.MS_PER_TICK)


if __name__ == '__main__':
    game = Game()
    game.run()
