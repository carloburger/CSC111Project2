class Player:
    """Parent class for the player character and bot algorithms.
    
    Instance Attributes:
    - _num_moves: the number of moves this player has made
    - _path: the paths this player has taken in chronological order
    
    Representation Invariants:
    - self.num_moves >= 0
    - self._path == [] or self._path[-1] is the current position
    
    """
    _num_moves: int
    _path: list[int]
    
    def __init__(self):
        self._num_moves = 0
        self._path = []
        
    def get_num_moves(self) -> int:
        """Return the number of moves this player has made."""
        return self._num_moves

    def get_path(self) -> list[int]:
        """Return the path this player has traversed in chronological order."""
        return self._path
    
    def move(self, position: int) -> None:
        """Move the player to the given position and update the path and move count."""
        self._path.append(position)
        self._num_moves += 1

    def get_current_position(self) -> int:
        """Return the current position of the player, or -1 if the player has not moved yet."""
        if self._path == []:
            return -1
        return self._path[-1]

    def reset(self) -> None:
        """Reset the player to their initial state."""
        self._num_moves = 0
        self._path = []