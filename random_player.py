from player import Player
from graph import Graph
from typing import Any
import random

class Random_Player(Player):
    """A player that solves the maze by randomly choosing a direction to move in.
    
    This player does not use any strategy and may take a long time to solve the maze.
    
    Instance attributes:
        - _graph: the graph representation of the maze
    """
    _graph: Graph
    
    def __init__(self, graph: Graph) -> None:
        self._num_moves = 0
        self._path = []
        self._graph = graph
    
    def solve(self, start: int, end: int) -> list[int]:
        """Solve the maze from start to end by randomly choosing a direction to move in.
        Return the path taken.
        
        Preconditions:
        - start in self._graph._vertices
        - end in self._graph._vertices
        """
        
        while self.get_current_position() != end:
            current = self.get_current_position()
            neighbours = self._graph.get_neighbours(current)
            valid_choices = {n for n in neighbours if n != 0}
            choice = random.choice(valid_choices)
            self.move(choice)
        return []