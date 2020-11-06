from instruction_set import *

class CPU:

    def __init__(self):
        self.reg_accumulator = 0x00
        self.reg_x_index = 0x00
        self.reg_y_index = 0x00
        self.reg_status = 0x00
        self.program_counter = 0x00
        self.stack_pointer = 0x00

        # SR Flgas Register (bit 7 to bit 0)
        self.flag_negative = None
        self.flag_overflow = None
        self.flag_break = None
        self.flag_decimal = None
        self.flag_interrupt = None
        self.flag_zero = None
        self.flag_carry = None

        self.data_fetched = None
        self.address_abs = 0x0000
        self.address_rel = 0x00
        self.opcode = None
        self.cycles = 0
        pass



    def get_flag(self, flag):
        return (self.reg_status >> flag.value) & 0x1
        pass

    def update_flag(self, flag, value):
        if value:
            self.reg_status |= 0x1 << flag.value
        else:
            self.reg_status ^= 0x1 << flag.value
        pass

    def set_addr_mode(self, address_mode):
        if address_mode.value:
            getattr(self, address_mode.value)()

    def addr_immediate(self):
        print("immediate")
        self.address_abs = self.program_counter
        self.program_counter += 1
        return 0

    def addr_implied(self):
        print("addr_implied")
        self.data_fetched = self.reg_accumulator
        return 0

    def addr_zeropage(self):
        self.address_abs = self.read(self.program_counter)
        self.program_counter += 1
        self.address_abs &= 0x00FF
        return 0

    def addr_zeropage_x(self):
        self.address_abs = self.read(self.program_counter) + self.reg_x_index
        self.program_counter += 1
        self.address_abs &= 0x00FF
        return 0

    def addr_zeropage_y(self):
        self.address_abs = self.read(self.program_counter) + self.reg_y_index
        self.program_counter += 1
        self.address_abs &= 0x00FF
        return 0

    def addr_absolute(self):
        low_byte = self.read(self.program_counter)
        self.program_counter += 1
        high_byte = self.read(self.program_counter)
        self.program_counter += 1
        self.address_abs = high_byte << 8 | low_byte
        return 0

    def addr_absolute_x(self):
        low_byte = self.read(self.program_counter)
        self.program_counter += 1
        high_byte = self.read(self.program_counter)
        self.program_counter += 1
        self.address_abs = (high_byte << 8 | low_byte) + self.reg_x_index
        if self.address_abs & 0xFF00 != low_byte << 8:
            return 1
        return 0

    def addr_absolute_y(self):
        low_byte = self.read(self.program_counter)
        self.program_counter += 1
        high_byte = self.read(self.program_counter)
        self.program_counter += 1
        self.address_abs = (high_byte << 8 | low_byte)+ self.reg_y_index
        if self.address_abs & 0xFF00 != high_byte << 8:
            return 1
        return 0

    def addr_indirect(self):
        low_ptr = self.read(self.program_counter)
        self.program_counter += 1
        high_byte = self.read(self.program_counter)
        self.program_counter += 1
        ptr = high_byte << 8 | low_ptr

        if low_ptr == 0x00FF:
            # simulate hardware bug
            self.address_abs = self.read(ptr & 0xFF00) << 8 | self.read(ptr + 0)
        else:
            self.address_abs = self.read(ptr + 1) << 8 | self.read(ptr + 0)
        return 0

    def addr_indirect_x(self):
        # indirect addressing of zero page with x offset
        addr = self.read(self.program_counter)
        self.program_counter += 1
        low_byte = self.read((addr + self.reg_x_index) & 0X00FF)
        high_byte = self.read((addr + self.reg_x_index + 1) & 0x00FF)
        self.address_abs = high_byte << 8 | low_byte
        return 0

    def addr_indirect_y(self):
        # indirect addressing of zero page with y offset
        addr = self.read(self.program_counter)
        self.program_counter += 1
        low_byte = self.read(addr & 0x00FF)
        high_byte = self.read((addr+1) & 0x00FF)
        self.address_abs = high_byte << 8 | low_byte
        self.address_abs += self.reg_y_index

        if (self.address_abs & 0xFF00) != high_byte << 8:
            return 1
        return 0

    def addr_relative(self):
        self.address_rel = self.read(self.program_counter)
        self.program_counter += 1
        # restrict jumping >= 0x80 locations
        # used for signed number
        if self.address_rel & 0x80:
            self.address_rel |= 0xFF00
        return 0

    def fetch(self):
        if self.opcode["addr_mode"] != AddrMode.ADDR_IMM:
            self.data_fetched
        return self.data_fetched

    def op_and(self):

        data = self.fetch()
        self.reg_accumulator &= data
        self.update_flag(Flags.Z, self.reg_accumulator == 0x00)
        self.update_flag(Flags.N, self.reg_accumulator & 0x80)
        return 1

    def op_bcs(self):

        if self.get_flag(Flags.C) == 1:
            self.cycles += 1
            self.address_abs = self.program_counter + self.address_rel

            if (self.address_abs & 0xFF00) != (self.program_counter & 0xFF00):
                self.cycles += 1

            self.program_counter = self.address_abs
        return 0

    def op_bcc(self):

        if self.get_flag(Flags.C) == 0:
            self.cycles += 1
            self.address_abs = self.program_counter + self.address_rel

            if (self.address_abs & 0xFF00) != (self.program_counter & 0xFF00):
                self.cycles += 1

            self.program_counter = self.address_abs
        return 0

    def op_beq(self):

        if self.get_flag(Flags.Z) == 1:
            self.cycles += 1
            self.address_abs = self.program_counter + self.address_rel

            if (self.address_abs & 0xFF00) != (self.program_counter & 0xFF00):
                self.cycles += 1

            self.program_counter = self.address_abs
        return 0

    def op_bmi(self):

        if self.get_flag(Flags.N) == 1:
            self.cycles += 1
            self.address_abs = self.program_counter + self.address_rel

            if (self.address_abs & 0xFF00) != (self.program_counter & 0xFF00):
                self.cycles += 1

            self.program_counter = self.address_abs
        return 0

    def op_bne(self):

        if self.get_flag(Flags.Z) == 0:
            self.cycles += 1
            self.address_abs = self.program_counter + self.address_rel

            if (self.address_abs & 0xFF00) != (self.program_counter & 0xFF00):
                self.cycles += 1

            self.program_counter = self.address_abs
        return 0

    def op_bpl(self):

        if self.get_flag(Flags.N) == 0:
            self.cycles += 1
            self.address_abs = self.program_counter + self.address_rel

            if (self.address_abs & 0xFF00) != (self.program_counter & 0xFF00):
                self.cycles += 1

            self.program_counter = self.address_abs
        return 0

    def op_bvc(self):

        if self.get_flag(Flags.V) == 0:
            self.cycles += 1
            self.address_abs = self.program_counter + self.address_rel

            if (self.address_abs & 0xFF00) != (self.program_counter & 0xFF00):
                self.cycles += 1

            self.program_counter = self.address_abs
        return 0

    def op_bvs(self):

        if self.get_flag(Flags.V) == 1:
            self.cycles += 1
            self.address_abs = self.program_counter + self.address_rel

            if (self.address_abs & 0xFF00) != (self.program_counter & 0xFF00):
                self.cycles += 1

            self.program_counter = self.address_abs
        return 0

    def op_clc(self):
        self.update_flag(Flags.C, 0)


    def nmi(self):
        # Async
        pass

    def iqr(self):
        # Async
        pass

    def reset(self):
        # Async
        pass

    def execute_opcode(self, mnemonic):
        pass

    def clock(self):
        if self.cycles == 0:
            self.opcode = self.read(self.program_counter)
            self.program_counter += 1
            self.opcode = INSTRUCTION_SET[self.opcode]
            self.cycles = self.opcode["cycles"]
            more_cycle1 = self.set_addr_mode(self.opcode["addr_mode"])
            more_cycle2 = self.execute_opcode(self.opcode["mnemonic"])
            if more_cycle1 and more_cycle2:
                self.cycles += 1
        self.cycles -= 1


    def read(self, address):
        print('read')
        return self.bus.read(address=address, read_only=False)

    def write(self, address, data):
        self.bus.write(address=address, data=data)




