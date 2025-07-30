class Action:
    """Base class for all actions."""
    pass


class EscapeAction(Action):
    """Intent to exit the game or current state."""
    pass


class MovementAction(Action):
    """Intent to move in a direction."""
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy