# algorithms/bidirectional.py
from collections import deque
from node import Node
from utils import MOVES

def reconstruct_path(meet, parents_f, parents_b):
    # Reconstruct path from start to meet, then meet to target
    path_f = []
    node = meet
    while node:
        path_f.append((node.row, node.col))
        node = parents_f.get((node.row, node.col))
    path_b = []
    node = parents_b.get((meet.row, meet.col))
    while node:
        path_b.append((node.row, node.col))
        node = parents_b.get((node.row, node.col))
    return path_f[::-1] + path_b

def bidirectional(grid, start, target, gui=None):
    queue_f = deque([start])
    queue_b = deque([target])
    parents_f = {(start.row, start.col): None}
    parents_b = {(target.row, target.col): None}
    visited_f = set([(start.row, start.col)])
    visited_b = set([(target.row, target.col)])
    explored = set()
    frontier = set([(start.row, start.col), (target.row, target.col)])
    expanded = 0

    meet_node = None

    while queue_f and queue_b:
        # Forward step
        if queue_f:
            current_f = queue_f.popleft()
            pos_f = (current_f.row, current_f.col)
            frontier.discard(pos_f)
            explored.add(pos_f)
            expanded += 1

            if gui:
                gui.draw_grid(frontier, explored, set())
                import pygame
                pygame.time.delay(40)
                pygame.display.update()

            if pos_f in visited_b:
                meet_node = current_f
                break

            for dr, dc in MOVES:
                nr, nc = current_f.row + dr, current_f.col + dc
                if grid.in_bounds(nr, nc) and not grid.is_wall(nr, nc):
                    if (nr, nc) not in visited_f:
                        visited_f.add((nr, nc))
                        neighbor = Node(nr, nc)
                        parents_f[(nr, nc)] = current_f
                        queue_f.append(neighbor)
                        frontier.add((nr, nc))

        # Backward step
        if queue_b:
            current_b = queue_b.popleft()
            pos_b = (current_b.row, current_b.col)
            frontier.discard(pos_b)
            explored.add(pos_b)
            expanded += 1

            if gui:
                gui.draw_grid(frontier, explored, set())
                import pygame
                pygame.time.delay(40)
                pygame.display.update()

            if pos_b in visited_f:
                meet_node = Node(*pos_b)
                break

            for dr, dc in MOVES:
                nr, nc = current_b.row + dr, current_b.col + dc
                if grid.in_bounds(nr, nc) and not grid.is_wall(nr, nc):
                    if (nr, nc) not in visited_b:
                        visited_b.add((nr, nc))
                        neighbor = Node(nr, nc)
                        parents_b[(nr, nc)] = current_b
                        queue_b.append(neighbor)
                        frontier.add((nr, nc))

    if meet_node:
        path = reconstruct_path(meet_node, parents_f, parents_b)
        return path, expanded, explored, frontier
    return None, expanded, explored, frontier
