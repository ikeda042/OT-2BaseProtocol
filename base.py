from opentrons import protocol_api
from enum import Enum

metadata = {
    "protocolName": "Base Protocol",
    "author": "ikeda042",
    "description": "A base protocol for OpenTrons.",
    "apiLevel": "2.19",
}


class TipRackType(Enum):
    P20 = "opentrons_96_tiprack_20ul"
    P300 = "opentrons_96_tiprack_300ul"
    P1000 = "opentrons_96_tiprack_1000ul"
