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


class PipetteType(Enum):
    P20 = "p20_single_gen2"
    P300 = "p300_single_gen2"


class PlateType(Enum):
    P96 = "corning_96_wellplate_360ul_flat"
