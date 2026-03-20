import muutils.json_serialize.util as u

with open(u.__file__, "a") as f:
    f.write('\n_FORMAT_KEY = "__format__"\n')


from maze_dataset import MazeDataset, MazeDatasetConfig
from maze_dataset.generation import LatticeMazeGenerators
from maze_dataset.maze import SolvedMaze


def generate_mazes(n: int = 10) -> MazeDataset:
    """
    Generate a Maze using the maze-datasets Github repository.
    """
    cfg: MazeDatasetConfig = MazeDatasetConfig(
        name="FirstMaze", # name is only for you to keep track of things
        grid_n=10, # number of rows/columns in the lattice
        n_mazes=10, # number of mazes to generate
        maze_ctor=LatticeMazeGenerators.gen_dfs, # algorithm to generate the maze
        maze_ctor_kwargs=dict(do_forks=True), # additional parameters to pass to the maze generation algorithm
    )

    dataset = MazeDataset.from_config(cfg)

    return dataset



