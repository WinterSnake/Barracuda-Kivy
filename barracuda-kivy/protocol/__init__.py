#!/usr/bin/python
##-------------------------------##
## Barracuda: Kivy Client        ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Protocol                      ##
##-------------------------------##

## Imports
import hashlib
import socket

from .message import (
    BaseMessage,
    RequestAccountRegister,
)

## Constants
__all__: tuple[str] = ("Client",)


## Functions
def salt_password(username: str, password: str, salt: str) -> bytes:
    """
    """
    split_size = len(password) // 2
    hash_data = password[:split_size] + username + password[split_size:] + salt
    m = hashlib.sha256(hash_data.encode('utf-8'))
    return m.digest()


## Classes
class Client:
    """
    Barracuda Client Socket Protocol.
    Wrapper implementation around raw TCP socket to handle the Barracuda
    Protocol for the python Kivy client.
    """

    # -Constructors
    def __init__(self) -> None:
        self._socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # -Instance Methods: Public
    def connect(self, ip: str, port: int) -> str | None:
        '''Connects to Barracuda server. Returns error message if connection fails'''
        try:
            self._socket.connect((ip, port))
        except ConnectionRefusedError:
            return f"Unable to connect to Barracuda server @{ip}:{port}"

    def request_account_login(self, username: str, hashed_password: bytes) -> None:
        ''''''
        pass

    def request_account_register(
        self, username: str, hashed_password: str, salt: str
    ) -> None:
        ''''''
        self._send_message(RequestAccountRegister(
            username, hashed_password, salt
        ))

    def request_account_salt(self, username: str) -> None:
        ''''''
        pass

    # -Instance Methods: Private
    def _send_message(self, message: BaseMessage) -> None:
        '''INTERNAL: Add length of message and send through socket'''
        data = message.to_bytes()
        data[1:1] = (len(data) - 1).to_bytes(4)
        self._socket.send(data)
