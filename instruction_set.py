# 6502 Constants

from enum import Enum


class Flags(Enum):

    C = 1 << 0  # Carry
    Z = 1 << 1  # Zero
    I = 1 << 2  # Disable Interrupts
    D = 1 << 3  # Decimal Mode
    B = 1 << 4  # Break
    U = 1 << 5  # Unused
    V = 1 << 6  # Overflow
    N = 1 << 7   # Negative


class AddrMode(Enum):

    # Addressing Modes
    ADDR_ABS = "addr_absolute"  #
    ADDR_ABS_X = "addr_absolute_x"  #
    ADDR_ABS_Y = "addr_absolute_y"  #
    ADDR_ACCUMULATOR = "addr_accumulator"
    ADDR_INDIRECT = "addr_indirect" #
    ADDR_INDIRECT_X = "addr_indirect_x" #
    ADDR_INDIRECT_Y = "addr_indirect_y" #
    ADDR_IMM = "addr_immediate"  #
    ADDR_IMPLIED = "addr_implied"  #
    ADDR_RELATIVE = "addr_relative"
    ADDR_ZERO_PAGE = "addr_zeropage"  #
    ADDR_ZERO_PAGE_X = "addr_zeropage_x"  #
    ADDR_ZERO_PAGE_Y = "addr_zeropage_y"  #

