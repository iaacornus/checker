from collections.abc import Callable
from typing import Any, Self

from src.utils.logger import Logger


class ParseInput:
    def __init__(
            self: Self,
        ) -> None:
        self.log = log
        self.input_func: Callable = input_func

    def call_func(self: Self) -> Output:
        # calling function
        try:
            function_out: Any = self.input_func()
        except (AttributeError, ImportError) as err:
            self.log.CRIT(f"{err}")
            raise SystemExit(
                    f"{err} was raised."
                ) from err

        return {
                "func_name": self.input_func.__name__,
                "out": function_out
            }


