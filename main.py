#!/usr/bin/env python
import tcod

TITLE = "PyDungeon by Brian Shef"
TILESHEET_FILE = "./assets/dejavu10x10_gs_tc.png"


def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        TILESHEET_FILE, 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    with tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title=TITLE,
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=1, y=1, string="@")

            context.present(root_console)

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()



if __name__ == "__main__":
    main()
