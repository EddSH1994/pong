import pygame
import sys

# constants
# game
GAME_CAPTION = 'Pong'

# window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
WINDOW_TOP_LEFT = (0, 0)
WINDOW_CENTER_X = (WINDOW_WIDTH / 2)
WINDOW_CENTER_Y = (WINDOW_HEIGHT / 2)

# colors
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

# game objects
BALL_WIDTH = 10
BALL_HEIGHT = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
PLAYER_STARTING_X = 10
PLAYER_STARTING_Y = (WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2)
OPPONENT_STARTING_X = (WINDOW_WIDTH - PADDLE_WIDTH - 10)
OPPONENT_STARTING_Y = (WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2)

# set up pygame
pygame.init()
pygame.display.set_caption(GAME_CAPTION)

# set up the window
window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(window_size)
background = pygame.Surface(window_size)
screen.blit(background, WINDOW_TOP_LEFT)

clock = pygame.time.Clock()


class GameObject:
    def __init__(self, width, height, color, x, y):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y

    def initialize(self):
        pygame.draw.rect(screen, color=self.color, rect=[self.x, self.y, self.width, self.height])

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, color=self.color, rect=[self.x, self.y, self.width, self.height])


player = GameObject(PADDLE_WIDTH, PADDLE_HEIGHT, COLOR_BLACK, PLAYER_STARTING_X, PLAYER_STARTING_Y)
opponent = GameObject(PADDLE_WIDTH, PADDLE_HEIGHT, COLOR_BLACK, OPPONENT_STARTING_X, OPPONENT_STARTING_Y)
ball = GameObject(BALL_WIDTH, BALL_HEIGHT, COLOR_BLACK, WINDOW_CENTER_X, WINDOW_CENTER_Y)


def start_game():
    screen.fill(COLOR_WHITE)

    player.initialize()
    opponent.initialize()
    ball.initialize()


def draw_screen():
    screen.fill((255, 255, 255))
    player.draw()
    opponent.draw()
    ball.draw()


def update_screen():
    pygame.display.update()


if __name__ == '__main__':
    # Initialize game
    start_game()

    # Main game loop
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move(player.x, player.y - 10)
                if event.key == pygame.K_DOWN:
                    player.move(player.x, player.y + 10)

        draw_screen()
        update_screen()
