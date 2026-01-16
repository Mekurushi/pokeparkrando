from typing import List

from patcher.models.models import FilePatchConfig, FileProcessingType
from patcher.patterns.ScriptList_Ar04Zn02 import ScriptList_Ar04Zn02_patterns
from patcher.patterns.ScriptList_Ar06Zn01 import ScriptList_Ar06Zn01_patterns
from patcher.patterns.ScriptList_Ar99Zn01 import ScriptList_Ar99Zn01_patterns
from patcher.patterns.disposition_drifblim import disposition_drifblim_patterns
from patcher.patterns.evAr01Zn01_Gimmic import evAr01Zn01_Gimmic_patch_pattern
from patcher.patterns.evAr01Zn01_Npc_Main import \
    evAr01Zn01_Npc_Main_patch_pattern
from patcher.patterns.evAr01Zn01_ScriptEvent import evAr01Zn01_ScriptEvent_patch_pattern
from patcher.patterns.evAr01Zn02_Npc_Main import evAr01Zn02_Npc_Main_patterns
from patcher.patterns.evAr01Zn02_ScriptEvent import evAr01Zn02_ScriptEvent_patch_pattern
from patcher.patterns.evAr02Zn01_Npc_Main import evAr02Zn01_Npc_Main_pattern
from patcher.patterns.evAr02Zn01_ScriptEvent import evAr02Zn01_ScriptEvent_patch_pattern
from patcher.patterns.evAr03Zn01_Gimmic import evAr03Zn01_Gimmic_patch_pattern
from patcher.patterns.evAr03Zn01_Npc_Main import evAr03Zn01_Npc_Main_pattern
from patcher.patterns.evAr03Zn01_ScriptEvent import evAr03Zn01_ScriptEvent_patch_pattern
from patcher.patterns.evAr03Zn02_Gimmic import evAr03Zn02_Gimmic_patch_pattern
from patcher.patterns.evAr03Zn02_Npc_Main import evAr03Zn02_Npc_Main_patterns
from patcher.patterns.evAr03Zn02_ScriptEvent import evAr03Zn02_ScriptEvent_patch_pattern
from patcher.patterns.evAr03Zn03_Npc_Main import evAr03Zn03_Npc_Main_patterns
from patcher.patterns.evAr03Zn03_ScriptEvent import evAr03Zn03_ScriptEvent_patch_pattern
from patcher.patterns.evAr04Zn01_DemoEvent import evAr04Zn01_DemoEvent_patch_pattern
from patcher.patterns.evAr04Zn01_Gimmic import evAr04Zn01_Gimmic_patterns
from patcher.patterns.evAr04Zn01_Npc_Main import evAr04Zn01_Npc_Main_patterns
from patcher.patterns.evAr04Zn01_ScriptEvent import evAr04Zn01_ScriptEvent_patch_pattern
from patcher.patterns.evAr04Zn02_DemoEvent import evAr04Zn02_DemoEvent_patch_pattern
from patcher.patterns.evAr04Zn02_Gimmic import evAr04Zn02_Gimmic_patterns
from patcher.patterns.evAr04Zn02_Npc_Main import evAr04Zn02_Npc_Main_patterns
from patcher.patterns.evAr04Zn02_ScriptEvent import evAr04Zn02_ScriptEvent_patch_pattern
from patcher.patterns.evAr04Zn03_Npc_Main import evAr04Zn03_Npc_Main_patterns
from patcher.patterns.evAr04Zn03_ScriptEvent import evAr04Zn03_ScriptEvent_patch_pattern
from patcher.patterns.evAr05Zn01_Gimmic import evAr05Zn01_Gimmic_patterns
from patcher.patterns.evAr05Zn01_Npc_Main import evAr05Zn01_Npc_Main_patterns
from patcher.patterns.evAr05Zn01_ScriptEvent import evAr05Zn01_ScriptEvent_patch_pattern
from patcher.patterns.evAr05Zn02_Gimmic import evAr05Zn02_Gimmic_patterns
from patcher.patterns.evAr05Zn02_Npc_Main import evAr05Zn02_Npc_Main_patterns
from patcher.patterns.evAr05Zn02_ScriptEvent import evAr05Zn02_ScriptEvent_patch_pattern
from patcher.patterns.evAr05Zn03_Npc_Main import evAr05Zn03_Npc_Main_patterns
from patcher.patterns.evAr05Zn03_ScriptEvent import evAr05Zn03_ScriptEvent_patch_pattern
from patcher.patterns.evAr06Zn01_DemoEvent import evAr06Zn01_DemoEvent_patterns
from patcher.patterns.evAr06Zn01_Gimmic import evAr06Zn01_Gimmic_patterns
from patcher.patterns.evAr06Zn01_Npc_Main import evAr06Zn01_Npc_Main_patterns
from patcher.patterns.evAr06Zn01_ScriptEvent import evAr06Zn01_ScriptEvent_patch_pattern
from patcher.patterns.evAr06Zn02_Gimmic import evAr06Zn02_Gimmic_patch_pattern
from patcher.patterns.evAr06Zn02_Npc_Main import evAr06Zn02_Npc_Main_patterns
from patcher.patterns.evAr06Zn02_ScriptEvent import evAr06Zn02_ScriptEvent_patch_pattern
from patcher.patterns.evAr07Zn01_Npc_Main import evAr07Zn01_Npc_Main_patterns
from patcher.patterns.evAr99Zn01_Npc_Main import evAr99Zn01_Npc_Main_pattern
from patcher.patterns.evAr99Zn01_ScriptEvent import evAr99Zn01_ScriptEvent_patch_pattern
from patcher.patterns.gk0101Gate import gate101_close
from patcher.patterns.gk0302Gate import gk0302Gate_pattern
from patcher.patterns.gk0402Bridge import gk0402Bridge_pattern
from patcher.patterns.gk0402Gate import gk0402Gate_pattern
from patcher.patterns.gk0402Switch import gk0402Switch_pattern
from patcher.patterns.gk0501GateA import gk0501Gate_pattern
from patcher.patterns.gk0502DoorB import gk0502DoorB_pattern
from patcher.patterns.gk0502DoorC import gk0502DoorC_pattern
from patcher.patterns.gk0502DoorD import gk0502DoorD_pattern
from patcher.patterns.gk0502DoorE import gk0502DoorE_pattern
from patcher.patterns.gk0601DoorB import gk0601DoorB_pattern
from patcher.patterns.gk0601SwitchB import gk0601SwitchB_pattern
from patcher.patterns.gkBookShelf import gkBookShelf_pattern
from patcher.patterns.gkFireWallB import gkFireWall_pattern
from patcher.patterns.gkFireWallC import gkFireWallC_pattern
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
from patcher.patterns.mnStartMenu import load_new_file_pattern, start_menu_pattern
from patcher.patterns.treehouse import treehouse_pattern


