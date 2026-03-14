#!/usr/bin/python
"""
▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █  █
 █  █▀█ █▀▄ █ █  █  █ █  █
 ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀  ▀
    tarotui is a terminal-based tarot reading experience done in urwid and in python
    tarot.py is equivalent to the "main" in python
    this will connect all of the utils!
"""

from utils.Exceptions import *
from utils.Cards import *
from utils.Placements import *
from utils.StaticMethods import *
from utils.Widgets import widgetInit 

from dataclasses import dataclass

from typing import Dict, List, Union
from urwid import Button, LineBox, Filler, Pile, Text

import random
import ollama
import sys
import subprocess

class App(widgetInit):
    def __init__(self) -> None:
       pass

    def executeProgram(self) -> None:
       super().__init__()

main = App()
main.executeProgram()
