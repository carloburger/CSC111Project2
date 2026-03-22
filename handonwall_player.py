from graph import Graph
from player import Player


class HandOnWallPlayer(Player):
    """
    A player solving the maze using the hand on wall approach.
    This player will always keep its hand on the left side.

    Instance attributes:
        -

    Representation Invariants:
        -

    """
    _graph: Graph

    def __init__(self) -> None:
        super().__init__()
        self._num_moves = 0
        self._path = []

    def walkthrough(self, start: int, finish: int) -> list:
        """Solve the maze from start to finish using the hand on the wall method (left hand).
        The path the player takes will be stored and returned at the end.
        """
        directions = [1, 10, -1, -10]
        current_location = start  # initial position ()
        current_direction = 0
        left_hand = 3
        stored_path = []
        vertices = self._graph.get_all_vertices()

        while current_location != finish:
            assert current_location in vertices

            if left_hand < 3:
                left_hand += 1
            else:
                left_hand = 0
            if current_location + directions[left_hand] in vertices[current_location].get_neighbours():
                stored_path.append(current_direction)
                current_location = current_location + directions[left_hand]
            else:
                if current_location + directions[current_direction] in vertices[current_location].get_neighbours():
                    stored_path.append(current_direction)
                    current_location = current_location + directions[current_direction]

                if current_direction < 3:
                    current_location += 1
                else:
                    current_location = 0

        return stored_path


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['Graph', 'Player'],
        'allowed-io': [],
        'max-line-length': 120,
        'max-nested-blocks': 4
    })
