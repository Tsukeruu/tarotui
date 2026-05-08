from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Any, Callable
from src.utils.functions import main

"""
 ▀▄    ▀█▀ █▀█ █▀▄ █▀█ ▀█▀ █ █ ▀█▀
  ▄▀    █  █▀█ █▀▄ █ █  █  █ █  █ 
 ▀      ▀  ▀ ▀ ▀ ▀ ▀▀▀  ▀  ▀▀▀ ▀▀▀
- This is the wrapper
- When the user executes this, a hierachy works its way from top to bottom
"""

class Main(main):
    def __init__(self) -> None:
        super().__init__() 

    def run(self) -> None:
        super().execute()


app = Main()
app.run()
