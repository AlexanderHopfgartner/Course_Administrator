import os
from typing import TypedDict, Optional


INPUT_END = "\n>>>"
YON = "[yes/no]"


def clear():
    """Clears the Console"""
    os.system('cls' if os.name == 'nt' else 'clear')


def itis(text: str) -> bool:
    answer = input(text)
    if answer:
        return answer.lower()[0] == "y"
    return False
