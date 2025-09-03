from typing import List

from patcher.models.models import FilePatchConfig, FileProcessingType
from patcher.patterns.evAr01Zn01_Gimmic import evAr01Zn01_Gimmic_patch_pattern
from patcher.patterns.evAr01Zn01_Npc_Main import \
    evAr01Zn01_Npc_Main_patch_pattern
from patcher.patterns.evAr01Zn02_Npc_Main import evAr01Zn02_Npc_Main_patterns
from patcher.patterns.evAr02Zn01_Npc_Main import evAr02Zn01_Npc_Main_pattern
from patcher.patterns.evAr03Zn01_Npc_Main import evAr03Zn01_Npc_Main_pattern
from patcher.patterns.evAr03Zn02_Npc_Main import evAr03Zn02_Npc_Main_patterns
from patcher.patterns.evAr03Zn03_Npc_Main import evAr03Zn03_Npc_Main_patterns
from patcher.patterns.evAr04Zn01_Gimmic import evAr04Zn01_Gimmic_patterns
from patcher.patterns.evAr04Zn01_Npc_Main import evAr04Zn01_Npc_Main_patterns
from patcher.patterns.evAr04Zn02_Npc_Main import evAr04Zn02_Npc_Main_patterns
from patcher.patterns.evAr05Zn01_Gimmic import evAr05Zn01_Gimmic_patterns
from patcher.patterns.evAr05Zn01_Npc_Main import evAr05Zn01_Npc_Main_patterns
from patcher.patterns.evAr99Zn01_Npc_Main import evAr99Zn01_Npc_Main_pattern
from patcher.patterns.gk0101Gate import gate101_close
from patcher.patterns.gk0302Gate import gk0302Gate_pattern
from patcher.patterns.gk0402Bridge import gk0402Bridge_pattern
from patcher.patterns.gk0402Gate import gk0402Gate_pattern
from patcher.patterns.gk0501GateA import gk0501Gate_pattern
from patcher.patterns.gk0502DoorB import gk0502DoorB_pattern
from patcher.patterns.gk0502DoorC import gk0502DoorC_pattern
from patcher.patterns.gk0502DoorD import gk0502DoorD_pattern
from patcher.patterns.gk0502DoorE import gk0502DoorE_pattern
from patcher.patterns.gk0601DoorB import gk0601DoorB_pattern
from patcher.patterns.gkBookShelf import gkBookShelf_pattern
from patcher.patterns.gkFireWallB import gkFireWall_pattern
from patcher.patterns.gkKabigonWall import gkKabigonWallPattern
from patcher.patterns.gkMammoo import gkMammoo_patterns
from patcher.patterns.gkRecycleSanbasiA import gkRecycleSanbasiA_pattern
from patcher.patterns.gkRecycleSanbasiB import gkRecycleSanbasiB_pattern
from patcher.patterns.gkRecycleSanbasiC import gkRecycleSanbasiC_pattern
from patcher.patterns.gkRecycleSanbasiD import gkRecycleSanbasiD_pattern
from patcher.patterns.gkRockB import gkRockB
from patcher.patterns.gkWoodBoxKino import gkWoodBoxKinoPattern
from patcher.patterns.main import main_dol_pattern
from patcher.patterns.mnAttractionInfo import mnAttractionInfo_pattern
from patcher.patterns.mnLobby import mnLobby_pattern
from patcher.patterns.mnStartMenu import load_new_file_pattern
from patcher.patterns.treehouse import treehouse_pattern

plando_dict_ap = None


