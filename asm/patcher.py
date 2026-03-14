from asm.fs_helpers import *


def split_pointer_into_high_and_low_half_for_hardcoding(pointer):
    high_halfword = (pointer & 0xFFFF0000) >> 16
    low_halfword = pointer & 0xFFFF

    if low_halfword >= 0x8000:
        # If the low halfword has the highest bit set, it will be considered a negative number.
        # Therefore we need to add 1 to the high halfword (equivalent to adding 0x10000) to compensate for the low halfword being negated.
        high_halfword = high_halfword + 1

    return high_halfword, low_halfword


def apply_dol_patch(self, dol, patch):
    for org_address, patchlet in patch.items():
        new_bytes = patchlet["Data"]

        free_space_start = self.free_space_start_offsets["main.dol"]

        if org_address >= free_space_start:
            add_free_space_section_to_main_dol(self, dol, new_bytes)
        else:
            dol.write_data(
                write_and_pack_bytes, org_address, new_bytes, "B" * len(new_bytes)
            )


def add_free_space_section_to_main_dol(self, main_dol, new_bytes):
    dol_section = main_dol.sections[2]
    patch_length = len(new_bytes)

    if dol_section.size != 0:
        raise Exception(
            "Having multiple separate free space directives for main.dol is not currently supported."
        )

    # First add a new text section to the dol (Text2).
    dol_section.offset = self.ORIGINAL_DOL_SIZE  # Set the file offset of new Text2 section (which will be the original
    # end of the file, where we put the patch)
    dol_section.address = self.ORIGINAL_FREE_SPACE_RAM_ADDRESS  # Write loading address of the new Text2 section
    dol_section.size = patch_length  # Write length of the new Text2 section

    # Next write our custom code to the end of the dol file.
    main_dol.write_data(
        write_and_pack_bytes,
        self.ORIGINAL_FREE_SPACE_RAM_ADDRESS,
        new_bytes,
        "B" * len(new_bytes),
    )

    # Next we need to change a hardcoded pointer to where free space begins. Otherwise the game will overwrite the custom code.
    padded_patch_length = (
                                  patch_length + 3
                          ) & ~3  # Pad length of patch to next 4 just in case
    new_start_pointer_for_default_thread = (
            self.ORIGINAL_FREE_SPACE_RAM_ADDRESS + padded_patch_length
    )  # New free space pointer after our custom code
    high_halfword, low_halfword = split_pointer_into_high_and_low_half_for_hardcoding(
        new_start_pointer_for_default_thread
    )
    # Now update the asm instructions that load this hardcoded pointer.
    main_dol.write_data(write_u32, self.pointer1_high, 0x3CA00000 | high_halfword)
    main_dol.write_data(write_u32, self.pointer1_low, 0x38A50000 | low_halfword)
    # more hardcoded pointers that come later
    new_end_pointer_for_default_thread = new_start_pointer_for_default_thread + 0x10000
    high_halfword, low_halfword = split_pointer_into_high_and_low_half_for_hardcoding(
        new_end_pointer_for_default_thread
    )
    main_dol.write_data(write_u32, self.pointer2_high, 0x3C600000 | high_halfword)
    main_dol.write_data(write_u32, self.pointer2_low, 0x38630000 | low_halfword)
    # main_dol.write_data(write_u32, 0x803A2988, 0x3C600000 | high_halfword)  # unused by pokepark
    # main_dol.write_data(write_u32, 0x803A2990, 0x38630000 | low_halfword)
    main_dol.write_data(write_u32, self.pointer3_high, 0x3C600000 | high_halfword)
    main_dol.write_data(write_u32, self.pointer3_low, 0x38630000 | low_halfword)
    high_halfword = (new_end_pointer_for_default_thread & 0xFFFF0000) >> 16
    low_halfword = new_end_pointer_for_default_thread & 0xFFFF
    # default stack pointer
    main_dol.write_data(write_u32, self.pointer4_high, 0x3C200000 | high_halfword)
    main_dol.write_data(write_u32, self.pointer4_low, 0x60210000 | low_halfword)

    # Original thread start pointer: 803FCFA8 (must be updated)
    # Original stack end pointer (r1): 8040CFA8 (must be updated)
    # Original rtoc pointer (r2): 803FFD00 (must NOT be updated)
    # Original read-write small data area pointer (r13): 803FE0E0 (must NOT be updated)
