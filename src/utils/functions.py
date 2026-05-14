from dataclasses import dataclass, field
from .dataclasses import initScreenData, Card, Arcana, Suit
from .custom_errors import API_ERROR
from typing import Dict, List, Any, Tuple, ClassVar
from enum import Enum

from rich.panel import Panel
from rich.console import Console
from rich.live import Live

from terminaltexteffects.utils.graphics import Color
from terminaltexteffects.effects.effect_laseretch import LaserEtch

from os import system
from shutil import get_terminal_size
from sys import stdout
from time import sleep
from pathlib import Path
from random import choice, sample
from json import load

from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.shortcuts import choice

import requests
import random

"""
 ▀▄    ▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █ ▀█▀
  ▄▀    █  █▀█ █▀▄ █ █  █  █ █  █ 
 ▀      ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀ ▀▀▀
- This is the "functions"
- This provides the functions necessary for execution and executes from the dataclass
- In the future to maintain a light project, consider implementing get requests to a tarot api, examples include:
    - https://github.com/ekelen/tarot-api
- This results in deleting the json file keeping a light project overall
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
                  "placeholder": "#585b70",
                  "selected-option": "#b4befe bold",
                  "frame.border": "#89b4fa",
                  "blue": "#89b4fa"
                }
            ),
            api_endpoint = "http://localhost:11434/api/generate", 
            session = PromptSession(history=FileHistory(f"{Path(__file__).parent}/.tarotui_history")),
            tiptext="Press ctrl+c to quit!",
            dialog=["Polishing the crystal ball..", "Petting the black cat...", "Measuring if jupiter is in retrograde..."],
            dialog_colors=["#f5a97f", "#a6da95", "#c6a0f6"],
            file_directory=Path(__file__).parent,
            situation = ["The past", "The present", "The future"],
            boxContent = """