def get_default_patch_configs() -> List[FilePatchConfig]:
    configs = []

    field_Ar03Zn03_npc_script_config = FilePatchConfig(
        file_id="Ar03_Zn03",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar03Zn03Dat.dac", "Temporary/Field/ParkAr03Zn03Dat.dan",
                     "Script/evAr03Zn03_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar03Zn03Dat_Fr.dac", "Temporary/Field/ParkAr03Zn03Dat_Fr.dan",
                        "Script/evAr03Zn03_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar03Zn03Dat_Ge.dac", "Temporary/Field/ParkAr03Zn03Dat_Ge.dan",
                        "Script/evAr03Zn03_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn03Dat_It.dac", "Temporary/Field/ParkAr03Zn03Dat_It.dan",
                        "Script/evAr03Zn03_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn03Dat_Sp.dac", "Temporary/Field/ParkAr03Zn03Dat_Sp.dan",
                        "Script/evAr03Zn03_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr03Zn03_Npc_Main_patterns
    )
    configs.append(field_Ar03Zn03_npc_script_config)

    gkmammoo = FilePatchConfig(
        file_id="gkmammoo_gimmic",
        description="frozen Piloswine",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar03Zn02Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/GkMammoo.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn02Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkMammoo.fsb"), (
                        "DATA/files/Field/Ar03Zn02Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkMammoo.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn02Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkMammoo.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn02Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkMammoo.fsb"),
                    ],
        patch_patterns=gkMammoo_patterns
    )
    configs.append(gkmammoo)

    gk0302gate = FilePatchConfig(
        file_id="gate0302_gimmic",
        description="Empoleon Gate Magma Zone",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar03Zn02Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/Gk0302Gate.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn02Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0302Gate.fsb"), (
                        "DATA/files/Field/Ar03Zn02Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0302Gate.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn02Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0302Gate.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn02Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0302Gate.fsb"),
                    ],
        patch_patterns=gk0302Gate_pattern
    )
    configs.append(gk0302gate)

    field_Ar03Zn02_npc_script_config = FilePatchConfig(
        file_id="Ar03_Zn02",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar03Zn02Dat.dac", "Temporary/Field/ParkAr03Zn02Dat.dan",
                     "Script/evAr03Zn02_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar03Zn02Dat_Fr.dac", "Temporary/Field/ParkAr03Zn02Dat_Fr.dan",
                        "Script/evAr03Zn02_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar03Zn02Dat_Ge.dac", "Temporary/Field/ParkAr03Zn02Dat_Ge.dan",
                        "Script/evAr03Zn02_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn02Dat_It.dac", "Temporary/Field/ParkAr03Zn02Dat_It.dan",
                        "Script/evAr03Zn02_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn02Dat_Sp.dac", "Temporary/Field/ParkAr03Zn02Dat_Sp.dan",
                        "Script/evAr03Zn02_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr03Zn02_Npc_Main_patterns
    )
    configs.append(field_Ar03Zn02_npc_script_config)

    gk0601DoorB = FilePatchConfig(
        file_id="gk0601_doorb_gimmic",
        description="Granite Zone Flygon DoorB",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar06Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/Gk0601DoorB.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0601DoorB.fsb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0601DoorB.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0601DoorB.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0601DoorB.fsb"),
                    ],
        patch_patterns=gk0601DoorB_pattern
    )
    configs.append(gk0601DoorB)

    gkBookShelf = FilePatchConfig(
        file_id="gk0502_doorb_gimmic",
        description="Haunted Zone Mansion DoorB",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar05Zn02Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/GkBookShelf.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkBookShelf.fsb"), (
                        "DATA/files/Field/Ar05Zn02Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkBookShelf.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkBookShelf.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkBookShelf.fsb"),
                    ],
        patch_patterns=gkBookShelf_pattern
    )
    configs.append(gkBookShelf)

    gk0502DoorB = FilePatchConfig(
        file_id="gk0502_doorb_gimmic",
        description="Haunted Zone Mansion DoorB",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar05Zn02Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/Gk0502DoorB.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorB.fsb"), (
                        "DATA/files/Field/Ar05Zn02Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorB.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorB.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorB.fsb"),
                    ],
        patch_patterns=gk0502DoorB_pattern
    )
    configs.append(gk0502DoorB)

    gk0502DoorC = FilePatchConfig(
        file_id="gk0502_doorc_gimmic",
        description="Haunted Zone Mansion DoorC",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar05Zn02Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/Gk0502DoorC.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorC.fsb"), (
                        "DATA/files/Field/Ar05Zn02Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorC.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorC.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorC.fsb"),
                    ],
        patch_patterns=gk0502DoorC_pattern
    )
    configs.append(gk0502DoorC)

    gk0502DoorD = FilePatchConfig(
        file_id="gk0502_doord_gimmic",
        description="Haunted Zone Mansion DoorD",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar05Zn02Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/Gk0502DoorD.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorD.fsb"), (
                        "DATA/files/Field/Ar05Zn02Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorD.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorD.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorD.fsb"),
                    ],
        patch_patterns=gk0502DoorD_pattern
    )
    configs.append(gk0502DoorD)

    gk0502DoorE = FilePatchConfig(
        file_id="gk0502_doore_gimmic",
        description="Haunted Zone Mansion DoorE",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar05Zn02Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/Gk0502DoorE.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorE.fsb"), (
                        "DATA/files/Field/Ar05Zn02Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorE.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorE.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0502DoorE.fsb"),
                    ],
        patch_patterns=gk0502DoorE_pattern
    )
    configs.append(gk0502DoorE)

    gk0501gate = FilePatchConfig(
        file_id="gate0501_gimmic",
        description="Haunted Zone Gate A",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar05Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/Gk0501GateA.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0501GateA.fsb"), (
                        "DATA/files/Field/Ar05Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0501GateA.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0501GateA.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0501GateA.fsb"),
                    ],
        patch_patterns=gk0501Gate_pattern
    )
    configs.append(gk0501gate)

    field_Ar05Zn01_npc_script_config = FilePatchConfig(
        file_id="Ar05_Zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar05Zn01Dat.dac", "Temporary/Field/ParkAr05Zn01Dat.dan",
                     "Script/evAr05Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar05Zn01Dat_Fr.dac", "Temporary/Field/ParkAr05Zn01Dat_Fr.dan",
                        "Script/evAr05Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar05Zn01Dat_Ge.dac", "Temporary/Field/ParkAr05Zn01Dat_Ge.dan",
                        "Script/evAr05Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn01Dat_It.dac", "Temporary/Field/ParkAr05Zn01Dat_It.dan",
                        "Script/evAr05Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn01Dat_Sp.dac", "Temporary/Field/ParkAr05Zn01Dat_Sp.dan",
                        "Script/evAr05Zn01_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr05Zn01_Npc_Main_patterns
    )
    configs.append(field_Ar05Zn01_npc_script_config)

    evAr05Zn01_Gimmic = FilePatchConfig(
        file_id="ar05zn01_gimmic",
        description="",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar05Zn01Dat.dac", "Temporary/Field/ParkAr05Zn01Dat.dan",
                     "Script/evAr05Zn01_Gimmic.fsb"), (
                        "DATA/files/Field/Ar05Zn01Dat_Fr.dac", "Temporary/Field/ParkAr05Zn01Dat_Fr.dan",
                        "Script/evAr05Zn01_Gimmic.fsb"), (
                        "DATA/files/Field/Ar05Zn01Dat_Ge.dac", "Temporary/Field/ParkAr05Zn01Dat_Ge.dan",
                        "Script/evAr05Zn01_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn01Dat_It.dac", "Temporary/Field/ParkAr05Zn01Dat_It.dan",
                        "Script/evAr05Zn01_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn01Dat_Sp.dac", "Temporary/Field/ParkAr05Zn01Dat_Sp.dan",
                        "Script/evAr05Zn01_Gimmic.fsb"),
                    ],
        patch_patterns=evAr05Zn01_Gimmic_patterns
    )
    configs.append(evAr05Zn01_Gimmic)

    field_Ar04Zn02_npc_script_config = FilePatchConfig(
        file_id="Ar04_Zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn02Dat.dac", "Temporary/Field/ParkAr04Zn02Dat.dan",
                     "Script/evAr04Zn02_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Fr.dac", "Temporary/Field/ParkAr04Zn02Dat_Fr.dan",
                        "Script/evAr04Zn02_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Ge.dac", "Temporary/Field/ParkAr04Zn02Dat_Ge.dan",
                        "Script/evAr04Zn02_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_It.dac", "Temporary/Field/ParkAr04Zn02Dat_It.dan",
                        "Script/evAr04Zn02_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Sp.dac", "Temporary/Field/ParkAr04Zn02Dat_Sp.dan",
                        "Script/evAr04Zn02_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr04Zn02_Npc_Main_patterns
    )
    configs.append(field_Ar04Zn02_npc_script_config)

    gk0402gate = FilePatchConfig(
        file_id="gate0402_gimmic",
        description="Blaziken Gate Magma Zone",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar04Zn02Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/Gk0402Gate.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0402Gate.fsb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0402Gate.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0402Gate.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0402Gate.fsb"),
                    ],
        patch_patterns=gk0402Gate_pattern
    )
    configs.append(gk0402gate)

    gk0402bridge = FilePatchConfig(
        file_id="bridge0402_gimmic",
        description="Blaziken Bridge Magma Zone",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar04Zn02Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/Gk0402Bridge.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0402Bridge.fsb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0402Bridge.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0402Bridge.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0402Bridge.fsb"),
                    ],
        patch_patterns=gk0402Bridge_pattern
    )
    configs.append(gk0402bridge)

    firewall_b = FilePatchConfig(
        file_id="firewallB_gimmic",
        description="Fire Wall Magma Zone",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar04Zn02Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/GkFireWallB.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkFireWallB.fsb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkFireWallB.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkFireWallB.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkFireWallB.fsb"),
                    ],
        patch_patterns=gkFireWall_pattern
    )
    configs.append(firewall_b)

    rockB = FilePatchConfig(
        file_id="rockB_gimmic",
        description="Gimmic Rock blocking lapras",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar03Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/GkRockB.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRockB.fsb"), (
                        "DATA/files/Field/Ar03Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRockB.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRockB.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRockB.fsb"),
                    ],
        patch_patterns=gkRockB
    )
    configs.append(rockB)

    recycleSanbasiA = FilePatchConfig(
        file_id="recycleSanbasiA_gimmic",
        description="Gimmic Bridge1 for beach zone",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar03Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/GkRecycleSanbasiA.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiA.fsb"), (
                        "DATA/files/Field/Ar03Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiA.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiA.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiA.fsb"),
                    ],
        patch_patterns=gkRecycleSanbasiA_pattern
    )
    configs.append(recycleSanbasiA)

    recycleSanbasiB = FilePatchConfig(
        file_id="recycleSanbasiB_gimmic",
        description="Gimmic Bridge2 for beach zone",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar03Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/GkRecycleSanbasiB.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiB.fsb"), (
                        "DATA/files/Field/Ar03Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiB.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiB.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiB.fsb"),
                    ],
        patch_patterns=gkRecycleSanbasiB_pattern
    )
    configs.append(recycleSanbasiB)

    recycleSanbasiC = FilePatchConfig(
        file_id="recycleSanbasiC_gimmic",
        description="Gimmic Bridge2 for beach zone",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar03Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/GkRecycleSanbasiC.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiC.fsb"), (
                        "DATA/files/Field/Ar03Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiC.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiC.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiC.fsb"),
                    ],
        patch_patterns=gkRecycleSanbasiC_pattern
    )
    configs.append(recycleSanbasiC)

    recycleSanbasiD = FilePatchConfig(
        file_id="recycleSanbasiD_gimmic",
        description="Gimmic Bridge2 for beach zone",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar03Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/GkRecycleSanbasiD.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiD.fsb"), (
                        "DATA/files/Field/Ar03Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiD.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiD.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkRecycleSanbasiD.fsb"),
                    ],
        patch_patterns=gkRecycleSanbasiD_pattern
    )
    configs.append(recycleSanbasiD)

    start_menu_config = FilePatchConfig(
        file_id="mnStartMenu",
        description="",
        processing_type=FileProcessingType.DAC_U8,
        file_group=[("DATA/files/Archive/StartMenuDat.dac", "unused",
                     "Script/mnStartMenu.fsb"),
                    ("DATA/files/Archive/StartMenuDat_Fr.dac", "unused",
                     "Script/mnStartMenu.fsb"),
                    ("DATA/files/Archive/StartMenuDat_Ge.dac", "unused",
                     "Script/mnStartMenu.fsb"),
                    ("DATA/files/Archive/StartMenuDat_It.dac", "unused",
                     "Script/mnStartMenu.fsb"),
                    ("DATA/files/Archive/StartMenuDat_Sp.dac", "unused",
                     "Script/mnStartMenu.fsb"),
                    ],
        patch_patterns=[
            load_new_file_pattern
        ]
    )
    configs.append(start_menu_config)

    field_Ar02Zn01_npc_script_config = FilePatchConfig(
        file_id="Ar02_Zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar02Zn01Dat.dac", "Temporary/Field/ParkAr02Zn01Dat.dan",
                     "Script/evAr02Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar02Zn01Dat_Fr.dac", "Temporary/Field/ParkAr02Zn01Dat_Fr.dan",
                        "Script/evAr02Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar02Zn01Dat_Ge.dac", "Temporary/Field/ParkAr02Zn01Dat_Ge.dan",
                        "Script/evAr02Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar02Zn01Dat_It.dac", "Temporary/Field/ParkAr02Zn01Dat_It.dan",
                        "Script/evAr02Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar02Zn01Dat_Sp.dac", "Temporary/Field/ParkAr02Zn01Dat_Sp.dan",
                        "Script/evAr02Zn01_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr02Zn01_Npc_Main_pattern
    )
    configs.append(field_Ar02Zn01_npc_script_config)

    field_Ar03Zn01_npc_script_config = FilePatchConfig(
        file_id="Ar03_Zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar03Zn01Dat.dac", "Temporary/Field/ParkAr03Zn01Dat.dan",
                     "Script/evAr03Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar03Zn01Dat_Fr.dac", "Temporary/Field/ParkAr03Zn01Dat_Fr.dan",
                        "Script/evAr03Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar03Zn01Dat_Ge.dac", "Temporary/Field/ParkAr03Zn01Dat_Ge.dan",
                        "Script/evAr03Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_It.dac", "Temporary/Field/ParkAr03Zn01Dat_It.dan",
                        "Script/evAr03Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Sp.dac", "Temporary/Field/ParkAr03Zn01Dat_Sp.dan",
                        "Script/evAr03Zn01_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr03Zn01_Npc_Main_pattern
    )
    configs.append(field_Ar03Zn01_npc_script_config)

    treehouse = FilePatchConfig(
        file_id="treehouse_gimmic",
        description="Gimmic Treehouse",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar02Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/GkTreeHouse.fsb"),
                    (
                        "DATA/files/Field/Ar02Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkTreeHouse.fsb"), (
                        "DATA/files/Field/Ar02Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkTreeHouse.fsb"),
                    (
                        "DATA/files/Field/Ar02Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkTreeHouse.fsb"),
                    (
                        "DATA/files/Field/Ar02Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkTreeHouse.fsb"),
                    ],
        patch_patterns=treehouse_pattern
    )
    configs.append(treehouse)

    field_Ar99Zn01_npc_script_config = FilePatchConfig(
        file_id="Ar99_Zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar99Zn01Dat.dac", "Temporary/Field/ParkAr99Zn01Dat.dan",
                     "Script/evAr99Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar99Zn01Dat_Fr.dac", "Temporary/Field/ParkAr99Zn01Dat_Fr.dan",
                        "Script/evAr99Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar99Zn01Dat_Ge.dac", "Temporary/Field/ParkAr99Zn01Dat_Ge.dan",
                        "Script/evAr99Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar99Zn01Dat_It.dac", "Temporary/Field/ParkAr99Zn01Dat_It.dan",
                        "Script/evAr99Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar99Zn01Dat_Sp.dac", "Temporary/Field/ParkAr99Zn01Dat_Sp.dan",
                        "Script/evAr99Zn01_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr99Zn01_Npc_Main_pattern
    )
    configs.append(field_Ar99Zn01_npc_script_config)
    field_Ar01Zn02_npc_script_config = FilePatchConfig(
        file_id="Ar01_Zn02",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar01Zn02Dat.dac", "Temporary/Field/ParkAr01Zn02Dat.dan",
                     "Script/evAr01Zn02_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar01Zn02Dat_Fr.dac", "Temporary/Field/ParkAr01Zn02Dat_Fr.dan",
                        "Script/evAr01Zn02_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar01Zn02Dat_Ge.dac", "Temporary/Field/ParkAr01Zn02Dat_Ge.dan",
                        "Script/evAr01Zn02_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn02Dat_It.dac", "Temporary/Field/ParkAr01Zn02Dat_It.dan",
                        "Script/evAr01Zn02_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn02Dat_Sp.dac", "Temporary/Field/ParkAr01Zn02Dat_Sp.dan",
                        "Script/evAr01Zn02_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr01Zn02_Npc_Main_patterns
    )
    configs.append(field_Ar01Zn02_npc_script_config)

    field_Ar04Zn01_gimmic_config = FilePatchConfig(
        file_id="Ar04_Zn01_gimmic",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn01Dat.dac", "Temporary/Field/ParkAr04Zn01Dat.dan",
                     "Script/evAr04Zn01_Gimmic.fsb"), (
                        "DATA/files/Field/Ar04Zn01Dat_Fr.dac", "Temporary/Field/ParkAr04Zn01Dat_Fr.dan",
                        "Script/evAr04Zn01_Gimmic.fsb"), (
                        "DATA/files/Field/Ar04Zn01Dat_Ge.dac", "Temporary/Field/ParkAr04Zn01Dat_Ge.dan",
                        "Script/evAr04Zn01_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn01Dat_It.dac", "Temporary/Field/ParkAr04Zn01Dat_It.dan",
                        "Script/evAr04Zn01_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn01Dat_Sp.dac", "Temporary/Field/ParkAr04Zn01Dat_Sp.dan",
                        "Script/evAr04Zn01_Gimmic.fsb"),
                    ],
        patch_patterns=evAr04Zn01_Gimmic_patterns
    )
    configs.append(field_Ar04Zn01_gimmic_config)

    field_Ar04Zn01_npc_script_config = FilePatchConfig(
        file_id="Ar04_Zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn01Dat.dac", "Temporary/Field/ParkAr04Zn01Dat.dan",
                     "Script/evAr04Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar04Zn01Dat_Fr.dac", "Temporary/Field/ParkAr04Zn01Dat_Fr.dan",
                        "Script/evAr04Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar04Zn01Dat_Ge.dac", "Temporary/Field/ParkAr04Zn01Dat_Ge.dan",
                        "Script/evAr04Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn01Dat_It.dac", "Temporary/Field/ParkAr04Zn01Dat_It.dan",
                        "Script/evAr04Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn01Dat_Sp.dac", "Temporary/Field/ParkAr04Zn01Dat_Sp.dan",
                        "Script/evAr04Zn01_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr04Zn01_Npc_Main_patterns
    )
    configs.append(field_Ar04Zn01_npc_script_config)

    field_gimmic_shroomish_crate = FilePatchConfig(
        file_id="shroomish_crate_gimmic",
        description="Gimmic Shroomish Crate",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar01Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/GkWoodBoxKino.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkWoodBoxKino.fsb"), (
                        "DATA/files/Field/Ar01Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkWoodBoxKino.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkWoodBoxKino.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkWoodBoxKino.fsb"),
                    ],
        patch_patterns=gkWoodBoxKinoPattern
    )
    configs.append(field_gimmic_shroomish_crate)

    kabigon_wall = FilePatchConfig(
        file_id="kabigon_wall_gimmic",
        description="Gimmic KabigonWall",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar99Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/GkKabigonWall.fsb"),
                    (
                        "DATA/files/Field/Ar99Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkKabigonWall.fsb"), (
                        "DATA/files/Field/Ar99Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkKabigonWall.fsb"),
                    (
                        "DATA/files/Field/Ar99Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkKabigonWall.fsb"),
                    (
                        "DATA/files/Field/Ar99Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkKabigonWall.fsb"),
                    ],
        patch_patterns=gkKabigonWallPattern
    )
    configs.append(kabigon_wall)

    lobby16 = FilePatchConfig(
        file_id="lobby16_bulbasaur",
        description="Bulbasaur Minigame Lobby",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/Lobby16Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/Lobby16Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/Lobby16Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/Lobby16Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/Lobby16Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    configs.append(lobby16)

    lobby3 = FilePatchConfig(
        file_id="lobby3_venusaur",
        description="Venusaur Minigame Lobby",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby03Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby03Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby03Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby03Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby03Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    configs.append(lobby3)

    attraction16 = FilePatchConfig(
        file_id="attraction_info16_bulbasaur",
        description="Bulbasaur Minigame Attraction",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At016Dat.dac", "Temporary/PreAtArc/PreAt016Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At016Dat_Fr.dac", "Temporary/PreAtArc/PreAt016Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At016Dat_Ge.dac", "Temporary/PreAtArc/PreAt016Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At016Dat_It.dac", "Temporary/PreAtArc/PreAt016Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At016Dat_Sp.dac", "Temporary/PreAtArc/PreAt016Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    configs.append(attraction16)

    attraction3 = FilePatchConfig(
        file_id="attraction_info3_venusaur",
        description="Venusaur Minigame Attraction",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At003Dat.dac", "Temporary/PreAtArc/PreAt003Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At003Dat_Fr.dac", "Temporary/PreAtArc/PreAt003Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At003Dat_Ge.dac", "Temporary/PreAtArc/PreAt003Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At003Dat_It.dac", "Temporary/PreAtArc/PreAt003Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At003Dat_Sp.dac", "Temporary/PreAtArc/PreAt003Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    configs.append(attraction3)

    field_meadow_npc_script_config = FilePatchConfig(
        file_id="meadow_zone_main_npc_script",
        description="Field Script Main Randomization",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar01Zn01Dat.dac", "Temporary/Field/ParkAr01Zn01Dat.dan",
                     "Script/evAr01Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar01Zn01Dat_Fr.dac", "Temporary/Field/ParkAr01Zn01Dat_Fr.dan",
                        "Script/evAr01Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar01Zn01Dat_Ge.dac", "Temporary/Field/ParkAr01Zn01Dat_Ge.dan",
                        "Script/evAr01Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn01Dat_It.dac", "Temporary/Field/ParkAr01Zn01Dat_It.dan",
                        "Script/evAr01Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn01Dat_Sp.dac", "Temporary/Field/ParkAr01Zn01Dat_Sp.dan",
                        "Script/evAr01Zn01_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr01Zn01_Npc_Main_patch_pattern
    )
    configs.append(field_meadow_npc_script_config)

    main_dol = FilePatchConfig(
        file_id="main_dol",
        description="main dol",
        processing_type=FileProcessingType.MAIN_DOL,
        file_group=[("DATA/sys/main.dol", "", "")],
        patch_patterns=main_dol_pattern
    )

    configs.append(main_dol)

    evAr01Zn01_Gimmic = FilePatchConfig(
        file_id="ar01zn01_gimmic",
        description="",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar01Zn01Dat.dac", "Temporary/Field/ParkAr01Zn01Dat.dan",
                     "Script/evAr01Zn01_Gimmic.fsb"), (
                        "DATA/files/Field/Ar01Zn01Dat_Fr.dac", "Temporary/Field/ParkAr01Zn01Dat_Fr.dan",
                        "Script/evAr01Zn01_Gimmic.fsb"), (
                        "DATA/files/Field/Ar01Zn01Dat_Ge.dac", "Temporary/Field/ParkAr01Zn01Dat_Ge.dan",
                        "Script/evAr01Zn01_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn01Dat_It.dac", "Temporary/Field/ParkAr01Zn01Dat_It.dan",
                        "Script/evAr01Zn01_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn01Dat_Sp.dac", "Temporary/Field/ParkAr01Zn01Dat_Sp.dan",
                        "Script/evAr01Zn01_Gimmic.fsb"),
                    ],
        patch_patterns=evAr01Zn01_Gimmic_patch_pattern
    )
    configs.append(evAr01Zn01_Gimmic)

    gk_gate101 = FilePatchConfig(
        file_id="gk_gate101",
        description="",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar01Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/Gk0101Gate.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0101Gate.fsb"), (
                        "DATA/files/Field/Ar01Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0101Gate.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0101Gate.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0101Gate.fsb"),
                    ],
        patch_patterns=[gate101_close]
    )
    configs.append(gk_gate101)
    return configs
