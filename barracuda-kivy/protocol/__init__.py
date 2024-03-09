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

## Constants
__all__: tuple[str] = ("Client",)


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

    def request_register_account(self, username: str, password: str, salt: str) -> None:
        ''''''
        pass

    def request_account_salt(self, username: str) -> None:
        ''''''
        pass

    def request_login(self, username: str, password: str, salt: str) -> None:
        ''''''
        pass
