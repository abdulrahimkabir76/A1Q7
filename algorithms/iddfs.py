# algorithms/iddfs.py
from node import Node
from utils import MOVES
import pygame
import time

def iddfs(grid, start, target, gui=None, max_depth=20):
    expanded_total = 0
    explored = set()
    frontier = set()
    for limit in range(1, max_depth + 1):
        stack = [(start, 0)]
        visited = set()
        explored_iter = set()
        frontier_iter = set([(start.row, start.col)])
        found = False
        if gui:
            gui.set_info(f"IDDFS: Depth Limit {limit}")
            gui.draw_grid(frontier_iter, explored_iter, set())
            pygame.display.update()
            pygame.time.delay(200)
        while stack:
            current, depth = stack.pop()
            pos = (current.row, current.col)
            frontier_iter.discard(pos)
            explored_iter.add(pos)
            expanded_total += 1

            if gui:
                gui.draw_grid(frontier_iter, explored_iter, set())
                pygame.time.delay(40)
                pygame.display.update()

            if pos == (target.row, target.col):
                path = []
                while current:
                    path.append((current.row, current.col))
                    current = current.parent
                explored.update(explored_iter)
                frontier.update(frontier_iter)
                return path[::-1], expanded_total, explored, frontier

            if depth < limit:
                for dr, dc in MOVES[::-1]:
                    nr, nc = current.row + dr, current.col + dc
                    if grid.in_bounds(nr, nc) and not grid.is_wall(nr, nc):
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            neighbor = Node(nr, nc, current, depth=depth+1)
                            stack.append((neighbor, depth+1))
                            frontier_iter.add((nr, nc))
        explored.update(explored_iter)
        frontier.update(frontier_iter)
        if gui:
            gui.set_info(f"IDDFS: Increasing depth to {limit+1}")
            gui.draw_grid(frontier_iter, explored_iter, set())
            pygame.display.update()
            pygame.time.delay(200)
    return None, expanded_total, explored, frontier
