import logging
from functools import lru_cache

from rich.console import Console
from rich.logging import RichHandler

console = Console(color_system="256", width=200, style="blue")


getLogger = logging.getLogger