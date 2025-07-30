#!/usr/bin/env python3
import tcod


def main():
    print("PyDungeon by Brian Shef")


if __name__ == "__main__":
    tcod.console_init_root(80, 50, "PyDungeon by Brian Shef", False)
    main()
    tcod.console_flush()
    tcod.console_wait_for_keypress(True)
