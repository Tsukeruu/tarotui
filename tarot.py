#!/usr/bin/python
"""
▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █  █
 █  █▀█ █▀▄ █ █  █  █ █  █
 ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀  ▀
    tarotui is a terminal-based tarot reading experience done in urwid and in python
    tarot.py is equivalent to the "main" in python
"""

from utils.Exceptions import *
from utils.Dataclasses import *
from utils.Cards import *
from utils.Placements import *

from typing import Dict, List
from urwid import Button, LineBox, Filler, Pile

import random
import ollama

class Main():
    def __init__(self) -> None:
        pass
