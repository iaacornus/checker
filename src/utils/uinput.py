from datetime import datetime
from collections.abc import Callable
from typing import Any, Self

from src.misc.types import Output
from src.log.logger import Logger


class ParseInput:
    def __init__(
            self: Self,
            log: Logger,
            input_func: Callable,
            act_num: int
        ) -> None:
        self.log = log
        self.input_func: Callable = input_func
        self.act_num: int = act_num

    def call_func(self: Self) -> Output:
        try:
            func_out: Output = {}

            for i in range(3): # calling function 3 times
                output_: Any = self.input_func
                func_out[f"return-{i}"] = output_
        except (AttributeError, ImportError) as err:
            self.log.CRIT(f"{err}")
            raise SystemExit(
                    f"{err} was raised."
                ) from err

        return {
                "func_name": self.input_func.__name__,
                "out": func_out
            }

    def store_output(self: Self) -> bool:
        function_out: Output = self.call_func()
        fname: str = f"output-act-{self.act_num}"

        try:
            with open(
                    "w", fname, encoding="utf-8"
                ) as file_out:
                function_out["date"] = (
                        datetime
                            .now()
                            .strftime(
                                "%d/%m/%Y %H:%M:%S"
                            )
                    )
                file_out.write(function_out)
        except (
                IOError,
                SystemError,
                PermissionError
            ) as err:
            self.log.CRIT(
                f"{err}: Cannot write into file ..."
            )
            return False

        return True


