"""
▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █  █
 █  █▀█ █▀▄ █ █  █  █ █  █
 ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀  ▀
    tarotui is a terminal-based tarot reading experience done in urwid and in python
    color definitions and other color modifications go here
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Tuple, ClassVar
from urwid import AttrMap

@dataclass
class ColorInit:
    palette: ClassVar[List[Tuple]] = [
            ("header", "default", "default","default","#b4befe","default"),
            ("inputBorder","default", "default","default","#b4befe","default")
        ]
