from graph import Graph
from graph import _Vertex
from typing import Any
from __future__ import annotations

class Maze(Graph):
    """A Maze is a graph where the vertices are locations in the maze and the edges are paths between those locations.

    The items stored in the vertices of this graph are (x, y) tuples representing coordinates in the maze.
    """
    