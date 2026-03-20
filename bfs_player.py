from player import Player
from graph import Graph

class DFSPlayer(Player):
    """A player that solves the maze using Depth-First Search.
    
    Instance Attributes:
        - _graph: the graph representation of the maze
        
    Representation Invariants:
        - self._graph is not None
    """
    _graph: Graph
    
    def __init__(self, graph: Graph) -> None:
        self._num_moves = 0
        self._path = []
        self._graph = graph
    
    def solve(self, start: int, end: int) -> list[int]:
        """Solve the maze from start to end using DFS.
        Return the path taken, or an empty list if no path exists.
        """
        path = self._graph.get_path_dfs(start, end)
        for position in path:
            self.move(position)
        return self._path