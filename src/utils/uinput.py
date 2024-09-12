from collections.abc import Callable
from typing import Any


class ParseInput:
    def __init__(self, input_func: Callable) -> None:
        self.input_func: Callable = input_func

    def call_func(self) -> dict[str, Any]:
        return {
            "any": Any
        }


