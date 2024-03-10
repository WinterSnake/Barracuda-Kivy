#!/usr/bin/python
##-------------------------------##
## Barracuda: Kivy Client        ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Protocol                      ##
##-------------------------------##

## Imports
import hashlib
import random

from .message import Message
from .session import Session

## Constants
__all__: tuple[str] = ("Client",)


## Classes
class Client(Session):
    """Barracuda Client Session"""

    # -Instance Methods: Public
    def request_account_login(self, username: str, password_hash: bytes) -> None:
        '''Send Account::Login request event to Barracuda server'''
        pass

    def request_account_register(
        self, username: str, password_hash: bytes, salt: str
    ) -> None:
        '''Send Account::Register request event to Barracuda server'''
        msg = Message(
            Message.Type.RequestAccountRegister,
            username=username, password_hash=password_hash, salt=salt
        )
        self.send_message(msg)

    def request_account_salt(self, username: str) -> None:
        '''Send Account::GetSalt request event to Barracuda server'''
        pass
