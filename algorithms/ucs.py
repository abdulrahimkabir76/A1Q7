# algorithms/ucs.py
import heapq
from node import Node
from utils import MOVES, move_cost

def ucs(grid, start, target, gui=None):
    heap = []
    heapq.heappush(heap, (0, start))
    visited = set()
    cost_so_far = {(start.row, start.col): 0}
    explored = set()
    frontier = set([(start.row, start.col)])
    expanded = 0

    while heap:
        curr_cost, current = heapq.heappop(heap)
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

        for dr, dc in MOVES:
            nr, nc = current.row + dr, current.col + dc
            if grid.in_bounds(nr, nc) and not grid.is_wall(nr, nc):
                next_pos = (nr, nc)
                cost = curr_cost + move_cost(pos, next_pos)
                if next_pos not in cost_so_far or cost < cost_so_far[next_pos]:
                    cost_so_far[next_pos] = cost
                    neighbor = Node(nr, nc, current, cost)
                    heapq.heappush(heap, (cost, neighbor))
                    if next_pos not in explored:
                        frontier.add(next_pos)
    return None, expanded, explored, frontier
