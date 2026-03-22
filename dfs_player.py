from player import Player
from graph import Graph
from typing import Any

class DFSPlayer(Player):
    """A player that solves the maze using Depth-First Search.

    Instance Attributes:
        - _graph: the graph representation of the maze

    Representation Invariants:
        - self._graph is not None
    """
    _graph: Graph

    def __init__(self, graph: Graph) -> None:
        super().__init__()
        self._num_moves = 0
        self._path = []
        self._graph = graph

    def solve(self, start: int, end: int) -> list[int]:
        """Solve the maze from start to end using DFS.
        Return the path taken, or an empty list if no path exists.
        """
        path = self.get_path_dfs(start, end)
        for position in path:
            self.move(position)
        return self._path

    def get_path_dfs(self, start: Any, end: Any) -> list:
        """Return the shortest path from start to end using DFS, or an empty list if none exists.
        """
        if start not in self._graph.get_all_vertices() or end not in self._graph.get_all_vertices():
            return []
        return self._graph.get_all_vertices()[start].get_path(end, set())
