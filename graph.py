from typing import Any
from __future__ import annotations

class _Vertex:
    """A vertex in a graph.
    
    Instance Attributes:
        - item: The item stored in this vertex
        - neighbours: A set of the vertices adjacent to this vertex
        
    Representation Invariants:
        - item is not None
        - self not in self.neighbours
        - all(v not in self.neighbours for v in self.neighbours)
    """
    
    _item: Any
    _neighbours: set[_Vertex]
    
    def __init__(self, item: Any, neighbours: set[_Vertex]) -> None:
        self.item = item
        self.neighbours = neighbours

    def adjacent_vertices(self):
        """Return the set of adjacent vertices."""
        return self.neighbours
    
    def get_item(self) -> Any:
        """Return the item stored in this vertex."""
        return self.item
    
    def check_connected(self, target_item: Any, visited: set[_Vertex]) -> bool:
        """Return whether this vertex is connected to a vertex corresponding to the target_item,
        WITHOUT using any of the vertices in visited.

        Preconditions:
            - self not in visited
        """
        if self.item == target_item:
            return True
        else:
            visited.add(self)
            for neighbor in self.neighbours:
                if neighbor not in visited:
                    if neighbor.check_connected(target_item, visited):
                        return True
            return False
        
    def add_neighbour(self, vertex: _Vertex) -> None:
        """Add the given vertex to self.neighbours."""
        self.neighbours.add(vertex)
     
class Graph:
    """A graph data structure.
    
    Instance Attributes:
        - vertices: A set of the vertices in this graph.
        - edges: A set of the edges in this graph. Each edge is represented as a
            tuple of two vertices (u, v) where u and v are in vertices.
            
    Representation Invariants:
        - all(item == self._vertices[item].item for item in self._vertices)

    """

    _vertices: dict[Any, _Vertex]
    
    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def add_vertex(self, item: Any) -> None:
        """Add a vertex with the given item to this graph.

        The new vertex is not adjacent to any other vertices.
        
        If a vertex with the given item already exists in this graph, raise ValueError.
        """
        if item in self._vertices:
            raise ValueError
        self._vertices[item] = _Vertex(item, set())


    def add_edge(self, item1: Any, item2: Any) -> None:
        """Add an edge between the two vertices with the given items in this graph.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]
            v1.neighbors.add(v2)
            v2.neighbors.add(v1)
        else:
            raise ValueError

    def connected(self, item1: Any, item2: Any) -> bool:
        """Return whether item1 and item2 are connected vertices in this graph.

        Return False if item1 or item2 do not appear as vertices in this graph.

        >>> g = Graph()
        >>> g.add_vertex(1)
        >>> g.add_vertex(2)
        >>> g.add_vertex(3)
        >>> g.add_vertex(4)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 3)
        >>> g.connected(1, 3)
        True
        >>> g.connected(1, 4)
        False
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]
            if v1.check_connected(v2, set()):
                return True
        return False

    def get_connected_component(self, item: Any) -> set:
        """Return a set of all ITEMS connected to the given item in this graph.

        Raise a ValueError if item does not appear as a vertex in this graph.

        >>> g = Graph()
        >>> for i in range(0, 5):
        ...     g.add_vertex(i)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(1, 3)
        >>> g.add_edge(2, 3)
        >>> g.get_connected_component(0) == {0, 1, 2, 3}
        True

        Note: we've implemented this method for you, and you should not change it.
        Instead, your task is to implement _Vertex.get_connected_component below.
        """
        if item not in self._vertices:
            raise ValueError(f"Vertex {item} is not in this graph")
        else:
            return self._vertices[item].get_connected_component(set())       