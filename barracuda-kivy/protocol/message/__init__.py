#!/usr/bin/python
##-------------------------------##
## Barracuda: Kivy Client        ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Protocol: Message             ##
##-------------------------------##

## Imports
from .base import BaseMessage
from .registration import RequestAccountRegister

## Constants
__all__: tuple[str] = (
    # -Account Registration
    "RequestAccountRegister", 
    # -Account Login
)
