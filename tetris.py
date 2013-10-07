from __future__ import print_function
import pygame
import sys
import random
import tetromino
from pdb import set_trace


BASE_BLOCK_DIM = 30
WINDOW_SIZE = width, height = 800, 640

# Tetromino colors
colors = {
    #           R   G   B
    'CYAN':     (0, 255, 255),
    'BLUE':     (0, 0, 255),
    'ORANGE':   (255, 165, 0),
    'YELLOW':   (255, 255, 0),
    'GREEN':    (0, 255, 0),
    'PURPLE':   (170, 0, 255),
    'RED':      (255, 0, 0),
    'WHITE':    (255, 255, 255),
    'BLACK':    (0, 0, 0)
}

music = [
    'res/tetrisb.mid',
    'res/tetrisc.mid'
]

keys = {
    pygame.K_DOWN: (lambda x: print("DOWN")),
    pygame.K_LEFT: (lambda x: print("LEFT")),
    pygame.K_RIGHT: (lambda x: print("RIGHT")),
    pygame.K_ESCAPE: (lambda x: pygame.event.post(
        pygame.event.Event(pygame.QUIT))
    ),
    pygame.K_SPACE: (lambda x: print("DROP")),
    pygame.K_UP: (lambda x: print("ROTATE"))
}


class Visible(object):
    """ Visible class
    Base class for all visible elements
    """
    def __init__(self, screen):
        self.screen = screen
        self.render()

    def render(self):
        self.background = pygame.Surface(self.size)
        self.background.fill(colors['WHITE'])

    def blit(self):
        self.screen.blit(self.background, self.pos)


class Controllable(object):
    """Controllable class
    Base class for all elements that the user can control
    """
    def handle_keys(self, world, ev):
        pass


class Scoreboard(Visible):
    """Scoreboard class
    Creates a visible scoreboard in the upper left hand corner.
    The scoreboard class also contains scoring logic: 10 points per line.
    """
    size = width, height = 250, 150
    pos = xpos, ypos = 20, 20

    def render(self):
        super(Scoreboard, self).render()
        font = pygame.font.Font(None, 36)
        text = font.render("Scoreboard", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)


class NextTetromino(Visible):
    """NextTetromino class
    Creates a visible area that shows what the next tetromino will be.
    """
    size = width, height = 250, 200
    pos = xpos, ypos = 20, height + 20


class Well(Visible):
    """Well class
    Draws the board and handles gathering tetromino. Probably should handle \
    border collision too.

    Well is 10x20 tetromino blocks with 2 hidden rows at the top for \
    generating the next tetromino.
    """
    size = width, height = (BASE_BLOCK_DIM * 10), (BASE_BLOCK_DIM * 20)
    pos = xpos, ypos = (WINDOW_SIZE[0] - (BASE_BLOCK_DIM * 5))/2, 20

    def blank_well(self):
        well = []
        for i in range(self.width):
            well.append([' '] * self.height)
        return well


class GameState:
    """GameState class
    Contains global game information such as the score, the level, the well, \
    and references to the current and next tetrimino.
    """
    score = 0
    level = 1

    def __init__(self, screen):
        self.well = Well(screen)
        self.scoreboard = Scoreboard(screen)
        self.next = NextTetromino(screen)

    def calc_level(score):
        return int(score / 10) + 1

    def calc_speed(level):
        return (0.27 - (level * 0.02)) * 1000

    def blit(self):
        self.well.blit()
        self.scoreboard.blit()
        self.next.blit()


class Tetris:
    def __init__(self):
        self.running = True
        self.paused = False
        self.screen = None
        self.size = WINDOW_SIZE

    def setup(self):
        pygame.init()
        pygame.key.set_repeat(100, 100)
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(colors['BLACK'])
        # Initialize the GameState
        self.state = GameState(self.screen)

        # This is our initial timer
        pygame.time.set_timer(pygame.USEREVENT, 2000)

        self.running = True

    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        # Only valid keys are ESCAPE, DOWN, LEFT, RIGHT, and SPACE
        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key](event.key)
            elif event.key == pygame.K_BACKSPACE:
                print("backspace")
                self.paused = (True, False)[self.paused]

        if event.type == pygame.USEREVENT:
            print("timer elapsed")
            # This is where we handle a piece moving down the board

    def render(self):
        self.state.blit()
        pygame.display.flip()

    def quit(self):
        pygame.quit()

    def start(self):
        if self.setup() is False:
            self.running = False

        pygame.mixer.music.load(music[random.randint(0, 1)])
        pygame.mixer.music.play(-1, 0.0)

        while (self.running):
            for event in pygame.event.get():
                self.event(event)
            if not self.paused:
                self.render()
            else:
                pygame.mixer.music.stop()
        self.quit()


if __name__ == "__main__":
    # Set up everything
    tetris = Tetris()
    tetris.start()
