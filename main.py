from abc import ABC, abstractmethod
import pygame
import sys

# set up pygame
pygame.init()

# set up the window
surface = pygame.display.set_mode((500, 400), 0, 32)
clock = pygame.time.Clock()

pygame.display.set_caption('Pong')


class GameObject(ABC):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    @abstractmethod
    def move(self, x, y):
        pass


class Player(GameObject):
    def move(self, x, y):
        pygame.draw.rect(surface, color=self.color, rect=[x, y, self.width, self.height])


player = Player(10, 50, (0, 0, 0))
opponent = Player(10, 50, (0, 0, 0))


def start_game():
    surface.fill((255, 255, 255))

    player.move(10, 175)
    opponent.move(480, 175)
    pygame.display.flip()


if __name__ == '__main__':
    # Initialize game
    start_game()

    # Main game loop
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
