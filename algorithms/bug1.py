import numpy as np
import pygame

import core.const as c
from resources.render.fire_sim import Fire


def start(env: Fire) -> None:
    pygame.display.set_caption("Bug1 algorithm")
    while env.position != env.fire:
        if not move_towards_goal(env, env.fire):
            if not follow_obstacle(env):
                print("The goal is unattainable")
        env.increment_counter()
        env.render()
        pygame.time.delay(400)

def is_valid_move(env: Fire, next_position: tuple) -> bool:
    x, y = next_position
    return (0 <= x < c.GRID and
            0 <= y < c.GRID and
            next_position not in env.obstacles)

def move_towards_goal(env: Fire, goal: tuple) -> bool:
    x, y = env.position
    dx = np.sign(goal[0] - x)
    dy = np.sign(goal[1] - y)

    if dx != 0 and dy != 0:
        next_pos = (x + dx, y)
        if is_valid_move(env, next_pos):
            env.position = next_pos
            return True
        next_pos = (x, y + dy)
        if is_valid_move(env, next_pos):
            env.position = next_pos
            return True
    else:
        next_pos = (x + dx, y + dy)
        if is_valid_move(env, next_pos):
            env.position = next_pos
            return True

    return False

def follow_obstacle(env: Fire) -> bool:
    barrier_point = env.position
    visited_points = set()
    closest_point = barrier_point
    min_distance = distance(barrier_point, env.fire)
    last_direction = ""

    while True:
        possible_moves = get_possible_moves(env)
        directions = get_direction(possible_moves, last_direction)
        for direction in directions:
            next_position = possible_moves[direction]
            if next_position not in visited_points:
                last_direction = direction
                env.position = next_position
                visited_points.add(env.position)
                env.increment_counter()
                env.render()
                pygame.time.delay(400)

                distance_to_goal = distance(env.position, env.fire)
                if distance_to_goal < min_distance:
                    closest_point = env.position
                    min_distance = distance_to_goal
                break
        else:
            return False

        if env.position == barrier_point:
            move_towards_goal(env, closest_point)
            return False

        if env.position == closest_point:
            return True

def get_direction(possible_moves: dict, last_direction: tuple) -> list[str] | None:
    moves = ["Right", "Down", "Left", "Up"]
    traj = set(moves) - set(possible_moves.keys())
    if len(traj) == 1:
        traj = list(traj)[0]
        match traj:
            case "Up":
                return ["Left", "Up", "Right", "Down"]
            case "Right":
                return ["Up", "Right", "Down", "Left"]
            case "Down":
                return ["Right", "Down", "Left", "Up"]
            case "Left":
                return ["Down", "Left", "Up", "Right"]
    elif len(traj) == 0:
        match last_direction:
            case "Left":
                return ["Up", "Right", "Down", "Left"]
            case "Up":
                return ["Right", "Down", "Left", "Up"]
            case "Right":
                return ["Down", "Left", "Up", "Right"]
            case "Down":
                return ["Left", "Up", "Right", "Down"]
    else:
        return list(set(moves) & set(possible_moves.keys()))

def distance(a: [int], b: [int]) -> int:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def get_possible_moves(env: Fire) -> dict:
    x, y = env.position
    moves = {}
    if is_valid_move(env, (x + 1, y)):
        moves['Right'] = (x + 1, y)
    if is_valid_move(env, (x, y + 1)):
        moves['Down'] = (x, y + 1)
    if is_valid_move(env, (x - 1, y)):
        moves['Left'] = (x - 1, y)
    if is_valid_move(env, (x, y - 1)):
        moves['Up'] = (x, y - 1)
    return moves