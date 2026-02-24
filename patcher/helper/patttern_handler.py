from typing import Literal, Union

from patcher.helper.entrance_exit_names import ABSOL_S_HURDLE_BOUNCE_ATTRACTION_ATTRACTION_MENU, \
    BASTIODON_S_PANEL_CRUSH_ATTRACTION_ATTRACTION_MENU, \
    BLAZIKEN_S_BOULDER_BASH_ATTRACTION_ATTRACTION_MENU, BULBASAUR_S_DARING_DASH_ATTRACTION_ATTRACTION_MENU, \
    DUSKNOIR_S_SPEED_SLAM_ATTRACTION_ATTRACTION_MENU, EMPOLEON_S_SNOW_SLIDE_ATTRACTION_ATTRACTION_MENU, \
    GYARADOS_AQUA_DASH_ATTRACTION_ATTRACTION_MENU, \
    PELIPPER_S_CIRCLE_CIRCUIT_ATTRACTION_ATTRACTION_MENU, \
    RAYQUAZA_S_BALLOON_PANIC_ATTRACTION_ATTRACTION_MENU, RHYPERIOR_S_BUMPER_BURN_ATTRACTION_ATTRACTION_MENU, \
    ROTOM_S_SPOOKY_SHOOT_EM_UP_ATTRACTION_ATTRACTION_MENU, \
    SALAMENCE_S_SKY_RACE_ATTRACTION_ATTRACTION_MENU, TANGROWTH_S_SWING_ALONG_ATTRACTION_ATTRACTION_MENU, \
    VENUSAUR_S_VINE_SWING_ATTRACTION_ATTRACTION_MENU
from patcher.helper.exit_to_zone_data import ZoneKey, exit_to_zone_data
from patcher.models.models import Instruction, PatternMatch, MemoryData, PatchPattern


def parse_pattern_bytes(pattern_str: str):
    return [int(b, 16) if b != "??" else None for b in pattern_str.strip().split()]


def match_at(data: bytearray, offset: int, pattern: list[int | None]):
    for i, pat_byte in enumerate(pattern):
        if pat_byte is not None and data[offset + i] != pat_byte:
            return False
    return True


def search_pattern(data: bytearray, pattern_def: list[Instruction]):
    matches: list[PatternMatch] = []
    max_offset = max(pattern.offset + len(pattern.pattern) for pattern in pattern_def)
    anchor_pattern = next(
        (pattern for pattern in pattern_def
         if pattern.offset == 0),
        None
    )
    anchor_pattern_bytes = bytes(anchor_pattern.pattern)
    start_offset = 0
    while True:
        base = data.find(anchor_pattern_bytes, start_offset)
        if base == -1:  # No more occurrences found
            break

        if base + max_offset > len(data):
            break

        matched = {}
        for pattern in pattern_def:
            if base + pattern.offset + len(pattern.pattern) <= len(data) and match_at(
                    data, base + pattern.offset,
                    pattern.pattern
            ):
                matched[pattern.identifier] = MemoryData(
                    address=base + pattern.offset,
                    value=data[base + pattern.offset:base + pattern.offset + 0x4]
                )

            else:
                break
        else:
            matches.append(
                PatternMatch(
                    base_address=base,
                    matched_instructions=matched
                )
            )

        # Move to next potential position
        start_offset = base + 1

    return matches


