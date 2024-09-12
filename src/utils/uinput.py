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


