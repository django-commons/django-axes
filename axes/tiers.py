"""
``LockoutTier`` for the ``AXES_LOCKOUT_TIERS`` setting.

This module MUST NOT import Django settings or anything that reads them,
so that it can be imported from a Django settings module (#1544).
"""

from dataclasses import dataclass
from datetime import timedelta


@dataclass(frozen=True, order=True)
class LockoutTier:
    failures: int
    cooloff: timedelta
