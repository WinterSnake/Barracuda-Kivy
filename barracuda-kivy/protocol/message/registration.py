#!/usr/bin/python
##-------------------------------##
## Barracuda: Protocol           ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message: Request[Register]    ##
##-------------------------------##

## Imports
from __future__ import annotations

from .base import BaseMessage

## Constants
__all__: tuple[str] = ("Client",)


## Classes
class RequestAccountRegister(BaseMessage):
    """
    """

    # -Constructor
    def __init__(self, username: str, hashed_password: bytes, salt: str) -> None:
        self.username: str = username
        self.hashed_password: bytes = hashed_password
        self.salt: str = salt

    # -Instance Methods
    def to_bytes(self) -> bytes:
        data = bytearray([RequestAccountRegister.CODE])
        username = self.username.encode('utf-8')
        data += len(username).to_bytes(4)
        data += username
        salt = self.salt.encode('utf-8')
        data += len(salt).to_bytes(4)
        data += salt
        data += self.hashed_password
        return data

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> RequestAccountRegister:
        ''''''
        raise NotImplementedError(
            "RequestAccountRegistrationMessage.from_bytes(data) implementation"
            "only required for server"
        )

    # -Class Properties
    CODE = 0x01
