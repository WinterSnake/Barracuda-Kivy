#!/usr/bin/python
##-------------------------------##
## Barracuda: Protocol           ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message                       ##
##-------------------------------##

## Imports
from __future__ import annotations
from enum import IntEnum
from typing import Any, TypedDict, cast


## Classes
class Message:
    """
    Barracuda Protocol: Message
    Message class for communicating back and forth between the Barracuda server.
    """

    # -Constructor
    def __init__(self, _type: Message.Type, **kwargs: bytes | int | str) -> None:
        self.type: Message.Type = _type
        self.data: MessageData = cast(MessageData, kwargs)

    # -Instance Methods
    def to_bytes(self) -> bytes:
        '''Convert message to byte array for sending over network socket'''
        bytes_ = bytearray([self.type])
        match self.type:
            case Message.Type.RequestAccountRegister:
                data: RequestAccountRegister = cast(RequestAccountRegister, self.data)
                username = data['username'].encode('utf-8')
                bytes_ += len(username).to_bytes(4)
                bytes_ += username
                salt = data['salt'].encode('utf-8')
                bytes_ += len(salt).to_bytes(4)
                bytes_ += salt
                bytes_ += len(data['password_hash']).to_bytes(4)
                bytes_ += data['password_hash']
        bytes_[1:1] = (len(bytes_) - 1).to_bytes(4)
        return bytes_

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> Message:
        '''Convert network socket received byte array back into Message'''
        return cls(Message.Type.RequestAccountRegister)

    # -Sub-Classes
    class Type(IntEnum):
        '''Barracuda Protocol Message Type'''
        RequestAccountRegister = 0x01


class MessageData(TypedDict, total=False):
    pass


class RequestAccountRegister(MessageData):
    username: str
    password_hash: bytes
    salt: str
