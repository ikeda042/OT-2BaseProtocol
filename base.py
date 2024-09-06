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


class ReservoirType(Enum):
    R96 = "corning_96_wellplate_360ul_flat"


def run(protocol: protocol_api.ProtocolContext) -> None:
    plate = protocol.load_labware(PlateType.P96, location=1)
    tip_rack = protocol.load_labware(TipRackType.P20, location=2)
    left_pipette = protocol.load_instrument(
        PipetteType.P20, mount="left", tip_racks=[tip_rack]
    )
    reservoir = protocol.load_labware(ReservoirType.R96, location=3)
    # right_pipette = protocol.load_instrument(
    #     PipetteType.P300, mount="right", tip_racks=[tip_rack]
    # )
    left_pipette.pick_up_tip()
