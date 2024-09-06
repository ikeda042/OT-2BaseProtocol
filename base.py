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


class Settings:
    def __init__(
        self,
        tip_rack_type: TipRackType,
        left_pipette_type: PipetteType,
        right_pipette_type: PipetteType,
        plate_type: PlateType,
    ) -> None:
        self.tip_rack_type = tip_rack_type
        self.left_pipette_type = left_pipette_type
        self.right_pipette_type = right_pipette_type
        self.plate_type = plate_type


settings = Settings(
    tip_rack_type=TipRackType.P20,
    left_pipette_type=PipetteType.P20,
    right_pipette_type=PipetteType.P300,
    plate_type=PlateType.P96,
)
