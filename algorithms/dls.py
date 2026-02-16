# algorithms/dls.py
from node import Node
from utils import MOVES

def dls(grid, start, target, gui=None, limit=10):
    stack = [(start, 0)]
    visited = set()
    explored = set()
    frontier = set([(start.row, start.col)])
    expanded = 0

    while stack:
        current, depth = stack.pop()
        pos = (current.row, current.col)
        frontier.discard(pos)
        explored.add(pos)
        expanded += 1

        if gui:
            gui.draw_grid(frontier, explored, set())
            import pygame
            pygame.time.delay(40)
            pygame.display.update()

        if pos == (target.row, target.col):
            path = []
            while current:
                path.append((current.row, current.col))
                current = current.parent
            return path[::-1], expanded, explored, frontier

        if depth < limit:
            for dr, dc in MOVES[::-1]:  # Reverse for stack order
                nr, nc = current.row + dr, current.col + dc
                if grid.in_bounds(nr, nc) and not grid.is_wall(nr, nc):
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        neighbor = Node(nr, nc, current, depth=depth+1)
                        stack.append((neighbor, depth+1))
                        frontier.add((nr, nc))
    return None, expanded, explored, frontier
