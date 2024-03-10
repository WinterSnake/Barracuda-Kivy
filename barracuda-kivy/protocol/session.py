#!/usr/bin/python
##-------------------------------##
## Barracuda: Kivy Client        ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Protocol: Session             ##
##-------------------------------##

## Imports
import socket

from .message import Message

## Constants
__all__: tuple[str] = ("Session",)


## Classes
class Session:
    """
    Barracuda Protocol: Session
    Barebones session wrapper implementation around raw TCP socket
    to handle the Barracuda Protocol.
    """

    # -Constructors
    def __init__(self) -> None:
        self._socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # -Instance Methods
    def connect(self, ip: str, port: int) -> str | None:
        '''Connects to Barracuda server. Returns error message if connection fails'''
        try:
            self._socket.connect((ip, port))
        except ConnectionRefusedError:
            return f"Unable to connect to Barracuda server @{ip}:{port}"
        return None

    def receive_message(self) -> Message:
        '''Reads socket data and returns new message. If invalid, throws an error'''
        return Message.from_bytes(b'\x00')

    def send_message(self, message: Message, compressed: bool = False) -> None:
        '''Sends un/compressed message over socket'''
        data = message.to_bytes()
        self._socket.send(data)
