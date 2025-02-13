import logging
import pygame

import algorithms.random_motion as random_motion
import algorithms.bug1 as bug1

from tkinter import messagebox
from resources.render.fire_sim import Fire


def run() -> None:
    running = True
    try:
        env = Fire()
        env.add_button(125, 200, 250, 80, "Random motion")
        env.add_button(125, 100, 250, 80, "Bug1 algorithm")

        current_screen = "Menu"
        pygame.display.set_caption("Fire simulator")

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if current_screen == "Menu":
                    if env.get_button("Random motion").is_clicked(event):
                        current_screen = "Random motion"
                    elif env.get_button("Bug1 algorithm").is_clicked(event):
                        current_screen = "Bug1 algorithm"

            if current_screen == "Menu":
                menu_screen(env)
            elif current_screen == "Random motion":
                random_motion.start(env)
            elif current_screen == "Bug1 algorithm":
                bug1.start(env)
                messagebox.showinfo("Bug1 algorithm", "The goal has been achieved. "
                                    + "Number of steps: " + str(env.get_counter_steps()))
                running = False

            pygame.display.flip()
            pygame.time.delay(60)

    except KeyboardInterrupt:
        logging.info("Interrupt")
    except Exception:
        logging.error("Error")
        raise
    finally:
        pygame.quit()

def menu_screen(env: Fire) -> None:
    env.fill_screen()
    env.get_button("Random motion").draw(env.screen)
    env.get_button("Bug1 algorithm").draw(env.screen)
