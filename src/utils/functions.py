from dataclasses import dataclass, field
from typing import Dict, List, Any, Tuple, ClassVar
from .dataclasses import initScreenData
from rich.panel import Panel
from rich.console import Console

from terminaltexteffects.utils.graphics import Color
from terminaltexteffects.effects.effect_laseretch import LaserEtch

from os import system
from shutil import get_terminal_size

from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML

"""
 ▀▄    ▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █ ▀█▀
  ▄▀    █  █▀█ █▀▄ █ █  █  █ █  █ 
 ▀      ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀ ▀▀▀
- This is the "functions"
- This provides the functions necessary for execution and executes from the dataclass
"""

class main(initScreenData):
    def __init__(self) -> None:
        super().__init__(
            console = Console(),
            effect = LaserEtch("""
 ▀▄    ▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █ ▀█▀
  ▄▀    █  █▀█ █▀▄ █ █  █  █ █  █ 
 ▀      ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀ ▀▀▀
        """),
            ptk_style = Style.from_dict(
                {
                  "prompt": "#b4befe",
                  "placeholder": "#585b70"
            }
        )
    ) 

    def clearScreen(self) -> None:
        system("clear")

    def effectSettings(self, effect: terminaltexteffects.effects.effect_laseretch.LaserEtch):
        effect.effect_config.etch_speed: int = 1
        effect.effect_config.final_gradient_stops: Tuple[Color[str]] = (Color("#89b4fa"), Color("#cba6f7"))
    def drawAscii(self) -> None:
        with self.effect.terminal_output() as output:
            self.effectSettings(self.effect)
            for frame in self.effect: #Iteration for classes is achievable through a special method called iter, the rest is handled through terminal text effects
                output.print(frame)
         
    def userPrompt(self, style: Style.from_dict) -> Union[str, int]:
        userQuestion: Union[str, int] = prompt(
                HTML("<b><prompt> > </prompt></b>"),
                placeholder=HTML("<placeholder>Ask the fates...</placeholder>"),
                style=style 
            )
        return userQuestion
    
    def processQuestion(self, question: Union[str, int]) -> None:
        #Process user's question here 
        pass

    def renderPanel(self) -> rich.panel.Panel:
        mainPanel: rich.panel.Panel = Panel("""
[#cba6f7 b]Tarotui[/#cba6f7 b] is a tarot reading [#a6e3a1 b]TUI[/#a6e3a1 b] for the terminal
1. Be [#f9e2af b]straightforward[/#f9e2af b] with your question
2. Questions are answered through [#a6e3a1 b]ollama[/#a6e3a1 b]
3. [#74c7ec b]Enjoy![/#74c7ec b]
""".strip(), expand = False, title = "[b]About[/b]", title_align = "left", border_style = "#b4befe")
        return mainPanel

    def finalizePanel(self, width: int) -> None:
        self.console.print(self.renderPanel())
        self.console.print("[#585b70]─[/#585b70]" * width)

    def execute(self) -> None:
        orders: List[Callable[None,[None]]] = [
            lambda: self.clearScreen(),
            lambda: self.drawAscii(),
            lambda: self.finalizePanel(get_terminal_size().columns), 
            lambda: self.processQuestion(self.userPrompt(self.ptk_style))
        ]
        for execution in orders:
            execution()
