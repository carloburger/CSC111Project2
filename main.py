import pygame

from maze_dataset import MazeDataset, MazeDatasetConfig
from maze_dataset.generation import LatticeMazeGenerators
cfg: MazeDatasetConfig = MazeDatasetConfig(
	name="FirstMaze", # name is only for you to keep track of things
	grid_n=10, # number of rows/columns in the lattice
	n_mazes=10, # number of mazes to generate
	maze_ctor=LatticeMazeGenerators.gen_dfs, # algorithm to generate the maze
    maze_ctor_kwargs=dict(do_forks=True), # additional parameters to pass to the maze generation algorithm
)
dataset = MazeDataset.from_config(cfg)

m = dataset[0]


maze = LatticeMazeGenerators.gen_dfs(grid_shape=(2, 2))
print(maze.as_ascii())

