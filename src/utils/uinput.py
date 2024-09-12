from collections.abc import Callable
from typing import Any

from src.utils.logger import Logger


class ParseInput:
    def __init__(
            self, log: Logger, input_func: Callable
        ) -> None:
        self.log = log
        self.input_func: Callable = input_func

    def call_func(self) -> dict[str, Any]:
        return {
            "any": Any
        }