def get_meadow_zone_patches() -> List[FilePatchConfig]:
    patches = []
    ar01zn01Disposition = FilePatchConfig(
        file_id="disposition_ar01zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.DAC_U8,
        file_group=[("DATA/files/Field/Ar01Zn01Dat.dac", "unused",
                     "Field/Ar01/Zn01/Ar01Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar01Zn01Dat_Fr.dac", "unused",
                     "Field/Ar01/Zn01/Ar01Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar01Zn01Dat_Ge.dac", "unused",
                     "Field/Ar01/Zn01/Ar01Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar01Zn01Dat_It.dac", "unused",
                     "Field/Ar01/Zn01/Ar01Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar01Zn01Dat_Sp.dac", "unused",
                     "Field/Ar01/Zn01/Ar01Zn01Dp00.rlb"),
                    ],
        patch_patterns=disposition_drifblim_patterns
    )
    patches.append(ar01zn01Disposition)

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
    patches.append(field_Ar01Zn02_npc_script_config)

    field_Ar01Zn02_script_event_config = FilePatchConfig(
        file_id="Ar01_Zn02_script_event",
        description="Zonechanges logic",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar01Zn02Dat.dac", "Temporary/Field/ParkAr01Zn02Dat.dan",
                     "Script/evAr01Zn02_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar01Zn02Dat_Fr.dac", "Temporary/Field/ParkAr01Zn02Dat_Fr.dan",
                        "Script/evAr01Zn02_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar01Zn02Dat_Ge.dac", "Temporary/Field/ParkAr01Zn02Dat_Ge.dan",
                        "Script/evAr01Zn02_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn02Dat_It.dac", "Temporary/Field/ParkAr01Zn02Dat_It.dan",
                        "Script/evAr01Zn02_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn02Dat_Sp.dac", "Temporary/Field/ParkAr01Zn02Dat_Sp.dan",
                        "Script/evAr01Zn02_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr01Zn02_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar01Zn02_script_event_config)

    field_Ar01Zn01_script_event_config = FilePatchConfig(
        file_id="Ar01_Zn01_script_event",
        description="Zonechanges logic",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar01Zn01Dat.dac", "Temporary/Field/ParkAr01Zn01Dat.dan",
                     "Script/evAr01Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar01Zn01Dat_Fr.dac", "Temporary/Field/ParkAr01Zn01Dat_Fr.dan",
                        "Script/evAr01Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar01Zn01Dat_Ge.dac", "Temporary/Field/ParkAr01Zn01Dat_Ge.dan",
                        "Script/evAr01Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn01Dat_It.dac", "Temporary/Field/ParkAr01Zn01Dat_It.dan",
                        "Script/evAr01Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar01Zn01Dat_Sp.dac", "Temporary/Field/ParkAr01Zn01Dat_Sp.dan",
                        "Script/evAr01Zn01_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr01Zn01_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar01Zn01_script_event_config)

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
    patches.append(field_gimmic_shroomish_crate)

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
    patches.append(field_meadow_npc_script_config)

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
    patches.append(evAr01Zn01_Gimmic)

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
    patches.append(gk_gate101)

    return patches


def get_park_entrance_patches() -> List[FilePatchConfig]:
    patches = []
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
    patches.append(field_Ar99Zn01_npc_script_config)
    field_Ar99Zn01_script_event_config = FilePatchConfig(
        file_id="Ar99_Zn01_script_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar99Zn01Dat.dac", "Temporary/Field/ParkAr99Zn01Dat.dan",
                     "Script/evAr99Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar99Zn01Dat_Fr.dac", "Temporary/Field/ParkAr99Zn01Dat_Fr.dan",
                        "Script/evAr99Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar99Zn01Dat_Ge.dac", "Temporary/Field/ParkAr99Zn01Dat_Ge.dan",
                        "Script/evAr99Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar99Zn01Dat_It.dac", "Temporary/Field/ParkAr99Zn01Dat_It.dan",
                        "Script/evAr99Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar99Zn01Dat_Sp.dac", "Temporary/Field/ParkAr99Zn01Dat_Sp.dan",
                        "Script/evAr99Zn01_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr99Zn01_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar99Zn01_script_event_config)
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
    patches.append(kabigon_wall)
    return patches


def get_attraction_patches() -> List[FilePatchConfig]:
    patches = []

    lobby1 = FilePatchConfig(
        file_id="lobby1",
        description="Attraction Lobby 1",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby01Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby01Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby01Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby01Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby01Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    patches.append(lobby1)

    lobby2 = FilePatchConfig(
        file_id="lobby2",
        description="Attraction Lobby 2",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby02Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby02Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby02Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby02Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby02Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    patches.append(lobby2)

    lobby3 = FilePatchConfig(
        file_id="lobby3_venusaur",
        description="Venusaur Attraction Lobby",
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
    patches.append(lobby3)

    lobby4 = FilePatchConfig(
        file_id="lobby4",
        description="Attraction Lobby 4",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby04Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby04Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby04Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby04Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby04Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    patches.append(lobby4)

    lobby5 = FilePatchConfig(
        file_id="lobby5",
        description="Attraction Lobby 5",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby05Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby05Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby05Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby05Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby05Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    patches.append(lobby5)

    lobby6 = FilePatchConfig(
        file_id="lobby6",
        description="Attraction Lobby 6",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby06Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby06Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby06Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby06Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby06Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    patches.append(lobby6)

    lobby7 = FilePatchConfig(
        file_id="lobby7",
        description="Attraction Lobby 7",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby07Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby07Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby07Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby07Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby07Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    patches.append(lobby7)

    lobby9 = FilePatchConfig(
        file_id="lobby9",
        description="Attraction Lobby 9",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby09Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby09Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby09Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby09Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby09Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    patches.append(lobby9)

    lobby10 = FilePatchConfig(
        file_id="lobby10",
        description="Attraction Lobby 10",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby10Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby10Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby10Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby10Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby10Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    patches.append(lobby10)

    lobby11 = FilePatchConfig(
        file_id="lobby11",
        description="Attraction Lobby 11",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby11Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby11Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby11Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby11Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby11Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    patches.append(lobby11)

    lobby12 = FilePatchConfig(
        file_id="lobby12",
        description="Attraction Lobby 12",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby12Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby12Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby12Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby12Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby12Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    patches.append(lobby12)

    lobby13 = FilePatchConfig(
        file_id="lobby13",
        description="Attraction Lobby 13",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby13Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby13Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby13Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby13Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby13Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    patches.append(lobby13)

    lobby15 = FilePatchConfig(
        file_id="lobby15",
        description="Attraction Lobby 15",
        processing_type=FileProcessingType.DAC_U8,

        file_group=[("DATA/files/Archive/lobby15Dat.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby15Dat_Fr.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby15Dat_Ge.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby15Dat_It.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ("DATA/files/Archive/lobby15Dat_Sp.dac", "unused",
                     "Script/mnLobby.fsb"),
                    ],
        patch_patterns=mnLobby_pattern
    )
    patches.append(lobby15)

    lobby16 = FilePatchConfig(
        file_id="lobby16_bulbasaur",
        description="Bulbasaur Attraction Lobby",
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
    patches.append(lobby16)

    attraction1 = FilePatchConfig(
        file_id="attraction_info1",
        description="Attraction 1",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At001Dat.dac", "Temporary/PreAtArc/PreAt001Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At001Dat_Fr.dac", "Temporary/PreAtArc/PreAt001Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At001Dat_Ge.dac", "Temporary/PreAtArc/PreAt001Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At001Dat_It.dac", "Temporary/PreAtArc/PreAt001Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At001Dat_Sp.dac", "Temporary/PreAtArc/PreAt001Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    patches.append(attraction1)

    attraction2 = FilePatchConfig(
        file_id="attraction_info2",
        description="Attraction 2",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At002Dat.dac", "Temporary/PreAtArc/PreAt002Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At002Dat_Fr.dac", "Temporary/PreAtArc/PreAt002Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At002Dat_Ge.dac", "Temporary/PreAtArc/PreAt002Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At002Dat_It.dac", "Temporary/PreAtArc/PreAt002Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At002Dat_Sp.dac", "Temporary/PreAtArc/PreAt002Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    patches.append(attraction2)

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
    patches.append(attraction3)

    attraction4 = FilePatchConfig(
        file_id="attraction_info4",
        description="Attraction 4",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At004Dat.dac", "Temporary/PreAtArc/PreAt004Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At004Dat_Fr.dac", "Temporary/PreAtArc/PreAt004Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At004Dat_Ge.dac", "Temporary/PreAtArc/PreAt004Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At004Dat_It.dac", "Temporary/PreAtArc/PreAt004Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At004Dat_Sp.dac", "Temporary/PreAtArc/PreAt004Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    patches.append(attraction4)

    attraction5 = FilePatchConfig(
        file_id="attraction_info5",
        description="Attraction 5",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At005Dat.dac", "Temporary/PreAtArc/PreAt005Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At005Dat_Fr.dac", "Temporary/PreAtArc/PreAt005Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At005Dat_Ge.dac", "Temporary/PreAtArc/PreAt005Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At005Dat_It.dac", "Temporary/PreAtArc/PreAt005Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At005Dat_Sp.dac", "Temporary/PreAtArc/PreAt005Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    patches.append(attraction5)

    attraction6 = FilePatchConfig(
        file_id="attraction_info6",
        description="Attraction 6",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At006Dat.dac", "Temporary/PreAtArc/PreAt006Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At006Dat_Fr.dac", "Temporary/PreAtArc/PreAt006Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At006Dat_Ge.dac", "Temporary/PreAtArc/PreAt006Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At006Dat_It.dac", "Temporary/PreAtArc/PreAt006Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At006Dat_Sp.dac", "Temporary/PreAtArc/PreAt006Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    patches.append(attraction6)

    attraction7 = FilePatchConfig(
        file_id="attraction_info7",
        description="Attraction 7",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At007Dat.dac", "Temporary/PreAtArc/PreAt007Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At007Dat_Fr.dac", "Temporary/PreAtArc/PreAt007Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At007Dat_Ge.dac", "Temporary/PreAtArc/PreAt007Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At007Dat_It.dac", "Temporary/PreAtArc/PreAt007Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At007Dat_Sp.dac", "Temporary/PreAtArc/PreAt007Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    patches.append(attraction7)

    attraction9 = FilePatchConfig(
        file_id="attraction_info9",
        description="Attraction 9",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At009Dat.dac", "Temporary/PreAtArc/PreAt009Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At009Dat_Fr.dac", "Temporary/PreAtArc/PreAt009Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At009Dat_Ge.dac", "Temporary/PreAtArc/PreAt009Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At009Dat_It.dac", "Temporary/PreAtArc/PreAt009Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At009Dat_Sp.dac", "Temporary/PreAtArc/PreAt009Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    patches.append(attraction9)

    attraction10 = FilePatchConfig(
        file_id="attraction_info10",
        description="Attraction 10",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At010Dat.dac", "Temporary/PreAtArc/PreAt010Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At010Dat_Fr.dac", "Temporary/PreAtArc/PreAt010Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At010Dat_Ge.dac", "Temporary/PreAtArc/PreAt010Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At010Dat_It.dac", "Temporary/PreAtArc/PreAt010Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At010Dat_Sp.dac", "Temporary/PreAtArc/PreAt010Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    patches.append(attraction10)

    attraction11 = FilePatchConfig(
        file_id="attraction_info11",
        description="Attraction 11",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At011Dat.dac", "Temporary/PreAtArc/PreAt011Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At011Dat_Fr.dac", "Temporary/PreAtArc/PreAt011Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At011Dat_Ge.dac", "Temporary/PreAtArc/PreAt011Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At011Dat_It.dac", "Temporary/PreAtArc/PreAt011Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At011Dat_Sp.dac", "Temporary/PreAtArc/PreAt011Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    patches.append(attraction11)

    attraction12 = FilePatchConfig(
        file_id="attraction_info12",
        description="Attraction 12",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At012Dat.dac", "Temporary/PreAtArc/PreAt012Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At012Dat_Fr.dac", "Temporary/PreAtArc/PreAt012Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At012Dat_Ge.dac", "Temporary/PreAtArc/PreAt012Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At012Dat_It.dac", "Temporary/PreAtArc/PreAt012Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At012Dat_Sp.dac", "Temporary/PreAtArc/PreAt012Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    patches.append(attraction12)

    attraction13 = FilePatchConfig(
        file_id="attraction_info13",
        description="Attraction 13",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At013Dat.dac", "Temporary/PreAtArc/PreAt013Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At013Dat_Fr.dac", "Temporary/PreAtArc/PreAt013Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At013Dat_Ge.dac", "Temporary/PreAtArc/PreAt013Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At013Dat_It.dac", "Temporary/PreAtArc/PreAt013Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At013Dat_Sp.dac", "Temporary/PreAtArc/PreAt013Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    patches.append(attraction13)

    attraction15 = FilePatchConfig(
        file_id="attraction_info15",
        description="Attraction 15",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Attraction/At015Dat.dac", "Temporary/PreAtArc/PreAt015Dat.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At015Dat_Fr.dac", "Temporary/PreAtArc/PreAt015Dat_Fr.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At015Dat_Ge.dac", "Temporary/PreAtArc/PreAt015Dat_Ge.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At015Dat_It.dac", "Temporary/PreAtArc/PreAt015Dat_It.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ("DATA/files/Attraction/At015Dat_Sp.dac", "Temporary/PreAtArc/PreAt015Dat_Sp.dan",
                     "Script/mnAttractionInfo.fsb"),
                    ],
        patch_patterns=mnAttractionInfo_pattern
    )
    patches.append(attraction15)

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
    patches.append(attraction16)

    return patches


def get_treehouse_patches() -> List[FilePatchConfig]:
    patches = []
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
    patches.append(field_Ar02Zn01_npc_script_config)
    field_Ar02Zn01_script_event_config = FilePatchConfig(
        file_id="Ar02_Zn01_script_event",
        description="Zonechanges logic",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar02Zn01Dat.dac", "Temporary/Field/ParkAr02Zn01Dat.dan",
                     "Script/evAr02Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar02Zn01Dat_Fr.dac", "Temporary/Field/ParkAr02Zn01Dat_Fr.dan",
                        "Script/evAr02Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar02Zn01Dat_Ge.dac", "Temporary/Field/ParkAr02Zn01Dat_Ge.dan",
                        "Script/evAr02Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar02Zn01Dat_It.dac", "Temporary/Field/ParkAr02Zn01Dat_It.dan",
                        "Script/evAr02Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar02Zn01Dat_Sp.dac", "Temporary/Field/ParkAr02Zn01Dat_Sp.dan",
                        "Script/evAr02Zn01_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr02Zn01_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar02Zn01_script_event_config)

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
    patches.append(treehouse)
    return patches


def get_beach_zone_patches() -> List[FilePatchConfig]:
    patches = []
    ar03zn01Disposition = FilePatchConfig(
        file_id="disposition_ar03zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.DAC_U8,
        file_group=[("DATA/files/Field/Ar03Zn01Dat.dac", "unused",
                     "Field/Ar03/Zn01/Ar03Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar03Zn01Dat_Fr.dac", "unused",
                     "Field/Ar03/Zn01/Ar03Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar03Zn01Dat_Ge.dac", "unused",
                     "Field/Ar03/Zn01/Ar03Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar03Zn01Dat_It.dac", "unused",
                     "Field/Ar03/Zn01/Ar03Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar03Zn01Dat_Sp.dac", "unused",
                     "Field/Ar03/Zn01/Ar03Zn01Dp00.rlb"),
                    ],
        patch_patterns=disposition_drifblim_patterns
    )
    patches.append(ar03zn01Disposition)

    evAr03Zn01_Gimmic = FilePatchConfig(
        file_id="ar03zn01_gimmic",
        description="",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar03Zn01Dat.dac", "Temporary/Field/ParkAr03Zn01Dat.dan",
                     "Script/evAr03Zn01_Gimmic.fsb"), (
                        "DATA/files/Field/Ar03Zn01Dat_Fr.dac", "Temporary/Field/ParkAr03Zn01Dat_Fr.dan",
                        "Script/evAr03Zn01_Gimmic.fsb"), (
                        "DATA/files/Field/Ar03Zn01Dat_Ge.dac", "Temporary/Field/ParkAr03Zn01Dat_Ge.dan",
                        "Script/evAr03Zn01_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_It.dac", "Temporary/Field/ParkAr03Zn01Dat_It.dan",
                        "Script/evAr03Zn01_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Sp.dac", "Temporary/Field/ParkAr03Zn01Dat_Sp.dan",
                        "Script/evAr03Zn01_Gimmic.fsb"),
                    ],
        patch_patterns=evAr03Zn01_Gimmic_patch_pattern
    )
    patches.append(evAr03Zn01_Gimmic)

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
    patches.append(rockB)

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
    patches.append(recycleSanbasiA)

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
    patches.append(recycleSanbasiB)

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
    patches.append(recycleSanbasiC)

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
    patches.append(recycleSanbasiD)

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
    patches.append(field_Ar03Zn01_npc_script_config)

    field_Ar03Zn01_script_event_config = FilePatchConfig(
        file_id="Ar03_Zn01_script_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar03Zn01Dat.dac", "Temporary/Field/ParkAr03Zn01Dat.dan",
                     "Script/evAr03Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar03Zn01Dat_Fr.dac", "Temporary/Field/ParkAr03Zn01Dat_Fr.dan",
                        "Script/evAr03Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar03Zn01Dat_Ge.dac", "Temporary/Field/ParkAr03Zn01Dat_Ge.dan",
                        "Script/evAr03Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_It.dac", "Temporary/Field/ParkAr03Zn01Dat_It.dan",
                        "Script/evAr03Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn01Dat_Sp.dac", "Temporary/Field/ParkAr03Zn01Dat_Sp.dan",
                        "Script/evAr03Zn01_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr03Zn01_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar03Zn01_script_event_config)

    attraction_ranking = FilePatchConfig(
        file_id="attraction_prep",
        description="unlock unused attraction records",
        processing_type=FileProcessingType.DacCopyFilePatcher,
        file_group=[("DATA/files/Archive/PrepareSceneDat.dac", "Global/Attraction/AttractionRanking16.rlb",
                     "Global/Attraction/AttractionRanking08.rlb"),
                    ("DATA/files/Archive/PrepareSceneDat.dac", "Global/Attraction/AttractionRanking16.rlb",
                     "Global/Attraction/AttractionRanking14.rlb"),
                    ],
    )
    patches.append(attraction_ranking)

    return patches


def get_ice_zone_patches() -> List[FilePatchConfig]:
    patches = []

    ar03zn02Disposition = FilePatchConfig(
        file_id="disposition_ar03zn02",
        description="Field Script Main",
        processing_type=FileProcessingType.DAC_U8,
        file_group=[("DATA/files/Field/Ar03Zn02Dat.dac", "unused",
                     "Field/Ar03/Zn02/Ar03Zn02Dp00.rlb"),
                    ("DATA/files/Field/Ar03Zn02Dat_Fr.dac", "unused",
                     "Field/Ar03/Zn02/Ar03Zn02Dp00.rlb"),
                    ("DATA/files/Field/Ar03Zn02Dat_Ge.dac", "unused",
                     "Field/Ar03/Zn02/Ar03Zn02Dp00.rlb"),
                    ("DATA/files/Field/Ar03Zn02Dat_It.dac", "unused",
                     "Field/Ar03/Zn02/Ar03Zn02Dp00.rlb"),
                    ("DATA/files/Field/Ar03Zn02Dat_Sp.dac", "unused",
                     "Field/Ar03/Zn02/Ar03Zn02Dp00.rlb"),
                    ],
        patch_patterns=disposition_drifblim_patterns
    )
    patches.append(ar03zn02Disposition)

    evAr03Zn02_Gimmic = FilePatchConfig(
        file_id="ar03zn02_gimmic",
        description="",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar03Zn02Dat.dac", "Temporary/Field/ParkAr03Zn02Dat.dan",
                     "Script/evAr03Zn02_Gimmic.fsb"), (
                        "DATA/files/Field/Ar03Zn02Dat_Fr.dac", "Temporary/Field/ParkAr03Zn02Dat_Fr.dan",
                        "Script/evAr03Zn02_Gimmic.fsb"), (
                        "DATA/files/Field/Ar03Zn02Dat_Ge.dac", "Temporary/Field/ParkAr03Zn02Dat_Ge.dan",
                        "Script/evAr03Zn02_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn02Dat_It.dac", "Temporary/Field/ParkAr03Zn02Dat_It.dan",
                        "Script/evAr03Zn02_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn02Dat_Sp.dac", "Temporary/Field/ParkAr03Zn02Dat_Sp.dan",
                        "Script/evAr03Zn02_Gimmic.fsb"),
                    ],
        patch_patterns=evAr03Zn02_Gimmic_patch_pattern
    )
    patches.append(evAr03Zn02_Gimmic)

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
    patches.append(field_Ar03Zn03_npc_script_config)

    field_Ar03Zn03_script_event_config = FilePatchConfig(
        file_id="Ar03_Zn03_script_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar03Zn03Dat.dac", "Temporary/Field/ParkAr03Zn03Dat.dan",
                     "Script/evAr03Zn03_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar03Zn03Dat_Fr.dac", "Temporary/Field/ParkAr03Zn03Dat_Fr.dan",
                        "Script/evAr03Zn03_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar03Zn03Dat_Ge.dac", "Temporary/Field/ParkAr03Zn03Dat_Ge.dan",
                        "Script/evAr03Zn03_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn03Dat_It.dac", "Temporary/Field/ParkAr03Zn03Dat_It.dan",
                        "Script/evAr03Zn03_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn03Dat_Sp.dac", "Temporary/Field/ParkAr03Zn03Dat_Sp.dan",
                        "Script/evAr03Zn03_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr03Zn03_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar03Zn03_script_event_config)

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
    patches.append(gkmammoo)

    gk0302gate = FilePatchConfig(
        file_id="gate0302_gimmic",
        description="Empoleon Gate Ice Zone",
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
    patches.append(gk0302gate)

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
    patches.append(field_Ar03Zn02_npc_script_config)

    field_Ar03Zn02_script_event_config = FilePatchConfig(
        file_id="Ar03_Zn02_script_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar03Zn02Dat.dac", "Temporary/Field/ParkAr03Zn02Dat.dan",
                     "Script/evAr03Zn02_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar03Zn02Dat_Fr.dac", "Temporary/Field/ParkAr03Zn02Dat_Fr.dan",
                        "Script/evAr03Zn02_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar03Zn02Dat_Ge.dac", "Temporary/Field/ParkAr03Zn02Dat_Ge.dan",
                        "Script/evAr03Zn02_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn02Dat_It.dac", "Temporary/Field/ParkAr03Zn02Dat_It.dan",
                        "Script/evAr03Zn02_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar03Zn02Dat_Sp.dac", "Temporary/Field/ParkAr03Zn02Dat_Sp.dan",
                        "Script/evAr03Zn02_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr03Zn02_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar03Zn02_script_event_config)
    return patches


def get_cavern_zone_patches() -> List[FilePatchConfig]:
    patches = []
    ar04zn01Disposition = FilePatchConfig(
        file_id="disposition_ar04zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn01Dat.dac", "unused",
                     "Field/Ar04/Zn01/Ar04Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar04Zn01Dat_Fr.dac", "unused",
                     "Field/Ar04/Zn01/Ar04Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar04Zn01Dat_Ge.dac", "unused",
                     "Field/Ar04/Zn01/Ar04Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar04Zn01Dat_It.dac", "unused",
                     "Field/Ar04/Zn01/Ar04Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar04Zn01Dat_Sp.dac", "unused",
                     "Field/Ar04/Zn01/Ar04Zn01Dp00.rlb"),
                    ],
        patch_patterns=disposition_drifblim_patterns
    )
    patches.append(ar04zn01Disposition)

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
    patches.append(field_Ar04Zn01_gimmic_config)

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
    patches.append(field_Ar04Zn01_npc_script_config)

    field_Ar04Zn01_script_event_config = FilePatchConfig(
        file_id="Ar04_Zn01_script_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn01Dat.dac", "Temporary/Field/ParkAr04Zn01Dat.dan",
                     "Script/evAr04Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar04Zn01Dat_Fr.dac", "Temporary/Field/ParkAr04Zn01Dat_Fr.dan",
                        "Script/evAr04Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar04Zn01Dat_Ge.dac", "Temporary/Field/ParkAr04Zn01Dat_Ge.dan",
                        "Script/evAr04Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn01Dat_It.dac", "Temporary/Field/ParkAr04Zn01Dat_It.dan",
                        "Script/evAr04Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn01Dat_Sp.dac", "Temporary/Field/ParkAr04Zn01Dat_Sp.dan",
                        "Script/evAr04Zn01_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr04Zn01_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar04Zn01_script_event_config)

    field_Ar04Zn01_demo_event_config = FilePatchConfig(
        file_id="Ar04_Zn01_demo_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn01Dat.dac", "Temporary/Field/ParkAr04Zn01Dat.dan",
                     "Script/evAr04Zn01_DemoEvent.fsb"), (
                        "DATA/files/Field/Ar04Zn01Dat_Fr.dac", "Temporary/Field/ParkAr04Zn01Dat_Fr.dan",
                        "Script/evAr04Zn01_DemoEvent.fsb"), (
                        "DATA/files/Field/Ar04Zn01Dat_Ge.dac", "Temporary/Field/ParkAr04Zn01Dat_Ge.dan",
                        "Script/evAr04Zn01_DemoEvent.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn01Dat_It.dac", "Temporary/Field/ParkAr04Zn01Dat_It.dan",
                        "Script/evAr04Zn01_DemoEvent.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn01Dat_Sp.dac", "Temporary/Field/ParkAr04Zn01Dat_Sp.dan",
                        "Script/evAr04Zn01_DemoEvent.fsb"),
                    ],
        patch_patterns=evAr04Zn01_DemoEvent_patch_pattern
    )
    patches.append(field_Ar04Zn01_demo_event_config)

    field_Ar04Zn02_demo_event_config = FilePatchConfig(
        file_id="Ar04_Zn02_demo_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn02Dat.dac", "Temporary/Field/ParkAr04Zn02Dat.dan",
                     "Script/evAr04Zn02_DemoEvent.fsb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Fr.dac", "Temporary/Field/ParkAr04Zn02Dat_Fr.dan",
                        "Script/evAr04Zn02_DemoEvent.fsb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Ge.dac", "Temporary/Field/ParkAr04Zn02Dat_Ge.dan",
                        "Script/evAr04Zn02_DemoEvent.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_It.dac", "Temporary/Field/ParkAr04Zn02Dat_It.dan",
                        "Script/evAr04Zn02_DemoEvent.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Sp.dac", "Temporary/Field/ParkAr04Zn02Dat_Sp.dan",
                        "Script/evAr04Zn02_DemoEvent.fsb"),
                    ],
        patch_patterns=evAr04Zn02_DemoEvent_patch_pattern
    )
    patches.append(field_Ar04Zn02_demo_event_config)
    return patches


def get_magma_zone_patches() -> List[FilePatchConfig]:
    patches = []
    ar04zn02Disposition = FilePatchConfig(
        file_id="disposition_ar04zn02",
        description="Field Script Main",
        processing_type=FileProcessingType.DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn02Dat.dac", "unused",
                     "Field/Ar04/Zn02/Ar04Zn02Dp00.rlb"),
                    ("DATA/files/Field/Ar04Zn02Dat_Fr.dac", "unused",
                     "Field/Ar04/Zn02/Ar04Zn02Dp00.rlb"),
                    ("DATA/files/Field/Ar04Zn02Dat_Ge.dac", "unused",
                     "Field/Ar04/Zn02/Ar04Zn02Dp00.rlb"),
                    ("DATA/files/Field/Ar04Zn02Dat_It.dac", "unused",
                     "Field/Ar04/Zn02/Ar04Zn02Dp00.rlb"),
                    ("DATA/files/Field/Ar04Zn02Dat_Sp.dac", "unused",
                     "Field/Ar04/Zn02/Ar04Zn02Dp00.rlb"),
                    ],
        patch_patterns=disposition_drifblim_patterns
    )
    patches.append(ar04zn02Disposition)

    field_Ar04Zn02_npc_script_config = FilePatchConfig(
        file_id="Ar04_Zn02",
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
    patches.append(field_Ar04Zn02_npc_script_config)

    field_Ar04Zn02_script_event_config = FilePatchConfig(
        file_id="Ar04_Zn02_script_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn02Dat.dac", "Temporary/Field/ParkAr04Zn02Dat.dan",
                     "Script/evAr04Zn02_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Fr.dac", "Temporary/Field/ParkAr04Zn02Dat_Fr.dan",
                        "Script/evAr04Zn02_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Ge.dac", "Temporary/Field/ParkAr04Zn02Dat_Ge.dan",
                        "Script/evAr04Zn02_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_It.dac", "Temporary/Field/ParkAr04Zn02Dat_It.dan",
                        "Script/evAr04Zn02_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Sp.dac", "Temporary/Field/ParkAr04Zn02Dat_Sp.dan",
                        "Script/evAr04Zn02_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr04Zn02_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar04Zn02_script_event_config)

    field_Ar04Zn03_npc_script_config = FilePatchConfig(
        file_id="Ar04_Zn03",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn03Dat.dac", "Temporary/Field/ParkAr04Zn03Dat.dan",
                     "Script/evAr04Zn03_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar04Zn03Dat_Fr.dac", "Temporary/Field/ParkAr04Zn03Dat_Fr.dan",
                        "Script/evAr04Zn03_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar04Zn03Dat_Ge.dac", "Temporary/Field/ParkAr04Zn03Dat_Ge.dan",
                        "Script/evAr04Zn03_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn03Dat_It.dac", "Temporary/Field/ParkAr04Zn03Dat_It.dan",
                        "Script/evAr04Zn03_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn03Dat_Sp.dac", "Temporary/Field/ParkAr04Zn03Dat_Sp.dan",
                        "Script/evAr04Zn03_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr04Zn03_Npc_Main_patterns
    )
    patches.append(field_Ar04Zn03_npc_script_config)

    field_Ar04Zn03_script_event_config = FilePatchConfig(
        file_id="Ar04_Zn03_script_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn03Dat.dac", "Temporary/Field/ParkAr04Zn03Dat.dan",
                     "Script/evAr04Zn03_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar04Zn03Dat_Fr.dac", "Temporary/Field/ParkAr04Zn03Dat_Fr.dan",
                        "Script/evAr04Zn03_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar04Zn03Dat_Ge.dac", "Temporary/Field/ParkAr04Zn03Dat_Ge.dan",
                        "Script/evAr04Zn03_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn03Dat_It.dac", "Temporary/Field/ParkAr04Zn03Dat_It.dan",
                        "Script/evAr04Zn03_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn03Dat_Sp.dac", "Temporary/Field/ParkAr04Zn03Dat_Sp.dan",
                        "Script/evAr04Zn03_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr04Zn03_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar04Zn03_script_event_config)

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
    patches.append(gk0402gate)

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
    patches.append(gk0402bridge)

    gk0402switch = FilePatchConfig(
        file_id="switch0402_gimmic",
        description="Blaziken Bridge Switch",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar04Zn02Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/Gk0402Switch.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0402Switch.fsb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0402Switch.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0402Switch.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0402Switch.fsb"),
                    ],
        patch_patterns=gk0402Switch_pattern
    )
    patches.append(gk0402switch)

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
    patches.append(firewall_b)

    field_Ar04Zn02_gimmic_config = FilePatchConfig(
        file_id="Ar04_Zn02_gimmic",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn02Dat.dac", "Temporary/Field/ParkAr04Zn02Dat.dan",
                     "Script/evAr04Zn02_Gimmic.fsb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Fr.dac", "Temporary/Field/ParkAr04Zn02Dat_Fr.dan",
                        "Script/evAr04Zn02_Gimmic.fsb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Ge.dac", "Temporary/Field/ParkAr04Zn02Dat_Ge.dan",
                        "Script/evAr04Zn02_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_It.dac", "Temporary/Field/ParkAr04Zn02Dat_It.dan",
                        "Script/evAr04Zn02_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Sp.dac", "Temporary/Field/ParkAr04Zn02Dat_Sp.dan",
                        "Script/evAr04Zn02_Gimmic.fsb"),
                    ],
        patch_patterns=evAr04Zn02_Gimmic_patterns
    )
    patches.append(field_Ar04Zn02_gimmic_config)

    scriptList_Ar04Zn02 = FilePatchConfig(
        file_id="scriptList_Ar04Zn02",
        description="ScriptList from Ar04Zn02",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar04Zn02Dat.dac", "Temporary/Field/ParkAr04Zn02Dat.dan",
                     "Event/ScriptList/ScriptList_Ar04Zn02.rlb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Fr.dac", "Temporary/Field/ParkAr04Zn02Dat_Fr.dan",
                        "Event/ScriptList/ScriptList_Ar04Zn02.rlb"), (
                        "DATA/files/Field/Ar04Zn02Dat_Ge.dac", "Temporary/Field/ParkAr04Zn02Dat_Ge.dan",
                        "Event/ScriptList/ScriptList_Ar04Zn02.rlb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_It.dac", "Temporary/Field/ParkAr04Zn02Dat_It.dan",
                        "Event/ScriptList/ScriptList_Ar04Zn02.rlb"),
                    (
                        "DATA/files/Field/Ar04Zn02Dat_Sp.dac", "Temporary/Field/ParkAr04Zn02Dat_Sp.dan",
                        "Event/ScriptList/ScriptList_Ar04Zn02.rlb"),
                    ],
        patch_patterns=ScriptList_Ar04Zn02_patterns
    )
    patches.append(scriptList_Ar04Zn02)
    return patches


def get_haunted_zone_patches() -> List[FilePatchConfig]:
    patches = []
    ar05zn01Disposition = FilePatchConfig(
        file_id="disposition_ar05zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.DAC_U8,
        file_group=[("DATA/files/Field/Ar05Zn01Dat.dac", "unused",
                     "Field/Ar05/Zn01/Ar05Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar05Zn01Dat_Fr.dac", "unused",
                     "Field/Ar05/Zn01/Ar05Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar05Zn01Dat_Ge.dac", "unused",
                     "Field/Ar05/Zn01/Ar05Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar05Zn01Dat_It.dac", "unused",
                     "Field/Ar05/Zn01/Ar05Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar05Zn01Dat_Sp.dac", "unused",
                     "Field/Ar05/Zn01/Ar05Zn01Dp00.rlb"),
                    ],
        patch_patterns=disposition_drifblim_patterns
    )
    patches.append(ar05zn01Disposition)

    scriptList_Ar99Zn01 = FilePatchConfig(
        file_id="scriptList_Ar99Zn01",
        description="ScriptList fro Ar99Zn01",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar99Zn01Dat.dac", "Temporary/Field/ParkAr99Zn01Dat.dan",
                     "Event/ScriptList/ScriptList_Ar99Zn01.rlb"), (
                        "DATA/files/Field/Ar99Zn01Dat_Fr.dac", "Temporary/Field/ParkAr99Zn01Dat_Fr.dan",
                        "Event/ScriptList/ScriptList_Ar99Zn01.rlb"), (
                        "DATA/files/Field/Ar99Zn01Dat_Ge.dac", "Temporary/Field/ParkAr99Zn01Dat_Ge.dan",
                        "Event/ScriptList/ScriptList_Ar99Zn01.rlb"),
                    (
                        "DATA/files/Field/Ar99Zn01Dat_It.dac", "Temporary/Field/ParkAr99Zn01Dat_It.dan",
                        "Event/ScriptList/ScriptList_Ar99Zn01.rlb"),
                    (
                        "DATA/files/Field/Ar99Zn01Dat_Sp.dac", "Temporary/Field/ParkAr99Zn01Dat_Sp.dan",
                        "Event/ScriptList/ScriptList_Ar99Zn01.rlb"),
                    ],
        patch_patterns=ScriptList_Ar99Zn01_patterns
    )
    patches.append(scriptList_Ar99Zn01)

    scriptList_Ar06Zn01 = FilePatchConfig(
        file_id="scriptList_Ar06Zn01",
        description="ScriptList from Ar06Zn01",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar06Zn01Dat.dac", "Temporary/Field/ParkAr06Zn01Dat.dan",
                     "Event/ScriptList/ScriptList_Ar06Zn01.rlb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Fr.dac", "Temporary/Field/ParkAr06Zn01Dat_Fr.dan",
                        "Event/ScriptList/ScriptList_Ar06Zn01.rlb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Ge.dac", "Temporary/Field/ParkAr06Zn01Dat_Ge.dan",
                        "Event/ScriptList/ScriptList_Ar06Zn01.rlb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_It.dac", "Temporary/Field/ParkAr06Zn01Dat_It.dan",
                        "Event/ScriptList/ScriptList_Ar06Zn01.rlb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_Sp.dac", "Temporary/Field/ParkAr06Zn01Dat_Sp.dan",
                        "Event/ScriptList/ScriptList_Ar06Zn01.rlb"),
                    ],
        patch_patterns=ScriptList_Ar06Zn01_patterns
    )
    patches.append(scriptList_Ar06Zn01)

    gkBookShelf = FilePatchConfig(
        file_id="gk0502_bookshelf_gimmic",
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
    patches.append(gkBookShelf)

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
    patches.append(gk0502DoorB)

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
    patches.append(gk0502DoorC)

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
    patches.append(gk0502DoorD)

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
    patches.append(gk0502DoorE)

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
    patches.append(gk0501gate)

    field_Ar05Zn03_npc_script_config = FilePatchConfig(
        file_id="Ar05_Zn03",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar05Zn03Dat.dac", "Temporary/Field/ParkAr05Zn03Dat.dan",
                     "Script/evAr05Zn03_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar05Zn03Dat_Fr.dac", "Temporary/Field/ParkAr05Zn03Dat_Fr.dan",
                        "Script/evAr05Zn03_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar05Zn03Dat_Ge.dac", "Temporary/Field/ParkAr05Zn03Dat_Ge.dan",
                        "Script/evAr05Zn03_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn03Dat_It.dac", "Temporary/Field/ParkAr05Zn03Dat_It.dan",
                        "Script/evAr05Zn03_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn03Dat_Sp.dac", "Temporary/Field/ParkAr05Zn03Dat_Sp.dan",
                        "Script/evAr05Zn03_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr05Zn03_Npc_Main_patterns
    )
    patches.append(field_Ar05Zn03_npc_script_config)

    field_Ar05Zn03_script_event_config = FilePatchConfig(
        file_id="Ar05_Zn03_script_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar05Zn03Dat.dac", "Temporary/Field/ParkAr05Zn03Dat.dan",
                     "Script/evAr05Zn03_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar05Zn03Dat_Fr.dac", "Temporary/Field/ParkAr05Zn03Dat_Fr.dan",
                        "Script/evAr05Zn03_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar05Zn03Dat_Ge.dac", "Temporary/Field/ParkAr05Zn03Dat_Ge.dan",
                        "Script/evAr05Zn03_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn03Dat_It.dac", "Temporary/Field/ParkAr05Zn03Dat_It.dan",
                        "Script/evAr05Zn03_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn03Dat_Sp.dac", "Temporary/Field/ParkAr05Zn03Dat_Sp.dan",
                        "Script/evAr05Zn03_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr05Zn03_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar05Zn03_script_event_config)

    field_Ar05Zn02_npc_script_config = FilePatchConfig(
        file_id="Ar05_Zn02",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar05Zn02Dat.dac", "Temporary/Field/ParkAr05Zn02Dat.dan",
                     "Script/evAr05Zn02_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar05Zn02Dat_Fr.dac", "Temporary/Field/ParkAr05Zn02Dat_Fr.dan",
                        "Script/evAr05Zn02_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar05Zn02Dat_Ge.dac", "Temporary/Field/ParkAr05Zn02Dat_Ge.dan",
                        "Script/evAr05Zn02_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_It.dac", "Temporary/Field/ParkAr05Zn02Dat_It.dan",
                        "Script/evAr05Zn02_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Sp.dac", "Temporary/Field/ParkAr05Zn02Dat_Sp.dan",
                        "Script/evAr05Zn02_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr05Zn02_Npc_Main_patterns
    )
    patches.append(field_Ar05Zn02_npc_script_config)

    field_Ar05Zn02_script_event_config = FilePatchConfig(
        file_id="Ar05_Zn02_script_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar05Zn02Dat.dac", "Temporary/Field/ParkAr05Zn02Dat.dan",
                     "Script/evAr05Zn02_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar05Zn02Dat_Fr.dac", "Temporary/Field/ParkAr05Zn02Dat_Fr.dan",
                        "Script/evAr05Zn02_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar05Zn02Dat_Ge.dac", "Temporary/Field/ParkAr05Zn02Dat_Ge.dan",
                        "Script/evAr05Zn02_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_It.dac", "Temporary/Field/ParkAr05Zn02Dat_It.dan",
                        "Script/evAr05Zn02_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Sp.dac", "Temporary/Field/ParkAr05Zn02Dat_Sp.dan",
                        "Script/evAr05Zn02_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr05Zn02_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar05Zn02_script_event_config)

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
    patches.append(field_Ar05Zn01_npc_script_config)

    field_Ar05Zn01_script_event_config = FilePatchConfig(
        file_id="Ar05_Zn01_script_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar05Zn01Dat.dac", "Temporary/Field/ParkAr05Zn01Dat.dan",
                     "Script/evAr05Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar05Zn01Dat_Fr.dac", "Temporary/Field/ParkAr05Zn01Dat_Fr.dan",
                        "Script/evAr05Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar05Zn01Dat_Ge.dac", "Temporary/Field/ParkAr05Zn01Dat_Ge.dan",
                        "Script/evAr05Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn01Dat_It.dac", "Temporary/Field/ParkAr05Zn01Dat_It.dan",
                        "Script/evAr05Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn01Dat_Sp.dac", "Temporary/Field/ParkAr05Zn01Dat_Sp.dan",
                        "Script/evAr05Zn01_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr05Zn01_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar05Zn01_script_event_config)

    evAr05Zn02_Gimmic = FilePatchConfig(
        file_id="ar05zn02_gimmic",
        description="",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar05Zn02Dat.dac", "Temporary/Field/ParkAr05Zn02Dat.dan",
                     "Script/evAr05Zn02_Gimmic.fsb"), (
                        "DATA/files/Field/Ar05Zn02Dat_Fr.dac", "Temporary/Field/ParkAr05Zn02Dat_Fr.dan",
                        "Script/evAr05Zn02_Gimmic.fsb"), (
                        "DATA/files/Field/Ar05Zn02Dat_Ge.dac", "Temporary/Field/ParkAr05Zn02Dat_Ge.dan",
                        "Script/evAr05Zn02_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_It.dac", "Temporary/Field/ParkAr05Zn02Dat_It.dan",
                        "Script/evAr05Zn02_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar05Zn02Dat_Sp.dac", "Temporary/Field/ParkAr05Zn02Dat_Sp.dan",
                        "Script/evAr05Zn02_Gimmic.fsb"),
                    ],
        patch_patterns=evAr05Zn02_Gimmic_patterns
    )
    patches.append(evAr05Zn02_Gimmic)

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
    patches.append(evAr05Zn01_Gimmic)

    return patches


def get_granite_zone_patches() -> List[FilePatchConfig]:
    patches = []
    ar06zn01Disposition = FilePatchConfig(
        file_id="disposition_ar06zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.DAC_U8,
        file_group=[("DATA/files/Field/Ar06Zn01Dat.dac", "unused",
                     "Field/Ar06/Zn01/Ar06Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar06Zn01Dat_Fr.dac", "unused",
                     "Field/Ar06/Zn01/Ar06Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar06Zn01Dat_Ge.dac", "unused",
                     "Field/Ar06/Zn01/Ar06Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar06Zn01Dat_It.dac", "unused",
                     "Field/Ar06/Zn01/Ar06Zn01Dp00.rlb"),
                    ("DATA/files/Field/Ar06Zn01Dat_Sp.dac", "unused",
                     "Field/Ar06/Zn01/Ar06Zn01Dp00.rlb"),
                    ],
        patch_patterns=disposition_drifblim_patterns
    )
    patches.append(ar06zn01Disposition)

    gkFireWallC = FilePatchConfig(
        file_id="gkFireWallC",
        description="Granite Zone FireWall",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar06Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/GkFireWallC.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkFireWallC.fsb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkFireWallC.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkFireWallC.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/GkFireWallC.fsb"),
                    ],
        patch_patterns=gkFireWallC_pattern
    )
    patches.append(gkFireWallC)

    gk0601SwitchB = FilePatchConfig(
        file_id="gk0601SwitchB_gimmic",
        description="Granite Zone Flygon DoorB",
        processing_type=FileProcessingType.NESTED_DAC_U8,

        file_group=[("DATA/files/Field/Ar06Zn01Dat.dac", "Gimmick/GkDatArc.dan",
                     "Gimmick/Gk0601SwitchB.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_Fr.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0601SwitchB.fsb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Ge.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0601SwitchB.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_It.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0601SwitchB.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_Sp.dac", "Gimmick/GkDatArc.dan",
                        "Gimmick/Gk0601SwitchB.fsb"),
                    ],
        patch_patterns=gk0601SwitchB_pattern
    )
    patches.append(gk0601SwitchB)

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
    patches.append(gk0601DoorB)

    evAr06Zn01_Gimmic = FilePatchConfig(
        file_id="ar06zn01_gimmic",
        description="",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar06Zn01Dat.dac", "Temporary/Field/ParkAr06Zn01Dat.dan",
                     "Script/evAr06Zn01_Gimmic.fsb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Fr.dac", "Temporary/Field/ParkAr06Zn01Dat_Fr.dan",
                        "Script/evAr06Zn01_Gimmic.fsb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Ge.dac", "Temporary/Field/ParkAr06Zn01Dat_Ge.dan",
                        "Script/evAr06Zn01_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_It.dac", "Temporary/Field/ParkAr06Zn01Dat_It.dan",
                        "Script/evAr06Zn01_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_Sp.dac", "Temporary/Field/ParkAr06Zn01Dat_Sp.dan",
                        "Script/evAr06Zn01_Gimmic.fsb"),
                    ],
        patch_patterns=evAr06Zn01_Gimmic_patterns
    )
    patches.append(evAr06Zn01_Gimmic)

    evAr06Zn01_DemoEvent = FilePatchConfig(
        file_id="ar06zn01_demoEvent",
        description="",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar06Zn01Dat.dac", "Temporary/Field/ParkAr06Zn01Dat.dan",
                     "Script/evAr06Zn01_DemoEvent.fsb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Fr.dac", "Temporary/Field/ParkAr06Zn01Dat_Fr.dan",
                        "Script/evAr06Zn01_DemoEvent.fsb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Ge.dac", "Temporary/Field/ParkAr06Zn01Dat_Ge.dan",
                        "Script/evAr06Zn01_DemoEvent.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_It.dac", "Temporary/Field/ParkAr06Zn01Dat_It.dan",
                        "Script/evAr06Zn01_DemoEvent.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_Sp.dac", "Temporary/Field/ParkAr06Zn01Dat_Sp.dan",
                        "Script/evAr06Zn01_DemoEvent.fsb"),
                    ],
        patch_patterns=evAr06Zn01_DemoEvent_patterns
    )
    patches.append(evAr06Zn01_DemoEvent)

    field_Ar06Zn01_npc_script_config = FilePatchConfig(
        file_id="Ar06_Zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar06Zn01Dat.dac", "Temporary/Field/ParkAr06Zn01Dat.dan",
                     "Script/evAr06Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Fr.dac", "Temporary/Field/ParkAr06Zn01Dat_Fr.dan",
                        "Script/evAr06Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Ge.dac", "Temporary/Field/ParkAr06Zn01Dat_Ge.dan",
                        "Script/evAr06Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_It.dac", "Temporary/Field/ParkAr06Zn01Dat_It.dan",
                        "Script/evAr06Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_Sp.dac", "Temporary/Field/ParkAr06Zn01Dat_Sp.dan",
                        "Script/evAr06Zn01_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr06Zn01_Npc_Main_patterns
    )
    patches.append(field_Ar06Zn01_npc_script_config)

    field_Ar06Zn01_script_event_config = FilePatchConfig(
        file_id="Ar06_Zn01_script_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar06Zn01Dat.dac", "Temporary/Field/ParkAr06Zn01Dat.dan",
                     "Script/evAr06Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Fr.dac", "Temporary/Field/ParkAr06Zn01Dat_Fr.dan",
                        "Script/evAr06Zn01_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar06Zn01Dat_Ge.dac", "Temporary/Field/ParkAr06Zn01Dat_Ge.dan",
                        "Script/evAr06Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_It.dac", "Temporary/Field/ParkAr06Zn01Dat_It.dan",
                        "Script/evAr06Zn01_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn01Dat_Sp.dac", "Temporary/Field/ParkAr06Zn01Dat_Sp.dan",
                        "Script/evAr06Zn01_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr06Zn01_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar06Zn01_script_event_config)
    return patches


def get_flower_zone_patches() -> List[FilePatchConfig]:
    patches = []
    ar06zn02Disposition = FilePatchConfig(
        file_id="disposition_ar06zn02",
        description="Field Script Main",
        processing_type=FileProcessingType.DAC_U8,
        file_group=[("DATA/files/Field/Ar06Zn02Dat.dac", "unused",
                     "Field/Ar06/Zn02/Ar06Zn02Dp00.rlb"),
                    ("DATA/files/Field/Ar06Zn02Dat_Fr.dac", "unused",
                     "Field/Ar06/Zn02/Ar06Zn02Dp00.rlb"),
                    ("DATA/files/Field/Ar06Zn02Dat_Ge.dac", "unused",
                     "Field/Ar06/Zn02/Ar06Zn02Dp00.rlb"),
                    ("DATA/files/Field/Ar06Zn02Dat_It.dac", "unused",
                     "Field/Ar06/Zn02/Ar06Zn02Dp00.rlb"),
                    ("DATA/files/Field/Ar06Zn02Dat_Sp.dac", "unused",
                     "Field/Ar06/Zn02/Ar06Zn02Dp00.rlb"),
                    ],
        patch_patterns=disposition_drifblim_patterns
    )
    patches.append(ar06zn02Disposition)

    evAr06Zn02_Gimmic = FilePatchConfig(
        file_id="ar06zn02_gimmic",
        description="",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar06Zn02Dat.dac", "Temporary/Field/ParkAr06Zn02Dat.dan",
                     "Script/evAr06Zn02_Gimmic.fsb"), (
                        "DATA/files/Field/Ar06Zn02Dat_Fr.dac", "Temporary/Field/ParkAr06Zn02Dat_Fr.dan",
                        "Script/evAr06Zn02_Gimmic.fsb"), (
                        "DATA/files/Field/Ar06Zn02Dat_Ge.dac", "Temporary/Field/ParkAr06Zn02Dat_Ge.dan",
                        "Script/evAr06Zn02_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn02Dat_It.dac", "Temporary/Field/ParkAr06Zn02Dat_It.dan",
                        "Script/evAr06Zn02_Gimmic.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn02Dat_Sp.dac", "Temporary/Field/ParkAr06Zn02Dat_Sp.dan",
                        "Script/evAr06Zn02_Gimmic.fsb"),
                    ],
        patch_patterns=evAr06Zn02_Gimmic_patch_pattern
    )
    patches.append(evAr06Zn02_Gimmic)

    field_Ar06Zn02_npc_script_config = FilePatchConfig(
        file_id="Ar06_Zn02",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar06Zn02Dat.dac", "Temporary/Field/ParkAr06Zn02Dat.dan",
                     "Script/evAr06Zn02_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar06Zn02Dat_Fr.dac", "Temporary/Field/ParkAr06Zn02Dat_Fr.dan",
                        "Script/evAr06Zn02_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar06Zn02Dat_Ge.dac", "Temporary/Field/ParkAr06Zn02Dat_Ge.dan",
                        "Script/evAr06Zn02_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn02Dat_It.dac", "Temporary/Field/ParkAr06Zn02Dat_It.dan",
                        "Script/evAr06Zn02_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn02Dat_Sp.dac", "Temporary/Field/ParkAr06Zn02Dat_Sp.dan",
                        "Script/evAr06Zn02_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr06Zn02_Npc_Main_patterns
    )
    patches.append(field_Ar06Zn02_npc_script_config)

    field_Ar06Zn02_script_event_config = FilePatchConfig(
        file_id="Ar06_Zn02_script_event",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar06Zn02Dat.dac", "Temporary/Field/ParkAr06Zn02Dat.dan",
                     "Script/evAr06Zn02_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar06Zn02Dat_Fr.dac", "Temporary/Field/ParkAr06Zn02Dat_Fr.dan",
                        "Script/evAr06Zn02_ScriptEvent.fsb"), (
                        "DATA/files/Field/Ar06Zn02Dat_Ge.dac", "Temporary/Field/ParkAr06Zn02Dat_Ge.dan",
                        "Script/evAr06Zn02_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn02Dat_It.dac", "Temporary/Field/ParkAr06Zn02Dat_It.dan",
                        "Script/evAr06Zn02_ScriptEvent.fsb"),
                    (
                        "DATA/files/Field/Ar06Zn02Dat_Sp.dac", "Temporary/Field/ParkAr06Zn02Dat_Sp.dan",
                        "Script/evAr06Zn02_ScriptEvent.fsb"),
                    ],
        patch_patterns=evAr06Zn02_ScriptEvent_patch_pattern
    )
    patches.append(field_Ar06Zn02_script_event_config)
    return patches


def get_misc_patches() -> List[FilePatchConfig]:
    patches = []
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
        patch_patterns=start_menu_pattern
    )
    patches.append(start_menu_config)

    main_dol = FilePatchConfig(
        file_id="main_dol",
        description="main dol",
        processing_type=FileProcessingType.MAIN_DOL,
        file_group=[("DATA/sys/main.dol", "", "")],
        patch_patterns=main_dol_pattern
    )

    patches.append(main_dol)
    return patches


def get_skygarden_patches() -> List[FilePatchConfig]:
    patches = []
    field_Ar07Zn01_npc_script_config = FilePatchConfig(
        file_id="Ar07_Zn01",
        description="Field Script Main",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        file_group=[("DATA/files/Field/Ar07Zn01Dat.dac", "Temporary/Field/ParkAr07Zn01Dat.dan",
                     "Script/evAr07Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar07Zn01Dat_Fr.dac", "Temporary/Field/ParkAr07Zn01Dat_Fr.dan",
                        "Script/evAr07Zn01_Npc_Main.fsb"), (
                        "DATA/files/Field/Ar07Zn01Dat_Ge.dac", "Temporary/Field/ParkAr07Zn01Dat_Ge.dan",
                        "Script/evAr07Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar07Zn01Dat_It.dac", "Temporary/Field/ParkAr07Zn01Dat_It.dan",
                        "Script/evAr07Zn01_Npc_Main.fsb"),
                    (
                        "DATA/files/Field/Ar07Zn01Dat_Sp.dac", "Temporary/Field/ParkAr07Zn01Dat_Sp.dan",
                        "Script/evAr07Zn01_Npc_Main.fsb"),
                    ],
        patch_patterns=evAr07Zn01_Npc_Main_patterns
    )
    patches.append(field_Ar07Zn01_npc_script_config)
    return patches


def get_all_patches() -> List[FilePatchConfig]:
    patches = []
    patches.extend(get_attraction_patches())
    patches.extend(get_meadow_zone_patches())
    patches.extend(get_park_entrance_patches())
    patches.extend(get_treehouse_patches())
    patches.extend(get_beach_zone_patches())
    patches.extend(get_ice_zone_patches())
    patches.extend(get_cavern_zone_patches())
    patches.extend(get_magma_zone_patches())
    patches.extend(get_haunted_zone_patches())
    patches.extend(get_granite_zone_patches())
    patches.extend(get_flower_zone_patches())
    patches.extend(get_misc_patches())
    patches.extend(get_skygarden_patches())

    return patches
