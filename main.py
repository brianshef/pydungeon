#!/usr/bin/env python
import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

# Constants for the game
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
TITLE = "PyDungeon by Brian Shef"
TILESHEET_FILE = "./assets/dejavu10x10_gs_tc.png"


def main() -> None:
    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(
        TILESHEET_FILE, 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), "@", (255, 255, 255))
    npc = Entity(int(SCREEN_WIDTH / 2 - 5), int(SCREEN_HEIGHT / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new(
        columns=SCREEN_WIDTH,
        rows=SCREEN_HEIGHT,
        tileset=tileset,
        title=TITLE,
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            root_console.clear()

            engine.handle_events(events)

if __name__ == "__main__":
    main()
