from typing import List

from gui.core.models import FilePatchConfig, FileProcessingType, PatchOperation


def get_default_patch_configs() -> List[FilePatchConfig]:
    configs = []

    field_meadow_npc_script_config = FilePatchConfig(
        file_id="meadow_zone_main_npc_script",
        description="Field Script Main Randomization",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Field/Ar01Zn01Dat.dac",
        alternative_paths=["files/Field/Ar01Zn01Dat.dac"],
        nested_archive_path="Temporary/Field/ParkAr01Zn01Dat.dan",
        nested_alternative_paths=["Field/ParkAr01Zn01Dat.dan", "ParkAr01Zn01Dat.dan"],
        target_file_path="Script/evAr01Zn01_Npc_Main.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x0000c518,
                original_value=0x00020208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="patching Chimchar spawn requirement in Meadow Zone"
            ),
            PatchOperation(
                offset=0x0000bf94,
                original_value=0x00030208,
                new_value=0x00030008,
                size=4,
                byteorder="big",
                description="spawn magikarp always"
            ),
            PatchOperation(
                offset=0x0000027c,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="magikarp check sets always unlock data"
            ),
            PatchOperation(
                offset=0x000160fc,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship scyther"
            ),
            PatchOperation(
                offset=0x00015e64,
                original_value=0x00050010,
                new_value=0x00000010,
                size=4,
                byteorder="big",
                description="testing battle counter scyther set to 0"
            ),

            PatchOperation(
                offset=0x00015f5c,
                original_value=0x00050010,
                new_value=0x00000010,
                size=4,
                byteorder="big",
                description="testing battle counter scyther set to 0"
            ),

            PatchOperation(
                offset=0x0001317c,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Lotad"
            ),

            PatchOperation(
                offset=0x00011a58,
                original_value=0x000e0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Turtwig"
            ),
            PatchOperation(
                offset=0x00011ff8,
                original_value=0x00180208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Buneary"
            ),
            PatchOperation(
                offset=0x000124e8,
                original_value=0x00050208,
                new_value=0x00050008,
                size=4,
                byteorder="big",
                description="always trigger friendship Munchlax"
            ),
            PatchOperation(
                offset=0x00015454,
                original_value=0x00040208,
                new_value=0x00040008,
                size=4,
                byteorder="big",
                description="always trigger friendship Tropius"
            ),
            PatchOperation(
                offset=0x0001641c,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Leafeon"
            ),
            PatchOperation(
                offset=0x00012324,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Pachirisu 1"
            ),
            PatchOperation(
                offset=0x00012920,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Treecko"
            ),
            PatchOperation(
                offset=0x00012bcc,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Chimchar"
            ),
            PatchOperation(
                offset=0x00012e78,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Magikarp"
            ),
            PatchOperation(
                offset=0x00013428,
                original_value=0x00190208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Caterpie"
            ),
            PatchOperation(
                offset=0x00013710,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Weedle"
            ),
            PatchOperation(
                offset=0x0000f9a8,
                original_value=0x00040208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Bidoof"
            ),
            PatchOperation(
                offset=0x000139d4,
                original_value=0x00080208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Oddish"
            ),
            PatchOperation(
                offset=0x00013c70,
                original_value=0x00080208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Shroomish"
            ),
            PatchOperation(
                offset=0x00013f7c,
                original_value=0x00150208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Bonsly"
            ),
            PatchOperation(
                offset=0x0001424c,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Shinx 1"
            ),
            PatchOperation(
                offset=0x0001456c,
                original_value=0xc0f60103,
                new_value=0xc0da0003,
                size=4,
                byteorder="big",
                description="Overworld Mankey triggers Friendship"
            ),
            PatchOperation(
                offset=0x000147dc,
                original_value=0x00170208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Aipom (Tree)"
            ),
            PatchOperation(
                offset=0x00014abc,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Spearow"
            ),
            PatchOperation(
                offset=0x00014da4,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Torterra"
            ),
            PatchOperation(
                offset=0x00015050,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Starly 1"
            ),
            PatchOperation(
                offset=0x000152fc,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Butterfree 1"
            ),
            PatchOperation(
                offset=0x000157e4,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Bibarel"
            ),
            PatchOperation(
                offset=0x00015a90,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Ambipom"
            ),
            PatchOperation(
                offset=0x00015d4c,
                original_value=0x00080208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Sudowoodo"
            ),
            PatchOperation(
                offset=0x0001047c,
                original_value=0x000c0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Croagunk"
            ),
            PatchOperation(
                offset=0x00016adc,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Starly 2"
            ),
            PatchOperation(
                offset=0x00016d88,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Starly 3"
            ),
            PatchOperation(
                offset=0x00017034,
                original_value=0x00170208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Aipom free roaming"
            ),
            PatchOperation(
                offset=0x000176b8,
                original_value=0x000a0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger friendship Attraction Spearow"
            ),
            PatchOperation(
                offset=0x000179f0,
                original_value=0x00060208,
                new_value=0x00060008,
                size=4,
                byteorder="big",
                description="always trigger friendship Lotad 2"
            ),
            PatchOperation(
                offset=0x0001730c,
                original_value=0x00060208,
                new_value=0x00060008,
                size=4,
                byteorder="big",
                description="always trigger friendship Starly 4"
            ),
            PatchOperation(
                offset=0x00017cd0,
                original_value=0x00060208,
                new_value=0x00060008,
                size=4,
                byteorder="big",
                description="always trigger friendship Lotad 3"
            ),
            PatchOperation(
                offset=0x00017f5c,
                original_value=0x00060208,
                new_value=0x00060008,
                size=4,
                byteorder="big",
                description="always trigger friendship Starly 5"
            ),
            PatchOperation(
                offset=0x00018724,
                original_value=0x00060208,
                new_value=0x00060008,
                size=4,
                byteorder="big",
                description="always trigger friendship Shinx 2"
            ),
            PatchOperation(
                offset=0x000190d8,
                original_value=0x00060208,
                new_value=0x00060008,
                size=4,
                byteorder="big",
                description="always trigger friendship Butterfree 2"
            ),
            PatchOperation(
                offset=0x00019914,
                original_value=0x00060208,
                new_value=0x00060008,
                size=4,
                byteorder="big",
                description="always trigger friendship Pachirisu 2"
            ),
        ]
    )
    configs.append(field_meadow_npc_script_config)

    field_skygarden_npc_script_config = FilePatchConfig(
        file_id="skygarden_main_npc_script",
        description="Skygarden NPC Script",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Field/Ar07Zn01Dat.dac",
        alternative_paths=["files/Field/Ar07Zn01Dat.dac"],
        nested_archive_path="Temporary/Field/ParkAr07Zn01Dat.dan",
        nested_alternative_paths=["Field/ParkAr07Zn01Dat.dan", "ParkAr07Zn01Dat.dan"],
        target_file_path="Script/evAr07Zn01_Npc_Main.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011ad8,
                original_value=0x00140208,
                new_value=0x00140008,
                size=4,
                byteorder="big",
                description="skip postgame check in mew dialog options"
            ),
            PatchOperation(
                offset=0x000127b0,
                original_value=0x006e0208,
                new_value=0x006e0008,
                size=4,
                byteorder="big",
                description="skip postgame check in piplup dialog options"
            ),
            PatchOperation(
                offset=0x0000e0a8,
                original_value=0x00700208,
                new_value=0x00700008,
                size=4,
                byteorder="big",
                description="skip postgame check in choosing story challenge or postgame challenge"
            ),
            PatchOperation(
                offset=0x0000ff18,
                original_value=0x00010508,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="skip postgame check in should befriend mew post challenge"
            ),
            PatchOperation(
                offset=0x000101fc,
                original_value=0xfe980010,
                new_value=0xff620010,
                size=4,
                byteorder="big",
                description="after challenge spawn player not on platform"
            ),
            PatchOperation(
                offset=0x00010200,
                original_value=0x00500010,
                new_value=0x00140010,
                size=4,
                byteorder="big",
                description="after challenge spawn player not on platform"
            ),

            PatchOperation(
                offset=0x000101cc,
                original_value=0xfe800010,
                new_value=0xff560010,
                size=4,
                byteorder="big",
                description="after challenge spawn mew not on platform"
            ),
            PatchOperation(
                offset=0x000101d0,
                original_value=0x00500010,
                new_value=0x00140010,
                size=4,
                byteorder="big",
                description="after challenge spawn mew not on platform"
            ),
            PatchOperation(
                offset=0x00010248,
                original_value=0xcd1c0403,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="after challenge spawn piplup, etc. on balloon"
            ),
            PatchOperation(
                offset=0x00010288,
                original_value=0xcd0c0403,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="after challenge spawn piplup, etc. on balloon"
            ),
            PatchOperation(
                offset=0x000102c8,
                original_value=0xccfc0403,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="after challenge spawn piplup, etc. on balloon"
            ),

            PatchOperation(
                offset=0x0000ce50,
                original_value=0x00030208,
                new_value=0x00030008,
                size=4,
                byteorder="big",
                description="remove spawn condition for mew world state 0x2710"
            ),
            PatchOperation(
                offset=0x0000ce84,
                original_value=0x00330208,
                new_value=0x00330008,
                size=4,
                byteorder="big",
                description="remove spawn condition for mew world state <0x2725"
            ),
            PatchOperation(
                offset=0x0000cf78,
                original_value=0x00410208,
                new_value=0x00410008,
                size=4,
                byteorder="big",
                description="remove spawn condition for mew world state <0x2742"
            ),
            PatchOperation(
                offset=0x0000d08c,
                original_value=0x004c0208,
                new_value=0x004c0008,
                size=4,
                byteorder="big",
                description="remove spawn condition for mew world state 0x2742"
            ),
            PatchOperation(
                offset=0x0000d1cc,
                original_value=0x00400208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="spawn always post game mew world state 0x2af0"
            ),
            PatchOperation(
                offset=0x000049ac,
                original_value=0x00000012,
                new_value=0x00000010,
                size=4,
                byteorder="big",
                description="Mew friendship trigger"
            ),
            PatchOperation(
                offset=0x000102fc,
                original_value=0xd1c40103,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="remove chapter update"
            )
        ]
    )
    configs.append(field_skygarden_npc_script_config)

    field_blaziken_npc_script_config = FilePatchConfig(
        file_id="blaziken_main_npc_script",
        description="Blaziken NPC Script",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Field/Ar04Zn03Dat.dac",
        nested_archive_path="Temporary/Field/ParkAr04Zn03Dat.dan",
        target_file_path="Script/evAr04Zn03_Npc_Main.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00008d3c,
                original_value=0x00000012,
                new_value=0x00000010,
                size=4,
                byteorder="big",
                description="skip is friend check in blaziken friendship"
            ),
            PatchOperation(
                offset=0x00008d84,
                original_value=0xdcbe0103,
                new_value=0x003e0008,
                size=4,
                byteorder="big",
                description="trigger blaziken minigame"
            ),
        ]
    )
    configs.append(field_blaziken_npc_script_config)

    field_beach_zone_gimmic_script_config = FilePatchConfig(
        file_id="beach_zone_gimmic_script",
        description="Beach Zone Gimmic Script",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Field/Ar03Zn01Dat.dac",
        nested_archive_path="Temporary/Field/ParkAr03Zn01Dat.dan",
        target_file_path="Script/evAr03Zn01_Gimmic.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x0000027c,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="always trigger unlock"
            ),
            PatchOperation(
                offset=0x0008348,
                original_value=0x000f0208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger unlock Recycle Box"
            ),
        ]
    )
    configs.append(field_beach_zone_gimmic_script_config)


    field_beach_zone_npc_script_config = FilePatchConfig(
        file_id="beach_zone_main_npc_script",
        description="Beach Zone NPC Script",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Field/Ar03Zn01Dat.dac",
        nested_archive_path="Temporary/Field/ParkAr03Zn01Dat.dan",
        target_file_path="Script/evAr03Zn01_Npc_Main.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x000123bc,
                original_value=0x00120208,
                new_value=0x00120008,
                size=4,
                byteorder="big",
                description="skip pre minigame friendship check gyarados"
            ),
            PatchOperation(
                offset=0x00011c30,
                original_value=0x00120208,
                new_value=0x00120008,
                size=4,
                byteorder="big",
                description="skip pre minigame friendship check pelipper"
            ),
        ]
    )
    configs.append(field_beach_zone_npc_script_config)

    field_event_gimmic_script = FilePatchConfig(
        file_id="meadow_zone_main_event_script",
        description="event Script Main Randomization",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Field/Ar01Zn01Dat.dac",
        alternative_paths=["files/Field/Ar01Zn01Dat.dac"],
        nested_archive_path="Temporary/Field/ParkAr01Zn01Dat.dan",
        nested_alternative_paths=["Field/ParkAr01Zn01Dat.dan", "ParkAr01Zn01Dat.dan"],
        target_file_path="Script/evAr01Zn01_Gimmic.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00008318,
                original_value=0x00e70208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always unlock caterpie"
            ),
            PatchOperation(
                offset=0x0000027c,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="always trigger unlock in gimmic"
            ),

            PatchOperation(
                offset=0x00008298,
                original_value=0x00040208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always unlock beedle"
            ),
            PatchOperation(
                offset=0x00007e70,
                original_value=0x00f00208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always trigger beedle unlock"
            ),

            PatchOperation(
                offset=0x00008bf4,
                original_value=0x00e90208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="always unlock shroomish"
            ),
        ]
    )
    configs.append(field_event_gimmic_script)

    field_gimmic_shroomish_crate = FilePatchConfig(
        file_id="gimmic_script_main",
        description="Gimmic Script Main Randomization",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Field/Ar01Zn01Dat.dac",
        alternative_paths=["files/Field/Ar01Zn01Dat.dac"],
        nested_archive_path="Gimmick/GkDatArc.dan",
        nested_alternative_paths=["GkDatArc.dan"],
        target_file_path="Gimmick/GkWoodBoxKino.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000be8,
                original_value=0x00100208,
                new_value=0x00100008,
                size=4,
                byteorder="big",
                description="always spawn shroomish Crate"
            ),
        ]
    )
    configs.append(field_gimmic_shroomish_crate)

    field_cavern_npc_script_config = FilePatchConfig(
        file_id="field_script_main_cavern",
        description="Field Script Main Cavern Randomization",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Field/Ar04Zn01Dat.dac",
        alternative_paths=["files/Field/Ar04Zn01Dat.dac"],
        nested_archive_path="Temporary/Field/ParkAr04Zn01Dat.dan",
        nested_alternative_paths=["Field/ParkAr04Zn01Dat.dan", "ParkAr04Zn01Dat.dan"],
        target_file_path="Script/evAr04Zn01_Npc_Main.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x0000ba40,
                original_value=0x00040208,
                new_value=0x00000002,
                size=4,
                byteorder="big",
                description="Chimchar and Torchic spawn requirement in cavern zone"
            )
        ]
    )

    configs.append(field_cavern_npc_script_config)

    main_dol = FilePatchConfig(
        file_id="main_dol",
        description="main dol",
        processing_type=FileProcessingType.MAIN_DOL,
        primary_file_path="DATA/sys/main.dol",
        patch_operations=[
            PatchOperation(
                offset=0x8004faa0,
                original_value=0x4e800020,
                new_value=0x3d808037,
                size=4,
                byteorder="big",
                description="Patching PokemonId cleanup function"
            ),
            PatchOperation(
                offset=0x8004faa4,
                original_value=0x00,
                new_value=0x38600000,
                size=4,
                byteorder="big",
                description="Patching PokemonId cleanup function"
            ),
            PatchOperation(
                offset=0x8004faa8,
                original_value=0x00,
                new_value=0x906CDC20,
                size=4,
                byteorder="big",
                description="Patching PokemonId cleanup function"
            ),
            PatchOperation(
                offset=0x8004faac,
                original_value=0x00,
                new_value=0x4e800020,
                size=4,
                byteorder="big",
                description="Patching PokemonId cleanup function"
            ),

            PatchOperation(
                offset=0x80126508,
                original_value=0x98030000,
                new_value=0x98030001,
                size=4,
                byteorder="big",
                description="Friendship trigger patch"
            ),

            PatchOperation(
                offset=0x8018397c,
                original_value=0x90040010,
                new_value=0x90047fff,
                size=4,
                byteorder="big",
                description="Unlock trigger patch"
            ),
            PatchOperation(
                offset=0x80183970,
                original_value=0x80640010,
                new_value=0x38600000,
                size=4,
                byteorder="big",
                description="Unlock trigger patch"
            ),

            PatchOperation(
                offset=0x80026664,
                original_value=0x4e800020,
                new_value=0x3ca08037,
                size=4,
                byteorder="big",
                description="Setup PokemonId patch"
            ),
            PatchOperation(
                offset=0x80026668,
                original_value=0x0,
                new_value=0x9085dc20,
                size=4,
                byteorder="big",
                description="Setup PokemonId patch"
            ),
            PatchOperation(
                offset=0x8002666c,
                original_value=0x0,
                new_value=0x4e800020,
                size=4,
                byteorder="big",
                description="Setup PokemonId patch"
            ),

            PatchOperation(
                offset=0x801261e0,
                original_value=0x90030000,
                new_value=0x90037fff,
                size=4,
                byteorder="big",
                description="Prisma Trigger function patch"
            ),

            PatchOperation(
                offset=0x801268f4,
                original_value=0xb003002e,
                new_value=0x60000000,
                size=4,
                byteorder="big",
                description="Deactivate PowerUp levelup"
            ),
        ]
    )

    configs.append(main_dol)

    lobby1_script = FilePatchConfig(
        file_id="lobby1_script",
        description="Lobby 01 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby01Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby1_script)

    attraction01_script_config = FilePatchConfig(
        file_id="attraction_01",
        description="Attraction 1 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At001Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt001Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction01_script_config)

    lobby2_script = FilePatchConfig(
        file_id="lobby2_script",
        description="Lobby 2 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby02Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby2_script)

    attraction02_script_config = FilePatchConfig(
        file_id="attraction_02",
        description="Attraction 2 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At002Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt002Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction02_script_config)

    lobby3_script = FilePatchConfig(
        file_id="lobby3_script",
        description="Lobby 3 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby03Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby3_script)

    attraction03_script_config = FilePatchConfig(
        file_id="attraction_03",
        description="Attraction 3 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At003Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt003Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction03_script_config)


    lobby4_script = FilePatchConfig(
        file_id="lobby4_script",
        description="Lobby 4 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby04Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby4_script)

    attraction04_script_config = FilePatchConfig(
        file_id="attraction_04",
        description="Attraction 4 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At004Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt004Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction04_script_config)

    lobby5_script = FilePatchConfig(
        file_id="lobby5_script",
        description="Lobby 5 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby05Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby5_script)

    attraction05_script_config = FilePatchConfig(
        file_id="attraction_05",
        description="Attraction 5 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At005Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt005Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction05_script_config)

    lobby6_script = FilePatchConfig(
        file_id="lobby6_script",
        description="Lobby 6 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby06Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby6_script)

    attraction06_script_config = FilePatchConfig(
        file_id="attraction_06",
        description="Attraction 6 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At006Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt006Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction06_script_config)

    lobby7_script = FilePatchConfig(
        file_id="lobby7_script",
        description="Lobby 7 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby07Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby7_script)

    attraction07_script_config = FilePatchConfig(
        file_id="attraction_07",
        description="Attraction 7 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At007Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt007Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction07_script_config)

    lobby9_script = FilePatchConfig(
        file_id="lobby9_script",
        description="Lobby 9 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby09Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby9_script)

    attraction09_script_config = FilePatchConfig(
        file_id="attraction_09",
        description="Attraction 9 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At009Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt009Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction09_script_config)

    lobby10_script = FilePatchConfig(
        file_id="lobby10_script",
        description="Lobby 10 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby10Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby10_script)

    attraction10_script_config = FilePatchConfig(
        file_id="attraction_10",
        description="Attraction 10 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At010Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt010Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction10_script_config)

    lobby11_script = FilePatchConfig(
        file_id="lobby11_script",
        description="Lobby 11 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby11Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby11_script)

    attraction11_script_config = FilePatchConfig(
        file_id="attraction_11",
        description="Attraction 11 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At011Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt011Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction11_script_config)

    lobby12_script = FilePatchConfig(
        file_id="lobby12_script",
        description="Lobby 12 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby12Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby12_script)

    attraction12_script_config = FilePatchConfig(
        file_id="attraction_12",
        description="Attraction 12 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At012Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt012Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction12_script_config)

    lobby13_script = FilePatchConfig(
        file_id="lobby13_script",
        description="Lobby 13 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby13Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby13_script)

    attraction13_script_config = FilePatchConfig(
        file_id="attraction_13",
        description="Attraction 13 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At013Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt013Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction13_script_config)

    lobby15_script = FilePatchConfig(
        file_id="lobby15_script",
        description="Lobby 15 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby15Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="always postgame modus" # idk why this works
            ),
        ]
    )
    configs.append(lobby15_script)

    attraction15_script_config = FilePatchConfig(
        file_id="attraction_15",
        description="Attraction 15 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At015Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt015Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction15_script_config)

    lobby16_script = FilePatchConfig(
        file_id="lobby16_script",
        description="Lobby 016 Script",
        processing_type=FileProcessingType.DAC_U8,
        primary_file_path="DATA/files/Archive/Lobby16Dat.dac",
        target_file_path="Script/mnLobby.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00011c4,
                original_value=0x00160010,
                new_value=0x00150010,
                size=4,
                byteorder="big",
                description="test postgame check skip attraction" # idk why this works
            ),
        ]
    )
    configs.append(lobby16_script)

    attraction16_script_config = FilePatchConfig(
        file_id="attraction_16",
        description="Attraction 16 Script changes",
        processing_type=FileProcessingType.NESTED_DAC_U8,
        primary_file_path="DATA/files/Attraction/At016Dat.dac",
        nested_archive_path="Temporary/PreAtArc/PreAt016Dat.dan",
        target_file_path="Script/mnAttractionInfo.fsb",
        patch_operations=[
            PatchOperation(
                offset=0x00000120,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="skip postgame check allow bonus pokemon trigger"
            ),
            PatchOperation(
                offset=0x000001cc,
                original_value=0x00020208,
                new_value=0x00020008,
                size=4,
                byteorder="big",
                description="trigger always bonus pokemon trigger"
            ),
        ]
    )
    configs.append(attraction16_script_config)
    return configs