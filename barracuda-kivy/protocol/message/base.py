#!/usr/bin/python
##-------------------------------##
## Barracuda: Kivy Client        ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Protocol Message: Abstract    ##
##-------------------------------##

## Imports
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import ClassVar


## Classes
class BaseMessage(ABC):
    """
    """

    # -Instance Methods
    @abstractmethod
    def to_bytes(self) -> bytes: ...

    # -Class Methods
    @classmethod
    @abstractmethod
    def from_bytes(cls, data: bytes) -> BaseMessage: ...

    # -Class Properties
    CODE: ClassVar[int]
