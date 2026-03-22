from player import Player
from graph import Graph
from typing import Any
from typing import Any

class BFSPlayer(Player):
    """A player that solves the maze using Breadth-First Search.
    
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
        """Solve the maze from start to end using BFS.
        Return the path taken, or an empty list if no path exists.
        """
        path = self._graph.get_path_bfs(start, end)
        for position in path:
            self.move(position)
        return self._path

    def get_path_bfs(self, start: Any, end: Any) -> list:
        """Return the shortest path from start to end using BFS, or an empty list if none exists.
        """
        if start not in self._graph._vertices or end not in self._graph._vertices:
            return []
        
        queue = [[start]]
        visited = {start}
        
        while queue:
            path = queue.pop(0)
            current = path[-1]
            self._num_moves += 1
            
            if current == end:
                return path
            
            for neighbour in self._graph_.get_neighbours(current):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(path + [neighbour])
        
        return []