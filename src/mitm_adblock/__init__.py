"""
mitmproxy-adblock package.

Ad blocker for mitmproxy
"""
from typing import List

from .adblocker import AdBlocker

__version__ = "0.2.0"
__all__: List[str] = ["addons"]  # noqa: WPS410 (the only __variable__ we use)

addons = [AdBlocker()]
