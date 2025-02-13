import pygame
from pygame import Surface
from pygame.event import Event

import core.const as c

pygame.init()


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.color = c.GRAY
        self.hover_color = c.BLUE
        self.is_hovered = False

    def draw(self, screen: Surface) -> None:
        mouse_pos = pygame.mouse.get_pos()
        self.is_hovered = self.rect.collidepoint(mouse_pos)

        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, current_color, self.rect)

        text_surface = self.font.render(self.text, True, c.BLACK)
        text_rect = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event: Event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                return True
        return False
