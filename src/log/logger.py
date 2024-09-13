import logging
from pathlib import Path
from os import mkdir
from os.path import exists

from rich.logging import RichHandler


class Logger:
    """ Custom logger """

    def __init__(self) -> None:
        logging.basicConfig(
            format="%(message)s",
            level=logging.INFO,
            datefmt="[%X]",
            handlers=[
                    RichHandler(
                        show_time=False,
                        show_path=False
                    )
                ]
        )

        self.log: logging.Logger = logging.getLogger("rich")

        BASE_PATH: str = f"{Path.home()}/.checker"
        if not exists(BASE_PATH):
            try:
                mkdir(BASE_PATH)
            except (PermissionError, OSError) as err:
                self.CRIT(f"{err}")
                raise SystemExit(err) from err

        file_log = logging.FileHandler(
                filename=f"{BASE_PATH}/checker.log"
            )

        file_log.setLevel(logging.INFO)
        file_log.setFormatter(
            logging.Formatter(
                "%(levelname)s %(message)s"
            )
        )
        self.log.addHandler(file_log)

    def CRIT(self, msg: str) -> None:
        self.log.critical("CRIT: %s", msg)

    def ERR(self, msg: str) -> None:
        self.log.error("ERR: %s", msg)

    def INFO(self, msg: str) -> None:
        self.log.info("INFO: %s", msg)
