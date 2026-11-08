"""Reachy Mini SDK."""

from importlib.metadata import version

from reachy_mini.apps.app import ReachyMiniApp
from reachy_mini.io.protocol import MoveBusyError
from reachy_mini.reachy_mini import ReachyMini, VOICE, WAKE_UP_SENTENCE

__version__ = version("reachy_mini")

__all__ = [
    "MoveBusyError",
    "ReachyMini",
    "ReachyMiniApp",
    "VOICE",
    "WAKE_UP_SENTENCE",
    "__version__",
]
