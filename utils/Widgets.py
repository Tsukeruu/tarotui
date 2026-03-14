"""
Try to understand what you just wrote
"""

from dataclasses import dataclass, field
from urwid import Button, LineBox, Filler, Pile, Text, Edit, MainLoop, Padding
from typing import List, Dict, Union, Tuple

import sys
import subprocess
import ollama

class RoundBox(LineBox):
    def __init__(self,widget: Any, title: str, title_align: str) -> None:
        super().__init__(
                widget,
                title=title,
                title_align=title_align,
                tlcorner='╭',
                tline='─',
                bline='─',
                trcorner='╮',
                rline='│',
                lline='│',
                blcorner='╰',
                brcorner='╯'
            )

@dataclass
class necessaryData:
    headerTitle: str = """
▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █  █
 █  █▀█ █▀▄ █ █  █  █ █  █
 ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀  ▀
"""
    inputWidth: int = 60
    inputTitle: str = "Ask the fates"
    
    @staticmethod
    def runLoop(mainWidget: urwid.Filler, palette: List[Tuple(str)] = None) -> urwid.MainLoop:
        mainLoop: urwid.MainLoop = MainLoop(mainWidget,palette=palette)
        mainLoop.run()
        return mainLoop

class widgetInit(necessaryData):
    def __init__(self) -> None:
        self.userInput: urwid.Padding = Padding(
                RoundBox(
                    Edit(caption=" > "),title=self.inputTitle,title_align='left', 
                    ),
                width=self.inputWidth, align='center'
            )

        self.headerTitle: urwid.Text = Text(self.headerTitle, align='center')
        self.pile: urwid.Pile = Pile(
            [
                (self.headerTitle),
                (self.userInput)
            ]
        )
        self.mainWidget: urwid.Filler = Filler(self.pile, valign='middle')
        self.mainLoop: urwid.MainLoop = self.runLoop(self.mainWidget)