def search_all_pattern(data: bytearray, patch_def: PatchPattern):
    patch_def.matchesJP = search_pattern(data, patch_def.patternJP)
    patch_def.matchesPAL = search_pattern(data, patch_def.patternPAL)
    patch_def.matchesNA = search_pattern(data, patch_def.patternNA)

    if not patch_def.matchesJP and not patch_def.matchesPAL and not patch_def.matchesNA:
        print(f"ERROR: No match found for pattern: {patch_def.name}")
        raise ValueError(f"ERROR: No match found for pattern: {patch_def.name}")

    ambiguous_regions = []
    if len(patch_def.matchesJP) > 1:
        ambiguous_regions.append(f"JP({len(patch_def.matchesJP)})")
    if len(patch_def.matchesPAL) > 1:
        ambiguous_regions.append(f"PAL({len(patch_def.matchesPAL)})")
    if len(patch_def.matchesNA) > 1:
        ambiguous_regions.append(f"NA({len(patch_def.matchesNA)})")

    if ambiguous_regions:
        error_msg = f"ERROR: Ambiguous matches for pattern: {patch_def.name} - {', '.join(ambiguous_regions)}"
        print(error_msg)
        raise ValueError(error_msg)

    print(f"Pattern {patch_def.name} matched in region: {patch_def.get_matched_region()}")


def compute_call_instruction_fsb(offset: int, patch_patterns: list[PatchPattern], pattern_name: str):
    target_pattern = find_pattern_by_name(patch_patterns, pattern_name)
    new_function_address = target_pattern.base_address
    branch_offset = new_function_address - (offset + 0x4)
    operand = branch_offset // 4

    if not (-0x8000 <= operand <= 0x7FFF):
        raise ValueError(f"Operand out of 16-bit signed range: {operand:#x}")

    operand_bytes = operand.to_bytes(2, 'big', signed=True)
    instruction_bytes = operand_bytes + b'\x00\x03'

    print(
        f"call from offset 0x{offset:08X} to 0x{new_function_address:08X} "
        f"→ offset 0x{branch_offset & 0xFFFFFFFF:08X} "
        f"→ instruction 0x{int.from_bytes(instruction_bytes, 'big'):08X}"
    )
    return instruction_bytes


def get_num_battle_count_from_dict_as_instruction(plando_dict):
    battle_count: int = plando_dict["Options"]["num_required_battle_count"]
    if not (0x0000 <= battle_count <= 0xFFFF):
        raise ValueError(f"Invalid Battle Count: {battle_count}")
    battle_count_as_bytes = battle_count.to_bytes(2, byteorder="big")
    battle_count_instruction = battle_count_as_bytes + b'\x00\x10'
    print(f"writing battle Count: {battle_count}")
    return battle_count_instruction


def get_exit_zone_area_position_data(plando_dict, entrance: str, zone_key: ZoneKey):

    exit: str = plando_dict["Entrances"][entrance]

    id = exit_to_zone_data[exit][zone_key]
    print(f"{entrance}  -> {exit} : {id}")

    id_as_bytes = id.to_bytes(2, byteorder="big")
    id_instruction = id_as_bytes + b'\x00\x10'

    return id_instruction


def patch_taxi_stop(plando_dict):
    if plando_dict["Options"]["unlock_fast_travel_with_taxi_stop"]:
        return None
    return (0x00010010).to_bytes(4, 'big')


