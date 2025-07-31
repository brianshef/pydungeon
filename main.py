#!/usr/bin/env python
import tcod

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler

# Constants for the game
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
TITLE = "PyDungeon by Brian Shef"
TILESHEET_FILE = "./assets/dejavu10x10_gs_tc.png"


def main() -> None:
    tileset = tcod.tileset.load_tilesheet(
        TILESHEET_FILE, 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), "@", (255, 255, 255))
    npc = Entity(int(SCREEN_WIDTH / 2 - 5), int(SCREEN_HEIGHT / 2), "@", (255, 255, 0))
    entities = {npc, player}

    with tcod.context.new(
        columns=SCREEN_WIDTH,
        rows=SCREEN_HEIGHT,
        tileset=tileset,
        title=TITLE,
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
        while True:
            root_console.print(x=player.x, y=player.y, text=player.char, fg=player.color)

            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():

                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):                    
                    player.move(dx=action.dx, dy=action.dy)

                elif isinstance(action, EscapeAction):
                    print("Escape action triggered, exiting...")
                    raise SystemExit()

if __name__ == "__main__":
    main()
