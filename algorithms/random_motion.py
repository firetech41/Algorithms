import numpy as np
import pygame
import random

from resources.render.fire_sim import Fire


def start(env: Fire) -> None:
    pygame.display.set_caption("Random motion")
    action = random.choice([0, 1, 2, 3])
    get_new_position(env, action)
    env.render()
    pygame.time.delay(200)

def get_new_position(env: Fire, action: int) -> None:
    x, y = env.position
    match action:
        case 0:
            new_pos = (x - 1, y)
        case 1:
            new_pos = (x + 1, y)
        case 2:
            new_pos = (x, y - 1)
        case 3:
            new_pos = (x, y + 1)
        case _:
            new_pos = env.position
    env.position = np.clip(new_pos, 0, 9)