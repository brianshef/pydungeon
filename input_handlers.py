from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction

MOVE_KEYS = {  # key_symbol: (x, y)
        # Arrow keys.
        tcod.event.KeySym.LEFT: (-1, 0),
        tcod.event.KeySym.RIGHT: (1, 0),
        tcod.event.KeySym.UP: (0, -1),
        tcod.event.KeySym.DOWN: (0, 1),
        tcod.event.KeySym.HOME: (-1, -1),
        tcod.event.KeySym.END: (-1, 1),
        tcod.event.KeySym.PAGEUP: (1, -1),
        tcod.event.KeySym.PAGEDOWN: (1, 1),
        tcod.event.KeySym.PERIOD: (0, 0),
        # Numpad keys.
        tcod.event.KeySym.KP_1: (-1, 1),
        tcod.event.KeySym.KP_2: (0, 1),
        tcod.event.KeySym.KP_3: (1, 1),
        tcod.event.KeySym.KP_4: (-1, 0),
        tcod.event.KeySym.KP_5: (0, 0),
        tcod.event.KeySym.KP_6: (1, 0),
        tcod.event.KeySym.KP_7: (-1, -1),
        tcod.event.KeySym.KP_8: (0, -1),
        tcod.event.KeySym.KP_9: (1, -1),
        tcod.event.KeySym.CLEAR: (0, 0),  # Numpad `clear` key
    }


class EventHandler(tcod.event.EventDispatch[Action]):
        def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
            """The window close button was clicked or Alt+F$ was pressed."""
            print(event)
            self.cmd_quit()

        def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
            """A key was pressed."""
            # print(event)
            if event.sym in MOVE_KEYS:
                # Send movement keys to the cmd_move method with parameters.
                return self.cmd_move(*MOVE_KEYS[event.sym])
            elif event.sym == tcod.event.KeySym.ESCAPE:
                return self.cmd_escape()

        def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[Action]:
            """The window was clicked."""
            # print(event)
            return None

        def ev_mousemotion(self, event: tcod.event.MouseMotion) -> Optional[Action]:
            """The mouse has moved within the window."""
            # print(event)
            return None

        def cmd_move(self, x: int, y: int) -> Optional[Action]:
            """Intent to move: `x` and `y` is the direction, both may be 0."""
            # print("Command move: " + str((x, y)))
            return MovementAction(x, y)

        def cmd_escape(self) -> Optional[Action]:
            """Intent to exit this state."""
            # print("Command escape.")
            return EscapeAction()

        def cmd_quit(self) -> Optional[Action]:
            """Intent to exit the game."""
            # print("Command quit.")
            raise SystemExit()

        def dispatch(self, event) -> Optional[Action]:
            if event.type == tcod.event.KeyDown:
                return self.ev_keydown(event)
            elif event.type == tcod.event.Quit:
                return self.cmd_quit()
            elif event.type == tcod.event.MouseButtonDown:
                return self.ev_mousebuttondown(event)
            elif event.type == tcod.event.MouseMotion:
                return self.ev_mousemotion(event)
            # Delegate unhandled events to the superclass.
            return super().dispatch(event)