from dataclasses import dataclass
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

@dataclass
class initScreenData:
    console: rich.Console 
    effect: terminaltexteffects.effects.effect_laseretch.LaserEtch
    ptk_style: Style.from_dict
    api_endpoint: str
    persona: str
    session: prompt_toolkit.PromptSession


    
