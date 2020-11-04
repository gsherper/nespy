# 6502 Constants

# Addressing Modes
ADDR_IMM = "immediate"
ADDR_ZERO_PAGE = "zeropage"
ADDR_ZERO_PAGE_X = "zeropagex"
ADDR_ZERO_PAGE_Y = "zeropagey"
ADDR_ABS = "absolute"
ADDR_ABS_X = "absolute_x"
ADDR_ABS_Y = "absolute_y"
ADDR_INDIRECT = "indirect"
ADDR_INDIRECT_X = "indirect_x"
ADDR_INDIRECT_Y = "indirect_y"
ADDR_ACCUMULATOR = "accumulator"
ADDR_RELATIVE = "relative"
ADDR_IMPLIED = "implied"

INSTRUCTION_SET = {
    # ADC - Add Memory to Accumulator with Carry
    0x69: {"instruction": "ADC", "bytes": 2, "cycles": 2, "addressing": ADDR_IMM},
    0x65: {"instruction": "ADC", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0x75: {"instruction": "ADC", "bytes": 2, "cycles": 4, "addressing": ADDR_ZERO_PAGE_X},
    0x6D: {"instruction": "ADC", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    0x7D: {"instruction": "ADC", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_X},
    0x79: {"instruction": "ADC", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_Y},
    0x61: {"instruction": "ADC", "bytes": 2, "cycles": 6, "addressing": ADDR_INDIRECT_X},
    0x71: {"instruction": "ADC", "bytes": 2, "cycles": 5, "addressing": ADDR_INDIRECT_Y},
    # AND - AND Memory with Accumulator
    0x29: {"instruction": "AND", "bytes": 2, "cycles": 2, "addressing": ADDR_IMM},
    0x25: {"instruction": "AND", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0x35: {"instruction": "AND", "bytes": 2, "cycles": 4, "addressing": ADDR_ZERO_PAGE_X},
    0x2D: {"instruction": "AND", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    0x3D: {"instruction": "AND", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_X},
    0x39: {"instruction": "AND", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_Y},
    0x21: {"instruction": "AND", "bytes": 2, "cycles": 6, "addressing": ADDR_INDIRECT_X},
    0x31: {"instruction": "AND", "bytes": 2, "cycles": 5, "addressing": ADDR_INDIRECT_Y},
    # ASL - Shift Left One Bit (Memory or  Accumulator)
    0x0A: {"instruction": "ASL", "bytes": 1, "cycles": 2, "addressing": ADDR_ACCUMULATOR},
    0x06: {"instruction": "ASL", "bytes": 2, "cycles": 5, "addressing": ADDR_ZERO_PAGE},
    0x16: {"instruction": "ASL", "bytes": 2, "cycles": 6, "addressing": ADDR_ZERO_PAGE_X},
    0x0E: {"instruction": "ASL", "bytes": 3, "cycles": 6, "addressing": ADDR_ABS},
    0x1E: {"instruction": "ASL", "bytes": 3, "cycles": 7, "addressing": ADDR_ABS_X},
    # BCC - Branch on Carry Clear
    0x90: {"instruction": "BCC", "bytes": 2, "cycles": 2, "addressing": ADDR_RELATIVE},
    # BCS - Branch on Carry SET
    0xB0: {"instruction": "BCS", "bytes": 2, "cycles": 2, "addressing": ADDR_RELATIVE},
    # BEQ - Branch on Result Zero
    0xF0: {"instruction": "BEQ", "bytes": 2, "cycles": 2, "addressing": ADDR_RELATIVE},
    # BIT - Test Bits in Memory with Accumulator
    0x24: {"instruction": "BIT", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0x2C: {"instruction": "BIT", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    # BMI - Branch on Result Minus
    0x30: {"instruction": "BMI", "bytes": 2, "cycles": 2, "addressing": ADDR_RELATIVE},
    # BNE - Branch on Result Not Zero
    0xD0: {"instruction": "BNE", "bytes": 2, "cycles": 2, "addressing": ADDR_RELATIVE},
    # BPL - Branch on Result Plus
    0x10: {"instruction": "BPL", "bytes": 2, "cycles": 2, "addressing": ADDR_RELATIVE},
    # BRK - Force Break
    0x00: {"instruction": "BRK", "bytes": 1, "cycles": 7, "addressing": ADDR_IMPLIED},
    # BVC - Branch on Overflow Clear
    0x50: {"instruction": "BVC", "bytes": 2, "cycles": 2, "addressing": ADDR_RELATIVE},
    # BVS - Branch on Overflow Set
    0x70: {"instruction": "BVS", "bytes": 2, "cycles": 2, "addressing": ADDR_RELATIVE},
    # CLC - Clear Carry Flag
    0x18: {"instruction": "CLC", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # CLD - Clear Decimal Mode
    0xD8: {"instruction": "CLD", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # CLI - Clear Interrupt Disable Bit
    0x58: {"instruction": "CLI", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # CLV - Clear Overflow Flag
    0xB8: {"instruction": "CLI", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # CMP - Compare Memory with Accumulator
    0xC9: {"instruction": "CMP", "bytes": 2, "cycles": 2, "addressing": ADDR_IMM},
    0xC5: {"instruction": "CMP", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0xD5: {"instruction": "CMP", "bytes": 2, "cycles": 4, "addressing": ADDR_ZERO_PAGE_X},
    0xCD: {"instruction": "CMP", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    0xDD: {"instruction": "CMP", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_X},
    0xD9: {"instruction": "CMP", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_Y},
    0xC1: {"instruction": "CMP", "bytes": 2, "cycles": 6, "addressing": ADDR_INDIRECT_X},
    0xD1: {"instruction": "CMP", "bytes": 2, "cycles": 5, "addressing": ADDR_INDIRECT_Y},
    # CPX - Compare Memory with Index X
    0xE0: {"instruction": "CMP", "bytes": 2, "cycles": 2, "addressing": ADDR_IMM},
    0xE4: {"instruction": "CMP", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0xEC: {"instruction": "CMP", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    # CPY - Compare Memory with Index Y
    0xC0: {"instruction": "CMY", "bytes": 2, "cycles": 2, "addressing": ADDR_IMM},
    0xC4: {"instruction": "CMY", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0xCC: {"instruction": "CMY", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    # DEC - Decrement Memory by One
    0xC6: {"instruction": "DEC", "bytes": 2, "cycles": 5, "addressing": ADDR_ZERO_PAGE},
    0xD6: {"instruction": "DEC", "bytes": 2, "cycles": 6, "addressing": ADDR_ZERO_PAGE_X},
    0xCE: {"instruction": "DEC", "bytes": 3, "cycles": 6, "addressing": ADDR_ABS},
    0xDE: {"instruction": "DEC", "bytes": 3, "cycles": 7, "addressing": ADDR_ABS_X},
    # DEX - Decrement Index X by One
    0xCA: {"instruction": "DEX", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # DEY - Decrement Index X by One
    0x88: {"instruction": "DEY", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # EOR - Exclusive-OR Memory with Accumulator
    0x49: {"instruction": "EOR", "bytes": 2, "cycles": 2, "addressing": ADDR_IMM},
    0x45: {"instruction": "EOR", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0x55: {"instruction": "EOR", "bytes": 2, "cycles": 4, "addressing": ADDR_ZERO_PAGE_X},
    0x4D: {"instruction": "EOR", "bytes": 2, "cycles": 4, "addressing": ADDR_ABS},
    0x5D: {"instruction": "EOR", "bytes": 2, "cycles": 4, "addressing": ADDR_ABS_X},
    0x59: {"instruction": "EOR", "bytes": 2, "cycles": 4, "addressing": ADDR_ABS_Y},
    0x41: {"instruction": "EOR", "bytes": 2, "cycles": 6, "addressing": ADDR_INDIRECT_X},
    0x51: {"instruction": "EOR", "bytes": 2, "cycles": 5, "addressing": ADDR_INDIRECT_Y},
    # INC - Increment Memory By One
    0xE6: {"instruction": "INC", "bytes": 2, "cycles": 5, "addressing": ADDR_ZERO_PAGE},
    0xF6: {"instruction": "INC", "bytes": 2, "cycles": 6, "addressing": ADDR_ZERO_PAGE_X},
    0xEE: {"instruction": "INC", "bytes": 2, "cycles": 6, "addressing": ADDR_ABS},
    0xFE: {"instruction": "INC", "bytes": 2, "cycles": 7, "addressing": ADDR_ABS_X},
    # INX - Increment X By One
    0xE8: {"instruction": "INX", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # INY - Increment Y By One
    0xC8: {"instruction": "INY", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # JMP - Jump to New Location
    0x4C: {"instruction": "JMP", "bytes": 3, "cycles": 3, "addressing": ADDR_ABS},
    0x6C: {"instruction": "JMP", "bytes": 3, "cycles": 5, "addressing": ADDR_INDIRECT},
    # JSR - Jump to New Location Saving Return Address
    0x20: {"instruction": "JSR", "bytes": 3, "cycles": 6, "addressing": ADDR_ABS},
    # LDA - Load Accumulator with Memory
    0xA9: {"instruction": "LDA", "bytes": 2, "cycles": 2, "addressing": ADDR_IMM},
    0xA5: {"instruction": "LDA", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0xB5: {"instruction": "LDA", "bytes": 2, "cycles": 4, "addressing": ADDR_ZERO_PAGE_X},
    0xAD: {"instruction": "LDA", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    0xBD: {"instruction": "LDA", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_X},
    0xB9: {"instruction": "LDA", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_Y},
    0xA1: {"instruction": "LDA", "bytes": 2, "cycles": 6, "addressing": ADDR_INDIRECT_X},
    0xB1: {"instruction": "LDA", "bytes": 2, "cycles": 5, "addressing": ADDR_INDIRECT_Y},
    # LDX - Load Index X with Memory
    0xA2: {"instruction": "LDX", "bytes": 2, "cycles": 2, "addressing": ADDR_IMM},
    0xA6: {"instruction": "LDX", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0xB6: {"instruction": "LDX", "bytes": 2, "cycles": 4, "addressing": ADDR_ZERO_PAGE_Y},
    0xAE: {"instruction": "LDX", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    0xBE: {"instruction": "LDX", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_Y},
    # LDY - Load Index Y with Memory
    0xA0: {"instruction": "LDY", "bytes": 2, "cycles": 2, "addressing": ADDR_IMM},
    0xA4: {"instruction": "LDY", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0xB4: {"instruction": "LDY", "bytes": 2, "cycles": 4, "addressing": ADDR_ZERO_PAGE_X},
    0xAC: {"instruction": "LDY", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    0xBC: {"instruction": "LDY", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_X},
    # LSR - Shift One Bit Right (Memory or Accumulator)
    0x4A: {"instruction": "LSR", "bytes": 1, "cycles": 2, "addressing": ADDR_ACCUMULATOR},
    0x46: {"instruction": "LSR", "bytes": 2, "cycles": 5, "addressing": ADDR_ZERO_PAGE},
    0x56: {"instruction": "LSR", "bytes": 2, "cycles": 6, "addressing": ADDR_ZERO_PAGE_X},
    0x4E: {"instruction": "LSR", "bytes": 3, "cycles": 6, "addressing": ADDR_ABS},
    0x5E: {"instruction": "LSR", "bytes": 3, "cycles": 7, "addressing": ADDR_ABS_X},
    # NOP - No Operation
    0xEA: {"instruction": "NOP", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # ORA - OR Memory with Accumulator
    0x09: {"instruction": "ORA", "bytes": 2, "cycles": 2, "addressing": ADDR_IMM},
    0x05: {"instruction": "ORA", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0x15: {"instruction": "ORA", "bytes": 2, "cycles": 4, "addressing": ADDR_ZERO_PAGE_X},
    0x0D: {"instruction": "ORA", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    0x1D: {"instruction": "ORA", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_X},
    0x19: {"instruction": "ORA", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_Y},
    0x01: {"instruction": "ORA", "bytes": 2, "cycles": 6, "addressing": ADDR_INDIRECT_X},
    0x11: {"instruction": "ORA", "bytes": 2, "cycles": 5, "addressing": ADDR_INDIRECT_Y},
    # PHA - Push Accumulator on Stack
    0x48: {"instruction": "PHA", "bytes": 1, "cycles": 3, "addressing": ADDR_IMPLIED},
    # PHP - Push Processor Status on Stack
    0x08: {"instruction": "PHP", "bytes": 1, "cycles": 3, "addressing": ADDR_IMPLIED},
    # PLA - Pull Accumulator Status on Stack
    0x68: {"instruction": "PLA", "bytes": 1, "cycles": 4, "addressing": ADDR_IMPLIED},
    # PLP - Pull Processor Status on Stack
    0x28: {"instruction": "PLP", "bytes": 1, "cycles": 4, "addressing": ADDR_IMPLIED},
    # ROL - Rotate One Bit Left (Memory or Accumulator)
    0x2A: {"instruction": "ROL", "bytes": 1, "cycles": 2, "addressing": ADDR_ACCUMULATOR},
    0x26: {"instruction": "ROL", "bytes": 2, "cycles": 5, "addressing": ADDR_ZERO_PAGE},
    0x36: {"instruction": "ROL", "bytes": 2, "cycles": 6, "addressing": ADDR_ZERO_PAGE_X},
    0x2E: {"instruction": "ROL", "bytes": 3, "cycles": 6, "addressing": ADDR_ABS},
    0x3E: {"instruction": "ROL", "bytes": 3, "cycles": 7, "addressing": ADDR_ABS_X},
    # ROR - Rotate One Bit Right (Memory or Accumulator)
    0x6A: {"instruction": "ROL", "bytes": 1, "cycles": 2, "addressing": ADDR_ACCUMULATOR},
    0x66: {"instruction": "ROL", "bytes": 2, "cycles": 5, "addressing": ADDR_ZERO_PAGE},
    0x76: {"instruction": "ROL", "bytes": 2, "cycles": 6, "addressing": ADDR_ZERO_PAGE_X},
    0x6E: {"instruction": "ROL", "bytes": 3, "cycles": 6, "addressing": ADDR_ABS},
    0x7E: {"instruction": "ROL", "bytes": 3, "cycles": 7, "addressing": ADDR_ABS_X},
    # RTI - Return from Interrupt
    0x40: {"instruction": "RTI", "bytes": 1, "cycles": 6, "addressing": ADDR_IMPLIED},
    # RTS - Return from Subroutine
    0x60: {"instruction": "RTS", "bytes": 1, "cycles": 6, "addressing": ADDR_IMPLIED},
    # SBC - OR Memory with Accumulator
    0xE9: {"instruction": "SBC", "bytes": 2, "cycles": 2, "addressing": ADDR_IMM},
    0xE5: {"instruction": "SBC", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0xF5: {"instruction": "SBC", "bytes": 2, "cycles": 4, "addressing": ADDR_ZERO_PAGE_X},
    0xED: {"instruction": "SBC", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    0xFD: {"instruction": "SBC", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_X},
    0xF9: {"instruction": "SBC", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS_Y},
    0xE1: {"instruction": "SBC", "bytes": 2, "cycles": 6, "addressing": ADDR_INDIRECT_X},
    0xF1: {"instruction": "SBC", "bytes": 2, "cycles": 5, "addressing": ADDR_INDIRECT_Y},
    # SEC - Set Carry Flag
    0x38: {"instruction": "SEC", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # SED - Set Decimal Flag
    0xF8: {"instruction": "SED", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # SEI - Set Interrupt Disable Status
    0x78: {"instruction": "SEI", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # STA - Store Accumulator in Memory
    0x85: {"instruction": "STA", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0x95: {"instruction": "STA", "bytes": 2, "cycles": 4, "addressing": ADDR_ZERO_PAGE_X},
    0x8D: {"instruction": "STA", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    0x9D: {"instruction": "STA", "bytes": 3, "cycles": 5, "addressing": ADDR_ABS_X},
    0x99: {"instruction": "STA", "bytes": 3, "cycles": 5, "addressing": ADDR_ABS_Y},
    0x81: {"instruction": "STA", "bytes": 2, "cycles": 6, "addressing": ADDR_INDIRECT_X},
    0x91: {"instruction": "STA", "bytes": 2, "cycles": 6, "addressing": ADDR_INDIRECT_Y},
    # STX - Store Index X in Memory
    0x86: {"instruction": "STX", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0x96: {"instruction": "STX", "bytes": 2, "cycles": 4, "addressing": ADDR_ZERO_PAGE_Y},
    0x8E: {"instruction": "STX", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    # STY - Store Index Y in Memory
    0x84: {"instruction": "STX", "bytes": 2, "cycles": 3, "addressing": ADDR_ZERO_PAGE},
    0x94: {"instruction": "STX", "bytes": 2, "cycles": 4, "addressing": ADDR_ZERO_PAGE_X},
    0x8C: {"instruction": "STX", "bytes": 3, "cycles": 4, "addressing": ADDR_ABS},
    # TAX - Transfer Accumulator to Index X
    0xAA: {"instruction": "TAX", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # TAY - Transfer Accumulator to Index Y
    0xA8: {"instruction": "TAY", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # TSX - Transfer Stack Pointer to Index X
    0xBA: {"instruction": "TSX", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # TXA - Transfer Index X to Accumulator
    0x8A: {"instruction": "TXA", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # TXS - Transfer Index X to Stack Register
    0x9A: {"instruction": "TXS", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED},
    # TYA - Transfer IndexYX to Accumulator
    0x98: {"instruction": "TYA", "bytes": 1, "cycles": 2, "addressing": ADDR_IMPLIED}
}