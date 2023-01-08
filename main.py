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
BALL_MOMENTUM_X = 1
BALL_MOMENTUM_Y = 1
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
PADDLE_MOVEMENT = 10
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

    def draw(self):
        pygame.draw.rect(screen, color=self.color, rect=[self.x, self.y, self.width, self.height])


class Player(GameObject):
    def move_up(self):
        if (self.y - PADDLE_MOVEMENT) > 0:
            self.y -= PADDLE_MOVEMENT

    def move_down(self):
        if (self.y + PADDLE_MOVEMENT) < (WINDOW_HEIGHT - PADDLE_HEIGHT):
            self.y += PADDLE_MOVEMENT


class Ball(GameObject):
    def move(self):
        # handle collision with paddle
        # handle goal for player
        # handle goal for opposition

        # otherwise
        self.x += BALL_MOMENTUM_X
        self.y += BALL_MOMENTUM_Y


player = Player(PADDLE_WIDTH, PADDLE_HEIGHT, COLOR_BLACK, PLAYER_STARTING_X, PLAYER_STARTING_Y)
opponent = Player(PADDLE_WIDTH, PADDLE_HEIGHT, COLOR_BLACK, OPPONENT_STARTING_X, OPPONENT_STARTING_Y)
ball = Ball(BALL_WIDTH, BALL_HEIGHT, COLOR_BLACK, WINDOW_CENTER_X, WINDOW_CENTER_Y)


def start_game():
    screen.fill(COLOR_WHITE)

    player.initialize()
    opponent.initialize()
    ball.initialize()


def draw_screen():
    screen.fill(COLOR_WHITE)

    player.draw()

    opponent.draw()

    ball.move()
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
                    player.move_up()
                if event.key == pygame.K_DOWN:
                    player.move_down()

        draw_screen()
        update_screen()
