# GOOD PERFORMANCE TIME APP

## Overview

This project is a modular, production-quality AI Pathfinder Visualization System built with Pygame. It visualizes six uninformed search algorithms on a 2D grid, animating their step-by-step progress, and displays performance metrics in real time.

## Features

- 20x20 adjustable grid with static walls
- Six search algorithms: BFS, DFS, UCS, DLS, IDDFS, Bidirectional Search
- Strict movement order (Up, Right, Down, Left, Bottom-Right, Top-Left)
- Animated search and path reconstruction
- Real-time display of nodes expanded, path length, and execution time
- Keyboard controls for algorithm selection, reset, and exit
- Optional: Place/remove walls with mouse

## Installation

1. Install Python 3.7+.
2. Install Pygame:
   ```
   pip install pygame
   ```

## How to Run

1. Navigate to the project directory:
   ```
   cd AI_A1_23F_0864
   ```
2. Run the application:
   ```
   python main.py
   ```

## Controls

- `1` - BFS
- `2` - DFS
- `3` - UCS
- `4` - DLS (Depth-Limited Search)
- `5` - IDDFS (Iterative Deepening DFS)
- `6` - Bidirectional Search
- `R` - Reset grid
- `Q` - Quit
- `UP/DOWN` - Increase/decrease depth limit (for DLS/IDDFS)
- `SPACE` - Run selected algorithm
- Mouse click - Place/remove wall

## Algorithms

### BFS (Breadth-First Search)
Expands nodes in order of increasing distance from the start. Guarantees shortest path in terms of steps.

### DFS (Depth-First Search)
Expands as far as possible along each branch before backtracking. Not optimal or complete in infinite spaces.

### UCS (Uniform Cost Search)
Expands the node with the lowest cumulative cost. Straight moves cost 1, diagonals cost √2. Guarantees optimality.

### DLS (Depth-Limited Search)
DFS with a maximum depth limit. Does not expand nodes beyond the limit.

### IDDFS (Iterative Deepening DFS)
Repeatedly applies DLS with increasing depth limits until a solution is found. Combines DFS space efficiency with BFS completeness.

### Bidirectional Search
Runs two BFS searches from start and target, meeting in the middle for efficiency.

## Movement Rules

Movement is allowed in the following strict order:

1. Up → (-1, 0)
2. Right → (0, 1)
3. Down → (1, 0)
4. Left → (0, -1)
5. Bottom-Right → (1, 1)
6. Top-Left → (-1, -1)

No other diagonals or movement orders are permitted.

## Notes

- All algorithms animate their progress step-by-step.
- No dynamic obstacles are allowed.
- The code is modular and PEP8 compliant.

---