INSTRUCTION_SET = {
    ## ADC - Add Memory to Accumulator with Carry
    0x69: {"mnemonic": "ADC", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_IMM},
    0x65: {"mnemonic": "ADC", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0x75: {"mnemonic": "ADC", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0x6D: {"mnemonic": "ADC", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    0x7D: {"mnemonic": "ADC", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_X},
    0x79: {"mnemonic": "ADC", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_Y},
    0x61: {"mnemonic": "ADC", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_INDIRECT_X},
    0x71: {"mnemonic": "ADC", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_INDIRECT_Y},
    ## AND - AND Memory with Accumulator
    0x29: {"mnemonic": "AND", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_IMM},
    0x25: {"mnemonic": "AND", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0x35: {"mnemonic": "AND", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0x2D: {"mnemonic": "AND", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    0x3D: {"mnemonic": "AND", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_X},
    0x39: {"mnemonic": "AND", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_Y},
    0x21: {"mnemonic": "AND", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_INDIRECT_X},
    0x31: {"mnemonic": "AND", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_INDIRECT_Y},
    # ASL - Shift Left One Bit (Memory or  Accumulator)
    0x0A: {"mnemonic": "ASL", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_ACCUMULATOR},
    0x06: {"mnemonic": "ASL", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0x16: {"mnemonic": "ASL", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0x0E: {"mnemonic": "ASL", "bytes": 3, "cycles": 6, "addr_mode": AddrMode.ADDR_ABS},
    0x1E: {"mnemonic": "ASL", "bytes": 3, "cycles": 7, "addr_mode": AddrMode.ADDR_ABS_X},
    ## BCC - Branch on Carry Clear
    0x90: {"mnemonic": "BCC", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_RELATIVE},
    ## BCS - Branch on Carry SET
    0xB0: {"mnemonic": "BCS", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_RELATIVE},
    ## BEQ - Branch on Result Zero
    0xF0: {"mnemonic": "BEQ", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_RELATIVE},
    # BIT - Test Bits in Memory with Accumulator
    0x24: {"mnemonic": "BIT", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0x2C: {"mnemonic": "BIT", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    ## BMI - Branch on Result Minus
    0x30: {"mnemonic": "BMI", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_RELATIVE},
    ## BNE - Branch on Result Not Zero
    0xD0: {"mnemonic": "BNE", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_RELATIVE},
    ## BPL - Branch on Result Plus
    0x10: {"mnemonic": "BPL", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_RELATIVE},
    # BRK - Force Break
    0x00: {"mnemonic": "BRK", "bytes": 1, "cycles": 7, "addr_mode": AddrMode.ADDR_IMPLIED},
    ## BVC - Branch on Overflow Clear
    0x50: {"mnemonic": "BVC", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_RELATIVE},
    ## BVS - Branch on Overflow Set
    0x70: {"mnemonic": "BVS", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_RELATIVE},
    ## CLC - Clear Carry Flag
    0x18: {"mnemonic": "CLC", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    ## CLD - Clear Decimal Mode
    0xD8: {"mnemonic": "CLD", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    ## CLI - Clear Interrupt Disable Bit
    0x58: {"mnemonic": "CLI", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    ## CLV - Clear Overflow Flag
    0xB8: {"mnemonic": "CLI", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # CMP - Compare Memory with Accumulator
    0xC9: {"mnemonic": "CMP", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_IMM},
    0xC5: {"mnemonic": "CMP", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0xD5: {"mnemonic": "CMP", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0xCD: {"mnemonic": "CMP", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    0xDD: {"mnemonic": "CMP", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_X},
    0xD9: {"mnemonic": "CMP", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_Y},
    0xC1: {"mnemonic": "CMP", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_INDIRECT_X},
    0xD1: {"mnemonic": "CMP", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_INDIRECT_Y},
    # CPX - Compare Memory with Index X
    0xE0: {"mnemonic": "CMP", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_IMM},
    0xE4: {"mnemonic": "CMP", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0xEC: {"mnemonic": "CMP", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    # CPY - Compare Memory with Index Y
    0xC0: {"mnemonic": "CMY", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_IMM},
    0xC4: {"mnemonic": "CMY", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0xCC: {"mnemonic": "CMY", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    # DEC - Decrement Memory by One
    0xC6: {"mnemonic": "DEC", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0xD6: {"mnemonic": "DEC", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0xCE: {"mnemonic": "DEC", "bytes": 3, "cycles": 6, "addr_mode": AddrMode.ADDR_ABS},
    0xDE: {"mnemonic": "DEC", "bytes": 3, "cycles": 7, "addr_mode": AddrMode.ADDR_ABS_X},
    # DEX - Decrement Index X by One
    0xCA: {"mnemonic": "DEX", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # DEY - Decrement Index X by One
    0x88: {"mnemonic": "DEY", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # EOR - Exclusive-OR Memory with Accumulator
    0x49: {"mnemonic": "EOR", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_IMM},
    0x45: {"mnemonic": "EOR", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0x55: {"mnemonic": "EOR", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0x4D: {"mnemonic": "EOR", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    0x5D: {"mnemonic": "EOR", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_X},
    0x59: {"mnemonic": "EOR", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_Y},
    0x41: {"mnemonic": "EOR", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_INDIRECT_X},
    0x51: {"mnemonic": "EOR", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_INDIRECT_Y},
    # INC - Increment Memory By One
    0xE6: {"mnemonic": "INC", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0xF6: {"mnemonic": "INC", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0xEE: {"mnemonic": "INC", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_ABS},
    0xFE: {"mnemonic": "INC", "bytes": 2, "cycles": 7, "addr_mode": AddrMode.ADDR_ABS_X},
    # INX - Increment X By One
    0xE8: {"mnemonic": "INX", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # INY - Increment Y By One
    0xC8: {"mnemonic": "INY", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # JMP - Jump to New Location
    0x4C: {"mnemonic": "JMP", "bytes": 3, "cycles": 3, "addr_mode": AddrMode.ADDR_ABS},
    0x6C: {"mnemonic": "JMP", "bytes": 3, "cycles": 5, "addr_mode": AddrMode.ADDR_INDIRECT},
    # JSR - Jump to New Location Saving Return Address
    0x20: {"mnemonic": "JSR", "bytes": 3, "cycles": 6, "addr_mode": AddrMode.ADDR_ABS},
    # LDA - Load Accumulator with Memory
    0xA9: {"mnemonic": "LDA", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_IMM},
    0xA5: {"mnemonic": "LDA", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0xB5: {"mnemonic": "LDA", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0xAD: {"mnemonic": "LDA", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    0xBD: {"mnemonic": "LDA", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_X},
    0xB9: {"mnemonic": "LDA", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_Y},
    0xA1: {"mnemonic": "LDA", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_INDIRECT_X},
    0xB1: {"mnemonic": "LDA", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_INDIRECT_Y},
    # LDX - Load Index X with Memory
    0xA2: {"mnemonic": "LDX", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_IMM},
    0xA6: {"mnemonic": "LDX", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0xB6: {"mnemonic": "LDX", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ZERO_PAGE_Y},
    0xAE: {"mnemonic": "LDX", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    0xBE: {"mnemonic": "LDX", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_Y},
    # LDY - Load Index Y with Memory
    0xA0: {"mnemonic": "LDY", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_IMM},
    0xA4: {"mnemonic": "LDY", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0xB4: {"mnemonic": "LDY", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0xAC: {"mnemonic": "LDY", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    0xBC: {"mnemonic": "LDY", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_X},
    # LSR - Shift One Bit Right (Memory or Accumulator)
    0x4A: {"mnemonic": "LSR", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_ACCUMULATOR},
    0x46: {"mnemonic": "LSR", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0x56: {"mnemonic": "LSR", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0x4E: {"mnemonic": "LSR", "bytes": 3, "cycles": 6, "addr_mode": AddrMode.ADDR_ABS},
    0x5E: {"mnemonic": "LSR", "bytes": 3, "cycles": 7, "addr_mode": AddrMode.ADDR_ABS_X},
    # NOP - No Operation
    0xEA: {"mnemonic": "NOP", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # ORA - OR Memory with Accumulator
    0x09: {"mnemonic": "ORA", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_IMM},
    0x05: {"mnemonic": "ORA", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0x15: {"mnemonic": "ORA", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0x0D: {"mnemonic": "ORA", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    0x1D: {"mnemonic": "ORA", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_X},
    0x19: {"mnemonic": "ORA", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_Y},
    0x01: {"mnemonic": "ORA", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_INDIRECT_X},
    0x11: {"mnemonic": "ORA", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_INDIRECT_Y},
    ## PHA - Push Accumulator on Stack
    0x48: {"mnemonic": "PHA", "bytes": 1, "cycles": 3, "addr_mode": AddrMode.ADDR_IMPLIED},
    ## PHP - Push Processor Status on Stack
    0x08: {"mnemonic": "PHP", "bytes": 1, "cycles": 3, "addr_mode": AddrMode.ADDR_IMPLIED},
    ## PLA - Pull Accumulator Status on Stack
    0x68: {"mnemonic": "PLA", "bytes": 1, "cycles": 4, "addr_mode": AddrMode.ADDR_IMPLIED},
    ## PLP - Pull Processor Status on Stack
    0x28: {"mnemonic": "PLP", "bytes": 1, "cycles": 4, "addr_mode": AddrMode.ADDR_IMPLIED},
    # ROL - Rotate One Bit Left (Memory or Accumulator)
    0x2A: {"mnemonic": "ROL", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_ACCUMULATOR},
    0x26: {"mnemonic": "ROL", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0x36: {"mnemonic": "ROL", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0x2E: {"mnemonic": "ROL", "bytes": 3, "cycles": 6, "addr_mode": AddrMode.ADDR_ABS},
    0x3E: {"mnemonic": "ROL", "bytes": 3, "cycles": 7, "addr_mode": AddrMode.ADDR_ABS_X},
    # ROR - Rotate One Bit Right (Memory or Accumulator)
    0x6A: {"mnemonic": "ROL", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_ACCUMULATOR},
    0x66: {"mnemonic": "ROL", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0x76: {"mnemonic": "ROL", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0x6E: {"mnemonic": "ROL", "bytes": 3, "cycles": 6, "addr_mode": AddrMode.ADDR_ABS},
    0x7E: {"mnemonic": "ROL", "bytes": 3, "cycles": 7, "addr_mode": AddrMode.ADDR_ABS_X},
    ## RTI - Return from Interrupt
    0x40: {"mnemonic": "RTI", "bytes": 1, "cycles": 6, "addr_mode": AddrMode.ADDR_IMPLIED},
    # RTS - Return from Subroutine
    0x60: {"mnemonic": "RTS", "bytes": 1, "cycles": 6, "addr_mode": AddrMode.ADDR_IMPLIED},
    ## SBC - OR Memory with Accumulator
    0xE9: {"mnemonic": "SBC", "bytes": 2, "cycles": 2, "addr_mode": AddrMode.ADDR_IMM},
    0xE5: {"mnemonic": "SBC", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0xF5: {"mnemonic": "SBC", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0xED: {"mnemonic": "SBC", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    0xFD: {"mnemonic": "SBC", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_X},
    0xF9: {"mnemonic": "SBC", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS_Y},
    0xE1: {"mnemonic": "SBC", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_INDIRECT_X},
    0xF1: {"mnemonic": "SBC", "bytes": 2, "cycles": 5, "addr_mode": AddrMode.ADDR_INDIRECT_Y},
    # SEC - Set Carry Flag
    0x38: {"mnemonic": "SEC", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # SED - Set Decimal Flag
    0xF8: {"mnemonic": "SED", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # SEI - Set Interrupt Disable Status
    0x78: {"mnemonic": "SEI", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # STA - Store Accumulator in Memory
    0x85: {"mnemonic": "STA", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0x95: {"mnemonic": "STA", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0x8D: {"mnemonic": "STA", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    0x9D: {"mnemonic": "STA", "bytes": 3, "cycles": 5, "addr_mode": AddrMode.ADDR_ABS_X},
    0x99: {"mnemonic": "STA", "bytes": 3, "cycles": 5, "addr_mode": AddrMode.ADDR_ABS_Y},
    0x81: {"mnemonic": "STA", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_INDIRECT_X},
    0x91: {"mnemonic": "STA", "bytes": 2, "cycles": 6, "addr_mode": AddrMode.ADDR_INDIRECT_Y},
    # STX - Store Index X in Memory
    0x86: {"mnemonic": "STX", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0x96: {"mnemonic": "STX", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ZERO_PAGE_Y},
    0x8E: {"mnemonic": "STX", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    # STY - Store Index Y in Memory
    0x84: {"mnemonic": "STX", "bytes": 2, "cycles": 3, "addr_mode": AddrMode.ADDR_ZERO_PAGE},
    0x94: {"mnemonic": "STX", "bytes": 2, "cycles": 4, "addr_mode": AddrMode.ADDR_ZERO_PAGE_X},
    0x8C: {"mnemonic": "STX", "bytes": 3, "cycles": 4, "addr_mode": AddrMode.ADDR_ABS},
    # TAX - Transfer Accumulator to Index X
    0xAA: {"mnemonic": "TAX", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # TAY - Transfer Accumulator to Index Y
    0xA8: {"mnemonic": "TAY", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # TSX - Transfer Stack Pointer to Index X
    0xBA: {"mnemonic": "TSX", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # TXA - Transfer Index X to Accumulator
    0x8A: {"mnemonic": "TXA", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # TXS - Transfer Index X to Stack Register
    0x9A: {"mnemonic": "TXS", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED},
    # TYA - Transfer IndexYX to Accumulator
    0x98: {"mnemonic": "TYA", "bytes": 1, "cycles": 2, "addr_mode": AddrMode.ADDR_IMPLIED}
}