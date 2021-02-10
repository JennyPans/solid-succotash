import pygame


class Game:
    """
    Classe comprenant la boucle de jeu
    """

    def __init__(self):
        self.is_running = True
        self.flags = pygame.RESIZABLE
        self.screen = pygame.display.set_mode((800, 600), self.flags, vsync=True)
        pygame.init()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        pass

    def render(self):
        self.screen.fill(pygame.Color(80, 50, 180))
        pygame.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()


if __name__ == '__main__':
    game = Game()
    game.run()
