from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Tuple, Any

from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession

import terminaltexteffects
import rich

"""
 ▀▄    ▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █ ▀█▀
  ▄▀    █  █▀█ █▀▄ █ █  █  █ █  █ 
 ▀      ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀ ▀▀▀
- This is the dataclass script
- This plays a crucial part in the hierachy by providing necessary data for order of execution
"""

#An ENUM typically used in regular classes (not dataclasses), is a way to explicity tell pyhon to use either of the choices, its like letting the user choose a choice, an enum allows for limited user options nad just by the given ones

class Arcana(Enum):
    MAJOR: str = "Major Arcana"
    MINOR: str = "Minor Arcana"

class Suit(Enum):
    WANDS: str = "Wands"
    CUPS: str = "Cups"
    SWORDS: str = "Swords"
    PENTACLES: str = "Pentacles"
    NONE: str = "None"


@dataclass()
class initScreenData:
    console: rich.Console 
    effect: terminaltexteffects.effects.effect_laseretch.LaserEtch
    ptk_style: Style.from_dict
    api_endpoint: str
    session: prompt_toolkit.PromptSession
    tiptext: str
    dialog: List[str]
    dialog_colors: List[str]
    file_directory: str
    situation: List[str]
    boxContent: str
    optionsConfirm: List[Tuple[str, str]]
    messageConfirm: str
    system: str
    availableSystems: List[str]


#In a card, being a major arcana means having suit set to NONE which is one of the awesome features of an enum, a minor arcana has a suit set to Suit[0:3], a major arcana has 22 cards whereas a minor arcana has 56 cards

@dataclass
class Card:
    name: str
    number: int
    arcana: Arcana
    suit: Suit
    keywords: List[str]
    meaning_upright: str
    meaning_reversed: str
    element: Optional[str] = None



