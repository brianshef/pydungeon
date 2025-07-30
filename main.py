#!/usr/bin/env python
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

# Constants for the game
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
TITLE = "PyDungeon by Brian Shef"
TILESHEET_FILE = "./assets/dejavu10x10_gs_tc.png"


def main() -> None:

    player_x = int(SCREEN_WIDTH / 2)
    player_y = int(SCREEN_HEIGHT / 2)

    tileset = tcod.tileset.load_tilesheet(
        TILESHEET_FILE, 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    with tcod.context.new(
        columns=SCREEN_WIDTH,
        rows=SCREEN_HEIGHT,
        tileset=tileset,
        title=TITLE,
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, text="@")

            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():

                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                    # Ensure the player stays within bounds
                    player_x = max(0, min(SCREEN_WIDTH - 1, player_x))
                    player_y = max(0, min(SCREEN_HEIGHT - 1, player_y))

                elif isinstance(action, EscapeAction):
                    print("Escape action triggered, exiting...")
                    raise SystemExit()

if __name__ == "__main__":
    main()
