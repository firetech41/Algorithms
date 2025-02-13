import pygame
from pygame import Surface

import core.const as c
from resources.render.button import Button


class Fire:
    def __init__(self) -> None:
        self.screen_size = c.SCREEN_SIZE
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.cell = c.CELL_SIZE
        self.buttons = {}
        self.obstacles = c.OBSTACLES_COORDS
        self.fire = c.FIRE_COORDS
        self.base = c.BASE_COORDS
        self.position = self.base
        self.counter_steps = 0

    def render(self) -> None:
        self.screen.fill(c.WHITE)
        BASE = load_image("resources/images/base.jpg", self.cell)
        AGENT = load_image("resources/images/drone.jpg", self.cell)
        OBSTACLE = load_image("resources/images/tree.jpg", self.cell)
        FIRE = load_image("resources/images/fire.jpg", self.cell)
        self.screen.blit(BASE, (self.base[0] * self.cell, self.base[1] * self.cell))
        self.screen.blit(FIRE, (self.fire[0] * self.cell, self.fire[1] * self.cell))
        self.screen.blit(AGENT, (self.position[0] * self.cell, self.position[1] * self.cell))
        for i in self.obstacles:
            self.screen.blit(OBSTACLE, (i[0] * self.cell, i[1] * self.cell))
        pygame.display.flip()

    def fill_screen(self) -> None:
        self.screen.fill(c.WHITE)

    def get_counter_steps(self) -> int:
        return self.counter_steps

    def increment_counter(self) -> None:
        self.counter_steps = self.counter_steps + 1

    def add_button(self, x: int, y: int, width: int, height: int, text: str) -> None:
        self.buttons[text] = Button(x, y, width, height, text)

    def get_button(self, text: str) -> Button:
        return self.buttons.get(text)

def load_image(filename: str, size: int) -> Surface:
    image = pygame.image.load(filename)
    return pygame.transform.scale(image, (size, size))
