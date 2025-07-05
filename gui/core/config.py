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
    return configs