[#cba6f7 b]Tarotui[/#cba6f7 b]: Terminal Tarot
1. Ask [#cba6f7 b]straightforward[/#cba6f7 b] questions.
2. Powered by [#cba6f7 b]ollama[/#cba6f7 b] (intelligence may be limited).
3. Responses might misinterpret or be inaccurate.
4. [#cba6f7 b]Enjoy![/#cba6f7 b]
            """,
            optionsConfirm = [
                ("yes","Return to menu"),
                ("no", "I want to exit TAROTUI :( ")
            ],
            messageConfirm = "What would you like to do next?"
        ) 
    
    def return_deck(self, json_file: str) -> List[Card]:
        with open(json_file, 'r') as file:
            json_data: Dict[str, Union[str, int]] = load(file)

        deck = [
            Card(
                name=item["name"],
                number=item["number"],
                arcana=Arcana(item["arcana"]),
                suit=Suit(item["suit"]),
                keywords=item["keywords"],
                meaning_upright=item["meaning_upright"],
                meaning_reversed=item["meaning_reversed"],
                element=item["element"]
            )
            for item in json_data
        ]
        return deck

    def clearScreen(self) -> None:
        system("clear")

    def effectSettings(self, effect: terminaltexteffects.effects.effect_laseretch.LaserEtch):
        effect.effect_config.etch_speed: int = 1
        effect.effect_config.final_gradient_stops: Tuple[Color[str], Color[str]] = (Color("#89b4fa"), Color("#cba6f7"))

    def drawAscii(self, ascii_art: str) -> None:
        with self.effect.terminal_output() as output:
            self.effectSettings(ascii_art)
            for frame in ascii_art: #Iteration for classes is achievable through a special method called iter, the rest is handled through terminal text effects
                output.print(frame)

    def typeWrite(self, paragraph: str, delay: int) -> Union[bool, str]:
        initString: str = ""
        readingPanel: Panel = Panel(initString, title="[#89b4fa b]Reading[/#89b4fa b]", title_align="left", border_style="#89b4fa")
        #Vertical overflow is a dynamic arguement that calculates terminal height and decided what to do when the content being updated exceeds terminal height or is not showing, setting visible ensures the terminal scrolls with the content, by default when content exceeds terminal height, an ellipsis is shown indicating more is to be shown but does not usually update
        with Live(readingPanel, console=self.console, refresh_per_second=20, vertical_overflow="visible") as animation:
            for char in paragraph:
                initString += char
                animation.update(Panel(initString, title="[#89b4fa b]Reading[/#89b4fa b]", title_align="left", border_style="#89b4fa"))
                sleep(delay)
        userChoice: str = self.confirmChoice(self.optionsConfirm, self.messageConfirm)
        if userChoice == "no":
            return "exit"
        else:
            return False
        #Why did we not use our classic forloop with console.print? 
        #There is no mere support for that as console.print expects correct markdown opening and closing tags, in our code, we defined the paragraph with opening and closing tags, however console.print printed each character and expected each to have an opening and closing tag, not as a whole, by using live which has direct rich support, we use live.update(animation_object) to redraw it everytime, this way it re reads the tags and renders them as a whole paragraph
        #To understand rich Live effectively, the animationobject passed into the context manager is the starting point, then over time we add on characters through our forloop through arithmetic operations such as +=, and we update it by telling rich to redraw it, we use animation.update by notifying rich that it has changed, it handles the rest from there, by clearing it and adding on characters, then uses console.print with the finished full read of markdown and tags to parse bold characters effectively

    def userPrompt(self, style: Style.from_dict) -> Union[str, int]:
        userQuestion: Union[str, int] = self.session.prompt(
                HTML("<b><prompt>> </prompt></b>"),
                placeholder=HTML("<placeholder>Ask the fates...</placeholder>"),
                style=style,
                auto_suggest=AutoSuggestFromHistory()
            )
        return userQuestion
    
    def confirmChoice(self, optionList: List[Tuple[str, str]], message: str) -> str:
        confirmAnswer: str = choice(
                message=HTML(f"<b><blue>{message}</blue></b>"),
                options=optionList,
                default=optionList[0][0],
                style=self.ptk_style,
                show_frame=True
            )
        return confirmAnswer

    def response_spinner(self, question: str, shuffle: List[Tuple[str, Union[str, int, Suit, Arcana]]]) -> str:
        with self.console.status(f"[#a6e3a1 b]Performing an HTTP POST request to ollama[/#a6e3a1 b]",spinner="line") as status: 
            payload: Dict[str, Union[str, bool]] = {
                "model": "tarotui",
                "prompt": f"The question is {question} and the 3 cards are: {shuffle}",
                "stream": False
            }
            json_response = requests.post(self.api_endpoint, json=payload)
            json_response = json_response.json()
            self.console.print("[#f9e2af b][✓] Performed post request successfuly![/#f9e2af b]")
            status.update("[#a6e3a1 b]Finishing up...[/#a6e3a1 b]")
            sleep(1.5)  
            return f'[b]{json_response["response"]}[/b]'
            #Perhaps use .get() for when it says no such key as response (usually happens when model is not downloaded)    

    def shuffle_spinner(self, deck: List[Card]) -> List[Tuple[str, Union[str, int, bool, Arcana, Suit]]]: 
        with self.console.status("[#eed49f b]Shuffling the deck...[/#eed49f b]",spinner="line", spinner_style="bold #eed49f") as status:
            list_of_cards: List[Card] = sample(deck, 3)
            new_list_of_cards: List[Card] = []
            meanings: List[str] = []
            bool_meanings: List[bool] = []
            for card, situation in zip(list_of_cards, self.situation):
                reversed_meaning: bool = random.choice([True, False]) 
                if reversed_meaning:
                    meaning: str = card.meaning_reversed
                else:
                    meaning: str = card.meaning_upright
                new_list_of_cards.append(
                    (
                        situation,
                        card.name,
                        card.number,
                        card.arcana,
                        card.suit,
                        card.keywords,
                        meaning,
                        card.element,
                    )
                ) 
                meanings.append(meaning)
                bool_meanings.append(reversed_meaning)
            total_meanings: List[Tuple[bool, str]] = list(zip(bool_meanings,meanings))
            sleep(2)
            for message, color in zip(self.dialog, self.dialog_colors):
                status.update(f"[{color} b]{message}[/{color} b]", spinner_style=f"{color} bold")
                sleep(2)
            return new_list_of_cards

    def displayResults(self, shuffledDeck: List[Tuple[str, Union[str, int, Suit, Arcana]]], height: int) -> None:
        #Using -20 because each print leaves a newline which is an extra char, we did end="" to remove that extrachar so now we have 20 instead of 18 since we used 2 print statements with end="", subtracting total height by the chars taken helps with remaining space which we use
        calculatedHeight = min(max(int(((height-20) * (1/2)) * 1/2), 0), 4)
        #Using max here helps us with very small terminal windows, it ensures that when we have a small terminal window of a negative height or a height near zero, our calculatedheight may become negative, and so using max ensures it chooses 0 over the negative, same applies to the width
        #To minimize space between the panels while being within the correct terminal height range we minimize by dividing by 2, taking that first half of remaining terminal space, and then dividing it by 2 furthermore to get smaller versions
        #Using min here helps us strengthen minimization by making sure that in larger screens, that /2 of that remaining space * 1/2, isnt too large for a screen so we set a limit by choosing 2 whenever it gets large, Also in the final part we divide it by 2 because we used 2 gaps, and for example, dividing it by 3 would leave another empty 1/3 gap of the half of the remaining space, so we use /2 to fit the 2 panels and fill the half
        self.console.print("[#585b70]SHUFFLE RESULT[/#585b70]" + ("[#585b70]─[/#585b70]" * max(int((get_terminal_size().columns - len("SHUFFLE RESULT"))), 0)))
        self.console.print(Panel((
                f"[#fab387]Situation:[#fab387] [#fab387 b]{shuffledDeck[0][0]}[/#fab387 b]\n"
                f"[#fab387]Name:[#fab387] [#fab387 b]{shuffledDeck[0][1]}[/#fab387 b]\n"
                f"[#fab387]Number:[#fab387] [#fab387 b]{shuffledDeck[0][2]}[/#fab387 b]\n"  
            ).strip(),
            expand = False, title=shuffledDeck[0][1], title_align="left", border_style="#fab387"
            )
        )
        print("\n" * calculatedHeight, end="")
        self.console.print(Panel((
                f"[#f9e2af]Situation:[/#f9e2af] [#f9e2af b]{shuffledDeck[1][0]}[/#f9e2af b]\n"
                f"[#f9e2af]Name:[/#f9e2af] [#f9e2af b]{shuffledDeck[1][1]}[/#f9e2af b]\n"
                f"[#f9e2af]Number:[/#f9e2af] [#f9e2af b]{shuffledDeck[1][2]}[/#f9e2af b]\n"
            ).strip(),
            expand = False, title=shuffledDeck[1][1], title_align="left", border_style="#f9e2af"
            )
        )
        print("\n" * calculatedHeight, end="")
        self.console.print(Panel((
                f"[#a6e3a1]Situation:[/#a6e3a1] [#a6e3a1 b]{shuffledDeck[2][0]}[/#a6e3a1 b]\n"
                f"[#a6e3a1]Name:[/#a6e3a1] [#a6e3a1 b]{shuffledDeck[2][1]}[/#a6e3a1 b]\n"
                f"[#a6e3a1]Number:[/#a6e3a1] [#a6e3a1 b]{shuffledDeck[2][2]}[/#a6e3a1 b]\n"
            ).strip(),
            expand=False, title=shuffledDeck[2][1], title_align="left", border_style="#a6e3a1"
            )
        )
        self.console.print("[#585b70]─[/#585b70]" * max(int((get_terminal_size().columns)), 0))

    def processQuestion(self, question: Union[str, int]) -> Union[str, bool, None]:
        #Process user's question here  
        self.deck_data: List[Tuple[str, Union[str, int, Suit, Arcana]]] = self.shuffle_spinner(self.return_deck(f"{self.file_directory}/tarot_data.json"))
        self.clearScreen()
        self.displayResults(self.deck_data, get_terminal_size().lines)
        try:
            ollama_response: str = self.response_spinner(question, self.deck_data)
        except requests.exceptions.RequestException as requestException:
            self.console.print("[#f38ba8 b][ㄨ] A severe post request error has occured![/#f38ba8 b]")
            raise API_ERROR(message=None, error=requestException) 
        self.clearScreen()
        return self.typeWrite(ollama_response, 0.01)

    def renderPanel(self) -> rich.panel.Panel:
        mainPanel: rich.panel.Panel = Panel(self.boxContent.strip(), expand = False, title = "[b]About[/b]", title_align = "left", border_style = "#b4befe")
        return mainPanel

    def finalizePanel(self, width: int) -> None:
        self.console.print(self.renderPanel())
        self.console.print((f"[#585b70 b]{self.tiptext}[/#585b70 b]") + ("[#585b70]─[/#585b70]" * max(0, int((width - len(self.tiptext))))))
        #To create a dynamic "-" we multiply by the width, if we were to include text such as tiptext, simply multiplyig by the full width will not multiply the dash by the remaining space, we must take the full width of the terminal screen, including the tiptext and the dashes, and subtract the width by the len of tiptext to find the remaining space, then we multiply the - by that remaining space to fill the rest, using max helps with negative terminal sizes (very small) so - with the text will result in a negative, we lock it to 0

    def execute(self) -> None:
        orders: List[Callable[None,None]] = [
            lambda: self.clearScreen(),
            lambda: self.drawAscii(self.effect),
            lambda: self.finalizePanel(get_terminal_size().columns), 
            lambda: self.processQuestion(self.userPrompt(self.ptk_style))
        ]
        while True:
            for index, execution in enumerate(orders):
                choice_for_exit: Union[str, bool, None] = execution()
                if choice_for_exit == "exit":
                    return
                else:
                    pass
