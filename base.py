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
    tip_rack_20 = protocol.load_labware(TipRackType.P20, location=2)
    # tip_rack_300 = protocol.load_labware(TipRackType.P300, location=4)
    left_pipette = protocol.load_instrument(
        PipetteType.P20, mount="left", tip_racks=[tip_rack_20]
    )
    reservoir = protocol.load_labware(ReservoirType.R96, location=3)
    # right_pipette = protocol.load_instrument(
    #     PipetteType.P300, mount="right", tip_racks=[tip_rack_300]
    # )

    left_pipette.pick_up_tip()
    for i in range(1, 3):
        left_pipette.aspirate(50, reservoir["A7"])
        left_pipette.dispense(50, plate[f"A{i}"])
        left_pipette.blow_out()
    # drop tip where it was picked up
    left_pipette.drop_tip(
        home_after=False
    )  # home_after=False to prevent the tip from being dropped at the trash
    )
