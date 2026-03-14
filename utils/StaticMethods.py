"""
▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █  █
 █  █▀█ █▀▄ █ █  █  █ █  █
 ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀  ▀
    tarotui is a terminal-based tarot reading experience done in urwid and in python
    this will hold static methods
"""

from urwid import MainLoop, Filler, AttrMap
from typing import List, Tuple

@staticmethod
def runLoop(
    mainWidget: urwid.Filler, palette: List[Tuple[str]] = None, screen: Any = None) -> urwid.MainLoop:
    mainLoop: urwid.MainLoop = MainLoop(mainWidget, palette=palette, screen=screen)
    mainLoop.run()
    return mainLoop


@staticmethod
def applyPalette(widget: Any, paletteComponent: str) -> Any:
    return AttrMap(widget, paletteComponent)