def get_attraction_id_from_dict(plando_dict, entrance: str):
    exit_to_id: dict[str, int] = {
        BULBASAUR_S_DARING_DASH_ATTRACTION_ATTRACTION_MENU: 0xf,
        VENUSAUR_S_VINE_SWING_ATTRACTION_ATTRACTION_MENU: 0x2,
        PELIPPER_S_CIRCLE_CIRCUIT_ATTRACTION_ATTRACTION_MENU: 0x6,
        GYARADOS_AQUA_DASH_ATTRACTION_ATTRACTION_MENU: 0x5,
        EMPOLEON_S_SNOW_SLIDE_ATTRACTION_ATTRACTION_MENU: 0x8,
        BASTIODON_S_PANEL_CRUSH_ATTRACTION_ATTRACTION_MENU: 0x9,
        RHYPERIOR_S_BUMPER_BURN_ATTRACTION_ATTRACTION_MENU: 0xa,
        BLAZIKEN_S_BOULDER_BASH_ATTRACTION_ATTRACTION_MENU: 0xb,
        DUSKNOIR_S_SPEED_SLAM_ATTRACTION_ATTRACTION_MENU: 0x4,
        TANGROWTH_S_SWING_ALONG_ATTRACTION_ATTRACTION_MENU: 0x3,
        ROTOM_S_SPOOKY_SHOOT_EM_UP_ATTRACTION_ATTRACTION_MENU: 0xc,
        ABSOL_S_HURDLE_BOUNCE_ATTRACTION_ATTRACTION_MENU: 0x0,
        SALAMENCE_S_SKY_RACE_ATTRACTION_ATTRACTION_MENU: 0xe,
        RAYQUAZA_S_BALLOON_PANIC_ATTRACTION_ATTRACTION_MENU: 0x1
    }

    exit: str = plando_dict["Entrances"][entrance]

    id = exit_to_id[exit]
    attractionid_as_bytes = id.to_bytes(2, byteorder="big")
    attractionid_instruction = attractionid_as_bytes + b'\x00\x10'
    print(f"writing attraction Id: {id}")
    return attractionid_instruction


def get_num_skygarden_prisma_count_from_dict_as_instruction(plando_dict):
    prisma_count: int = plando_dict["Options"]["num_required_prisma_count_skygarden"]
    if not (0x0000 <= prisma_count <= 0xe):
        raise ValueError(f"Invalid prisma Count: {prisma_count}")
    prisma_count_as_bytes = prisma_count.to_bytes(2, byteorder="big")
    prisma_count_instruction = prisma_count_as_bytes + b'\x00\x10'
    print(f"writing prisma Count from option: {prisma_count}")
    return prisma_count_instruction


def create_lstr_instruction_fsb(patch_patterns: list[PatchPattern], start_pattern_name: str,
                                target_pattern_name: str):
    start_pattern = find_pattern_by_name(patch_patterns, start_pattern_name)
    target_pattern = find_pattern_by_name(patch_patterns, target_pattern_name)

    string_offset = target_pattern.base_address - start_pattern.base_address
    string_offset_as_bytes = string_offset.to_bytes(3, "big")
    lstr_instruction = string_offset_as_bytes + b'\x13'
    print(f"writing lstr instruction: 0x{int.from_bytes(lstr_instruction, 'big'):08X}")

    return lstr_instruction


def find_pattern_by_name(patterns: list[PatchPattern], name: str):
    matches = next((p for p in patterns if p.name == name), None).get_matches()
    if len(matches) > 1:
        raise ValueError("ambiguous match for pattern name: ", name)
    if len(matches) == 0:
        raise ValueError("no match found for pattern name: ", name)

    return matches[0]


def compute_jmp_instruction_fsb(offset: int, target_identifier: int, patch_patterns: list[PatchPattern],
                                pattern_name: str,
                                condition: Literal["jmp"] | Literal["jnz"] | Literal["jz"] = "jmp"):
    pattern = find_pattern_by_name(patch_patterns, pattern_name)
    target_address = pattern.matched_instructions.get(target_identifier).address

    branch_offset = target_address - (offset + 0x4)
    operand = branch_offset // 4

    if not (-0x8000 <= operand <= 0x7FFF):
        raise ValueError(f"Operand out of 16-bit signed range: {operand:#x}")
    condition_dict = {
        "jmp": b'\x00',
        "jnz": b'\x01',
        "jz": b'\x02'
    }
    condition_bit = condition_dict.get(condition)
    operand_bytes = operand.to_bytes(2, 'big', signed=True)
    instruction_bytes = operand_bytes + condition_bit + b'\x08'

    print(
        f"jmp from offset 0x{offset:08X} to 0x{target_address:08X} "
        f"→ offset 0x{branch_offset & 0xFFFFFFFF:08X} "
        f"→ instruction 0x{int.from_bytes(instruction_bytes, 'big'):08X}"
    )
    return instruction_bytes
