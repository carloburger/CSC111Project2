from __future__ import annotations
from typing import Any

    
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

    def degree(self) -> int:
        """Returns the number of neighbours that this vertex has."""
        return len(self.neighbours)

    def get_path(self, target_item: Any, visited: set[_Vertex]) -> list:
        """Return a path from this vertex to the vertex corresponding to target_item,
        WITHOUT using any of the vertices in visited. Returns an empty list if no path exists.

        Preconditions:
            - self not in visited
        """
        if self.item == target_item:
            return [self.item]
        else:
            visited.add(self)
            for neighbor in self.neighbours:
                if neighbor not in visited:
                    path = neighbor.get_path(target_item, visited)
                    if path:
                        return [self.item] + path
            return []
        
    def get_neighbours(self) -> set:
        """Return the set of items adjacent to this vertex."""
        return {v.item for v in self.neighbours}

    # def get_connected_component(self, visited: set[_Vertex]) -> set:
    #     """Return a set of all ITEMS connected to self by a path that does not use
    #     any vertices in visited.

    #     The items of the vertices in visited CANNOT appear in the returned set.

    #     Preconditions:
    #         - self not in visited

    #     Implementation notes:
    #         1. This can be implemented in a similar way to _Vertex.check_connected.
    #         2. This method must be recursive, and will have an implicit base case:
    #            when all vertices in self.neighbours are already in visited.
    #         3. Use a loop accumulator to store a set of the vertices connected to self.
    #     """
    #     visited.add(self)
    #     connected_items = {self.item}
    #     for neighbor in self.neighbours:
    #         if neighbor not in visited:
    #             neighbor_items = neighbor.get_connected_component(visited)
    #             for item in neighbor_items:
    #                 connected_items.add(item)
    #     return connected_items


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
        if item not in self._vertices:
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
            v1.neighbours.add(v2)
            v2.neighbours.add(v1)
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
            if v1.check_connected(v2.item, set()):
                return True
        return False
    
    def get_path(self, item1: Any, item2: Any) -> list:
        """Return a path between item1 and item2, or an empty list if none exists."""
        if item1 in self._vertices and item2 in self._vertices:
            return self._vertices[item1].get_path(item2, set())
        return []
    
    def is_vertex(self, item: Any) -> bool:
        """Return whether the given item exists as a vertex in this graph.
        
        >>> g = Graph()
        >>> g.add_vertex(1)
        >>> g.is_vertex(1)
        True
        >>> g.is_vertex(2)
        False
        """
        return item in self._vertices
    
    def get_neighbours(self, item: Any) -> set:
        """Return the set of items adjacent to the given item in this graph.
        
        Raise a ValueError if item does not appear as a vertex in this graph.
        
        >>> g = Graph()
        >>> g.add_vertex(1)
        >>> g.add_vertex(2)
        >>> g.add_vertex(3)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(1, 3)
        >>> g.get_neighbours(1) == {2, 3}
        True
        """
        if item not in self._vertices:
            raise ValueError
        return {v.item for v in self._vertices[item].neighbours}
    
    def get_all_vertices(self) -> dict[Any, _Vertex]:
        """Returns all vertices in the graph."""
        return self._vertices
    
    def remove_vertex(self, item: Any) -> None:
        if item not in self._vertices:
            raise ValueError
        vertex = self._vertices[item]
        for neighbour in vertex.neighbours:
            if vertex not in neighbour.neighbours:
                raise ValueError
            neighbour.neighbours.remove(vertex)
        self._vertices.pop(item)

    # def get_connected_component(self, item: Any) -> set:
    #     """Return a set of all ITEMS connected to the given item in this graph.

    #     Raise a ValueError if item does not appear as a vertex in this graph.

    #     >>> g = Graph()
    #     >>> for i in range(0, 5):
    #     ...     g.add_vertex(i)
    #     >>> g.add_edge(0, 1)
    #     >>> g.add_edge(1, 2)
    #     >>> g.add_edge(1, 3)
    #     >>> g.add_edge(2, 3)
    #     >>> g.get_connected_component(0) == {0, 1, 2, 3}
    #     True

    #     Note: we've implemented this method for you, and you should not change it.
    #     Instead, your task is to implement _Vertex.get_connected_component below.
    #     """
    #     if item not in self._vertices:
    #         raise ValueError(f"Vertex {item} is not in this graph")
    #     else:
    #         return self._vertices[item].get_connected_component(set())


if __name__ == '__main__':

    import doctest
    doctest.testmod()

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['annotations'],
        'allowed-io': [],
        'max-line-length': 120,
        'max-nested-blocks': 4
    })
 