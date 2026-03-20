import pygame
from maze_generation import generate_mazes, number_maze, number_maze

maze = generate_mazes(10)

g = number_maze(maze[0])
print(maze[0].as_ascii())
for vertex_id, vertex in g.get_all_vertices().items():
    print(vertex_id)
    print("Value: ", vertex.get_item())
    print("#############################")
    print("Neighbors: ", )
    for neighbour in vertex.get_neighbours():
        print(neighbour)


pygame.init()
