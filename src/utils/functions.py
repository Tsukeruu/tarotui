from dataclasses import dataclass, field
from .dataclasses import initScreenData
from typing import Dict, List, Any, Tuple, ClassVar

from rich.panel import Panel
from rich.console import Console
from rich.live import Live

from terminaltexteffects.utils.graphics import Color
from terminaltexteffects.effects.effect_laseretch import LaserEtch

from os import system
from shutil import get_terminal_size
from sys import stdout
from time import sleep

from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML

import requests

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
            ),
            api_endpoint = "http://localhost:11434/api/generate",
            persona = """
            You are a tarot card reader.
            You are giving a three-card tarot reading (Past, Present, Future spread), Give a rich, intuitive reading that weaves the three cards into a cohesive narrative.
            if the question is merely a number or a jumble of words or letters, stop the persona, respond in 10 words or less and tell the user Please give a comprehensive question for a specific response,
            keep in mind, do not ask for a review by saying in first person "how did i resonate with your reading", keep the reading straightforward, the question is: 
            """.strip()
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

    def typeWrite(self, paragraph: str, delay: int) -> None:
        initString: str = ""
        #Vertical overflow is a dynamic arguement that calculates terminal height and decided what to do when the content being updated exceeds terminal height or is not showing, setting visible ensures the terminal scrolls with the content, by default when content exceeds terminal height, an ellipsis is shown indicating more is to be shown but does not usually update
        with Live(initString, console=self.console, refresh_per_second=20, vertical_overflow="visible") as animation:
            for char in paragraph:
                initString += char
                animation.update(initString)
                sleep(delay)
        #Why did we not use our classic forloop with console.print? 
        #There is no mere support for that as console.print expects correct markdown opening and closing tags, in our code, we defined the paragraph with opening and closing tags, however console.print printed each character and expected each to have an opening and closing tag, not as a whole, by using live which has direct rich support, we use live.update(animation_object) to redraw it everytime, this way it re reads the tags and renders them as a whole paragraph
        #To understand rich Live effectively, the animationobject passed into the context manager is the starting point, then over time we add on characters through our forloop through arithmetic operations such as +=, and we update it by telling rich to redraw it, we use animation.update by notifying rich that it has changed, it handles the rest from there, by clearing it and adding on characters, then uses console.print with the finished full read of markdown and tags to parse bold characters effectively
    def userPrompt(self, style: Style.from_dict) -> Union[str, int]:
        userQuestion: Union[str, int] = prompt(
                HTML("<b><prompt> > </prompt></b>"),
                placeholder=HTML("<placeholder>Ask the fates...</placeholder>"),
                style=style 
            )
        return userQuestion

    def spinner(self, question: str) -> str: 
        with self.console.status("[#a6e3a1 b]Performing HTTP POST request to ollama[/#a6e3a1 b]",spinner="line") as status: 
            payload: Dict[str, Union[str, bool]] = {
                "model": "llama3.2",
                "prompt": self.persona + question,
                "stream": False
            }
            json_response = requests.post(self.api_endpoint, json=payload)
            json_response = json_response.json()
            self.console.print("[#50fa7b b][✓] Performed post request successfuly![/#50fa7b b]")
            status.update("[#a6e3a1 b]Finishing up...[/#a6e3a1 b]")
            sleep(1.5)  
            return "[b]" + json_response["response"] + "[/b]"

    def processQuestion(self, question: Union[str, int]) -> None:
        #Process user's question here 
        try:
            ollama_response: str = self.spinner(question)
        except requests.exceptions.RequestException:
            self.console.print("[#f38ba8 b][ㄨ] A severe post request error has occured![/#f38ba8 b]") 
            self.console.print_exception(show_locals=True)
            return
        self.clearScreen() 
        self.typeWrite(ollama_response, 0.01)
        #Next stop, add autocompletion from history using ptk, and add custom errors and "click any key to continue" at the end of the type write

    def renderPanel(self) -> rich.panel.Panel:
        mainPanel: rich.panel.Panel = Panel("""
[#cba6f7 b]Tarotui[/#cba6f7 b]: Terminal Tarot
1. Ask [#cba6f7 b]straightforward[/#cba6f7 b] questions.
2. Powered by [#cba6f7 b]ollama[/#cba6f7 b] (intelligence may be limited).
3. Responses might misinterpret or be inaccurate.
4. [#cba6f7 b]Enjoy![/#cba6f7 b]
    """.strip(), expand = False, title = "[b]About[/b]", title_align = "left", border_style = "#b4befe")
        return mainPanel

    def finalizePanel(self, width: int) -> None:
        self.console.print(self.renderPanel())
        self.console.print("[#585b70]─[/#585b70]" * width)
        #By multiplying dashes to the terminal columns / width, we ensure they fill the correct width of the terminal

    def execute(self) -> None:
        orders: List[Callable[None,[None]]] = [
            lambda: self.clearScreen(),
            lambda: self.drawAscii(),
            lambda: self.finalizePanel(get_terminal_size().columns), 
            lambda: self.processQuestion(self.userPrompt(self.ptk_style))
        ]
        for execution in orders:
            execution()
