"""
Try to understand what you just wrote and add colors
"""

"""
▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █  █
 █  █▀█ █▀▄ █ █  █  █ █  █
 ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀  ▀
    tarotui is a terminal-based tarot reading experience done in urwid and in python
    main component for the layout
"""

import urwid

from dataclasses import dataclass, field
from urwid import Button, LineBox, Filler, Pile, Text, Edit, MainLoop, Padding
from typing import List, Dict, Union, Tuple, Any, ClassVar
from utils.Colors import ColorInit
from utils.StaticMethods import runLoop, applyPalette 

import sys
import subprocess
import ollama

class RoundBox(LineBox):
    def __init__(self,widget: Any, title: str, title_align: str, borders: Dict[str]) -> None:
        super().__init__(
                widget,
                title=title,
                title_align=title_align,
                **borders
            )

@dataclass
class necessaryData(ColorInit):
    headerTitle: str = """
▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █  █
 █  █▀█ █▀▄ █ █  █  █ █  █
 ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀  ▀
"""
    inputWidth: int = 55
    inputTitle: str = "Ask the fates"
    borderCorner: Dict[str] = field(default_factory=lambda: {
            "tlcorner": '╭',
            "tline": '─',
            "bline": '─',
            "trcorner": '╮',
            "rline": '│',
            "lline": '│',
            "blcorner": '╰',
            "brcorner": '╯'
        })
    screen: urwid.raw_display.Screen = urwid.raw_display.Screen()

class widgetInit(necessaryData):
    def __init__(self) -> None:
        super().__init__()
        self.screen.set_terminal_properties(256)
        self.userInput: urwid.AttrMap = applyPalette(Padding(
                RoundBox(
                    Edit(caption=" > "),
                    self.inputTitle,
                    'left',
                    self.borderCorner
                ),
                width=self.inputWidth, align='center'
            ),"inputBorder")

        self.headerTitle: urwid.AttrMap = applyPalette(Text(self.headerTitle, align='center'),"header")
        self.pile: urwid.Pile = Pile(
            [
                (self.headerTitle),
                (self.userInput)
            ]
        )
        self.mainWidget: urwid.Filler = Filler(self.pile, valign='middle') 
        self.mainLoop: urwid.MainLoop = runLoop(self.mainWidget, self.palette, screen=self.screen)

