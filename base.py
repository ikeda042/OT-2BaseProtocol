from opentrons import protocol_api
from enum import Enum

metadata = {
    "protocolName": "Base Protocol",
    "author": "ikeda042",
    "description": "A base protocol for OpenTrons.",
    "apiLevel": "2.18",
}


class TipRackType(Enum):
    P20 = "opentrons_96_tiprack_20ul"
    P300 = "opentrons_96_tiprack_300ul"


class PipetteType(Enum):
    P20 = "p20_multi_gen2"
    P300 = "p300_multi_gen2"


class PlateType(Enum):
    P96 = "corning_96_wellplate_360ul_flat"


class ReservoirType(Enum):
    R96 = "corning_96_wellplate_360ul_flat"


def run(protocol: protocol_api.ProtocolContext) -> None:
    plate: protocol_api.Labware = protocol.load_labware(PlateType.P96.value, location=1)
    tip_rack_300: protocol_api.Labware = protocol.load_labware(
        TipRackType.P300.value, location=3
    )
    reservoir: protocol_api.Labware = protocol.load_labware(
        ReservoirType.R96.value, location=2
    )
    right_pipette: protocol_api.InstrumentContext = protocol.load_instrument(
        PipetteType.P300.value, mount="right", tip_racks=[tip_rack_300]
    )
    right_pipette.pick_up_tip()
    for i in range(1, 13):
        right_pipette.aspirate(100, reservoir["A7"])
        right_pipette.dispense(100, plate[f"A{i}"])
        right_pipette.blow_out()
    right_pipette.drop_tip()
