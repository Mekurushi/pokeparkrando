from typing import List

from patcher.models.models import FilePatchConfig, FileProcessingType
from patcher.patterns.evAr01Zn01_Gimmic import evAr01Zn01_Gimmic_patch_pattern
from patcher.patterns.evAr01Zn01_Npc_Main import \
    evAr01Zn01_Npc_Main_patch_pattern
from patcher.patterns.evAr01Zn02_Npc_Main import evAr01Zn02_Npc_Main_patterns
from patcher.patterns.evAr02Zn01_Npc_Main import evAr02Zn01_Npc_Main_pattern
from patcher.patterns.evAr99Zn01_Npc_Main import evAr99Zn01_Npc_Main_pattern
from patcher.patterns.gk0101Gate import gate101_close
from patcher.patterns.gkKabigonWall import gkKabigonWallPattern
from patcher.patterns.gkWoodBoxKino import gkWoodBoxKinoPattern
from patcher.patterns.main import stage_setup_new_file_pattern, setup_new_file_pattern, \
    custom_give_item_function_call_pattern, custom_give_item_function_pattern
from patcher.patterns.mnAttractionInfo import mnAttractionInfo_pattern
from patcher.patterns.mnLobby import mnLobby_pattern
from patcher.patterns.mnStartMenu import load_new_file_pattern
from patcher.patterns.treehouse import treehouse_pattern

plando_dict_ap = None


def get_default_patch_configs() -> List[FilePatchConfig]:
    configs = []

    start_menu_config = FilePatchConfig(
        file_id="mnStartMenu",
        description="",
        processing_type=FileProcessingType.DAC_U8,
        file_group=[("DATA/files/Archive/StartMenuDat.dac", "unused",
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
        patch_patterns=[
            custom_give_item_function_call_pattern,
            custom_give_item_function_pattern,
            stage_setup_new_file_pattern,
            setup_new_file_pattern
        ]
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
