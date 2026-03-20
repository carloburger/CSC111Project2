from graph import Graph
from graph import _Vertex
import muutils.json_serialize.util as u
u._FORMAT_KEY = "__format__"
import sys
sys.modules['muutils.json_serialize.util']._FORMAT_KEY = "__format__"


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

def number_maze(maze: MazeDataset) -> Graph:
    """
    Convert a MazeDataset instance into a graph object where the vertices 
    contain numbers from 1 to n^2, where n is the number of rows/columns in the maze.
    """
    
    graph = Graph()
    adj_list = maze.as_adj_list()

    for connection in adj_list:
        coord1 = connection[0]
        coord2 = connection[1]

        v1 = coord1[0] * 10 + coord1[1]
        v2 = coord2[0] * 10 + coord2[1]

        graph.add_vertex(v1)
        graph.add_vertex(v2)

        graph.add_edge(v1, v2)
        
    return graph
