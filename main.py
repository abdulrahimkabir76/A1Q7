# main.py
import pygame
import sys
import time

from grid import Grid
from gui import GUI
from node import Node

from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.ucs import ucs
from algorithms.dls import dls
from algorithms.iddfs import iddfs
from algorithms.bidirectional import bidirectional


ALGO_KEYS = {
    pygame.K_1: ("BFS", bfs),
    pygame.K_2: ("DFS", dfs),
    pygame.K_3: ("UCS", ucs),
    pygame.K_4: ("DLS", dls),
    pygame.K_5: ("IDDFS", iddfs),
    pygame.K_6: ("BIDIR", bidirectional)
}

def main():
    grid = Grid()
    gui = GUI(grid)
    running = True
    algo_name = "BFS"
    algo_func = bfs
    depth_limit = 10  # For DLS/IDDFS

    while running:
        gui.set_info(f"1:BFS 2:DFS 3:UCS 4:DLS 5:IDDFS 6:BIDIR | R:Reset | Q:Quit | Mouse:Toggle Wall")
        gui.draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key in ALGO_KEYS:
                    algo_name, algo_func = ALGO_KEYS[event.key]
                elif event.key == pygame.K_r:
                    grid.reset()
                elif event.key == pygame.K_q:
                    running = False
                    break
                elif event.key == pygame.K_UP:
                    depth_limit += 1
                elif event.key == pygame.K_DOWN:
                    depth_limit = max(1, depth_limit - 1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                from gui import CELL_SIZE, MARGIN
                col = (x - MARGIN) // (CELL_SIZE + MARGIN)
                row = (y - MARGIN) // (CELL_SIZE + MARGIN)
                if 0 <= row < grid.rows and 0 <= col < grid.cols:
                    if grid.is_wall(row, col):
                        grid.remove_wall(row, col)
                    elif (row, col) != grid.start and (row, col) != grid.target:
                        grid.set_wall(row, col)

        # Run algorithm on SPACE
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            start = Node(*grid.start)
            target = Node(*grid.target)
            gui.set_info(f"Running {algo_name}...")
            gui.draw_grid()
            pygame.display.update()
            time.sleep(0.2)
            t0 = time.time()
            if algo_name == "DLS":
                path, expanded, explored, frontier = algo_func(grid, start, target, gui, depth_limit)
            elif algo_name == "IDDFS":
                path, expanded, explored, frontier = algo_func(grid, start, target, gui, max_depth=depth_limit)
            else:
                path, expanded, explored, frontier = algo_func(grid, start, target, gui)
            t1 = time.time()
            gui.set_metrics(expanded, len(path) if path else 0, t1 - t0)
            gui.draw_grid(frontier, explored, set())
            pygame.display.update()
            if path:
                gui.animate_path(path, frontier, explored)
            else:
                gui.set_info("No path found.")
                gui.draw_grid(frontier, explored, set())
                pygame.display.update()
            time.sleep(0.5)
        pygame.time.delay(60)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()