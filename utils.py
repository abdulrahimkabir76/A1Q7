# utils.py
import math

MOVES = [
    (-1, 0),   # Up
    (0, 1),    # Right
    (1, 0),    # Down
    (0, -1),   # Left
    (1, 1),    # Bottom-Right
    (-1, -1)   # Top-Left
]

COLOR_MAP = {
    "start": (0, 200, 0),
    "target": (200, 0, 0),
    "wall": (0, 0, 0),
    "empty": (255, 255, 255),
    "frontier": (255, 255, 0),
    "explored": (0, 0, 200),
    "path": (0, 255, 0)
}

def move_cost(from_pos, to_pos):
    dr = abs(from_pos[0] - to_pos[0])
    dc = abs(from_pos[1] - to_pos[1])
    if dr == 1 and dc == 1:
        return math.sqrt(2)
    return 1
