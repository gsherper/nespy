from instruction_set import *

class CPU:

    def __init__(self):
        self.reg_accumulator = None
        self.reg_x_index = None
        self.reg_y_index = None
        self.reg_status = None
        self.program_counter = None
        self.stack_pointer = None
        self.data_fetched = None
        self.address_abs = None
        self.address_rel = None
        self.op_code = None
        self.cycles = 0
        self.bus = None

    def reset(self):
        # Async
        self.reg_accumulator = 0x00
        self.reg_x_index = 0x00
        self.reg_y_index = 0x00
        self.reg_status = 0x00

        self.address_abs = 0xFFFC
        lo = self.read(self.address_abs + 0)
        hi = self.read(self.address_abs + 1)
        self.program_counter = (hi << 8) | lo

        self.stack_pointer = 0xFF
        self.data_fetched = 0x00
        self.address_abs = 0x00
        self.address_rel = 0x00
        self.cycles = 8



    def iqr(self):
        # Async
        if self.get_flag(Flags.I) == 0:
            self.interrupt(address=0xFFFE, cycles=7)

    def nmi(self):
        # Async
        self.interrupt(address=0xFFFA, cycles=8)

    def interrupt(self, address, cycles):
        self.write(0x0100 + self.stack_pointer, (self.program_counter >> 8) & 0x00FF)
        self.stack_pointer -= 1
        self.write(0x0100 + self.stack_pointer, self.program_counter & 0x00FF)
        self.stack_pointer -= 1

        self.update_flag(Flags.B, 0)
        self.update_flag(Flags.U, 1)
        self.update_flag(Flags.I, 1)
        self.write(0x0100 + self.stack_pointer, self.status)
        self.stack_pointer -= 1

        self.address_abs = address
        lo = self.read(self.address_abs + 0)
        hi = self.read(self.address_abs + 1)
        self.program_counter = (hi << 8) | lo

        self.cycles = cycles

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

    def addr_accumulator(self):
        print("addr_accumulator")
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
            self.data_fetched = self.read(self.address_abs)
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
        return 0

    def op_cld(self):
        self.update_flag(Flags.D, 0)
        return 0

    def op_cli(self):
        self.update_flag(Flags.I, 0)
        return 0

    def op_clv(self):
        self.update_flag(Flags.V, 0)
        return 0

    def op_adc(self):
        data = self.fetch()
        temp = self.reg_accumulator + data + self.get_flag(Flags.C)
        self.update_flag(Flags.C, temp > 255)
        self.update_flag(Flags.Z, (temp & 0x00FF) == 0)
        self.update_flag(Flags.N, temp & 0x80)
        self.update_flag(Flags.V, (not (self.reg_accumulator ^ data) & (self.reg_accumulator ^ temp)) & 0x0080)
        self.reg_accumulator = temp & 0x00FF
        return 1

    def op_sbc(self):
        # a = a - m - (1-c) --> a = a + -m + 1 + c
        data = self.fetch()
        # 2's compliments
        value = data ^ 0x00FF
        temp = self.reg_accumulator + value + self.get_flag(Flags.C)
        self.update_flag(Flags.C, temp & 0XFF00)
        self.update_flag(Flags.Z, (temp & 0x00FF) == 0)
        self.update_flag(Flags.N, temp & 0x80)
        self.update_flag(Flags.V, (not(self.reg_accumulator ^ data) & (self.reg_accumulator ^ temp)) & 0x0080)
        self.reg_accumulator = temp & 0x00FF
        return 1

    def op_pha(self):
        self.write(0x1000 + self.stack_pointer, self.reg_accumulator)
        self.stack_pointer -= 1
        return 0

    def op_pla(self):
        self.stack_pointer += 1
        self.read(0x1000 + self.stack_pointer, self.reg_accumulator)
        self.update_flag(Flags.Z, self.reg_accumulator == 0)
        self.update_flag(Flags.N, self.reg_accumulator & 0x80)
        return 0

    def op_php(self):
        self.update_flag(Flags.B, 1)
        self.update_flag(Flags.U, 1)
        self.write(0x1000 + self.stack_pointer, self.reg_status)
        self.stack_pointer -= 1
        self.update_flag(Flags.B, 0)
        self.update_flag(Flags.U, 0)
        return 0

    def op_plp(self):
        self.stack_pointer += 1
        self.read(0x1000 + self.stack_pointer, self.reg_status)
        self.update_flag(Flags.U, 1)   # ? don't see in doc
        return 0

    def op_rti(self):
        self.stack_pointer += 1
        self.reg_status = self.read(0x0100 + self.stack_pointer)
        self.update_flag(Flags.B, 0)
        self.update_flag(Flags.U, 0)
        self.stack_pointer += 1
        lo = self.read(0x0100 + self.stack_pointer)
        self.stack_pointer += 1
        hi = self.read(0x0100 + self.stack_pointer)
        self.program_counter = (hi << 8) | lo
        return 0

    def op_asl(self):
        value = self.fetch() << 1
        if value & 0xFF00 > 1:
            self.update_flag(Flags.C, 1)
        if value & 0x00FF == 0:
            self.update_flag(Flags.Z, 1)
        if value & 0x80:
            self.update_flag(Flags.N, 1)
        if self.opcode["addr_mode"] == AddrMode.ADDR_ACCUMULATOR:
            self.reg_accumulator = value & 0x00FF
        else:
            self.write(self.address_abs, value & 0x00FF)
        return 0

    def op_brk(self):
        self.update_flag(Flags.I, 1)
        self.update_flag(Flags.U, 1)
        self.update_flag(Flags.B, 1)
        self.program_counter += 1
        self.write(0x0100 + self.stack_pointer, (self.program_counter >> 8) & 0x00FF)
        self.stack_pointer -= 1
        self.write(0x0100 + self.stack_pointer, self.program_counter & 0x00FF)
        self.stack_pointer -= 1
        self.write(0x0100 + self.stack_pointer, self.status)
        self.stack_pointer -= 1

        lo = self.read(0xFFFE + 0)
        hi = self.read(0xFFFE + 1)
        self.program_counter = (hi << 8) | lo
        return 0

    def op_tya(self):
        self.reg_accumulator = self.reg_y_index
        if self.reg_accumulator & 0x00FF == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_accumulator & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_txs(self):
        self.write(0x1000 + self.stack_pointer, self.reg_x_index)
        self.stack_pointer -= 1
        return 0

    def op_txa(self):
        self.reg_accumulator = self.reg_x_index
        if self.reg_accumulator & 0x00FF == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_accumulator & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_tsx(self):
        self.stack_pointer += 1
        self.reg_x_index = self.read(0x0100 + self.stack_pointer)
        if self.reg_accumulator & 0x00FF == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_accumulator & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_tay(self):
        self.reg_y_index = self.reg_accumulator
        if self.reg_y_index & 0x00FF == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_y_index & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_tax(self):
        self.reg_x_index = self.reg_accumulator
        if self.reg_x_index & 0x00FF == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_x_index & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_sty(self):
        self.write(self.address_abs, self.reg_y_index)
        return 0

    def op_stx(self):
        self.write(self.address_abs, self.reg_x_index)
        return 0

    def op_sta(self):
        self.write(self.address_abs, self.reg_accumulator)
        return 0

    def op_sei(self):
        self.update_flag(Flags.I, 1)
        return 0

    def op_sed(self):
        self.update_flag(Flags.D, 1)
        return 0

    def op_sec(self):
        self.update_flag(Flags.C, 1)
        return 0

    def op_cmp(self):
        value = self.fetch()
        if self.reg_accumulator >= value:
            self.update_flag(Flags.C, 1)
        if self.reg_accumulator == value:
            self.update_flag(Flags.Z, 1)
        diff = self.reg_accumulator - value
        if diff & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_cpx(self):
        value = self.fetch()
        if self.reg_x_index >= value:
            self.update_flag(Flags.C, 1)
        if self.reg_x_index == value:
            self.update_flag(Flags.Z, 1)
        diff = self.reg_x_index - value
        if diff & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_cpy(self):
        value = self.fetch()
        if self.reg_y_index >= value:
            self.update_flag(Flags.C, 1)
        if self.reg_y_index == value:
            self.update_flag(Flags.Z, 1)
        diff = self.reg_y_index - value
        if diff & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_dec(self):
        value = self.fetch() - 1
        self.write(self.address_abs, value)
        if value == 0:
            self.update_flag(Flags.Z, 1)
        if value & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_dex(self):
        self.reg_x_index -= 1
        if self.reg_x_index == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_x_index & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_dey(self):
        self.reg_y_index -= 1
        if self.reg_y_index == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_y_index & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_inc(self):
        value = self.fetch() + 1
        self.write(self.address_abs, value)
        if self.reg_y_index == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_y_index & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_inx(self):
        self.reg_x_index += 1
        if self.reg_x_index == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_x_index & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_iny(self):
        self.reg_y_index += 1
        if self.reg_y_index == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_y_index & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_nop(self):
        return 0

    def op_ora(self):
        value = self.fetch()
        self.reg_accumulator = value | self.reg_accumulator
        if self.reg_accumulator == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_accumulator & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_eor(self):
        value = self.fetch()
        self.reg_accumulator = value ^ self.reg_accumulator
        if self.reg_accumulator == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_accumulator & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_lda(self):
        self.reg_accumulator = self.fetch()
        if self.reg_accumulator == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_accumulator & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_ldx(self):
        self.reg_x_index = self.fetch()
        if self.reg_x_index == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_x_index & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_ldy(self):
        self.reg_y_index = self.fetch()
        if self.reg_y_index == 0:
            self.update_flag(Flags.Z, 1)
        if self.reg_y_index & 0x80:
            self.update_flag(Flags.N, 1)
        return 0

    def op_lsr(self):
        value = self.fetch() >> 1
        if value == 0:
            self.update_flag(Flags.Z, 1)
        if value & 0x80:
            self.update_flag(Flags.N, 1)
        if self.opcode["address_mode"] == AddrMode.ADDR_ACCUMULATOR:
            self.reg_accumulator = value
        else:
            self.write(self.address_abs, value & 0xFF)
        return 0

    def op_ror(self):
        value = self.fetch()
        self.update_flag(Flags.C, value & 0x1)
        new_msb = (value & 0x1) << 7
        value = (value >> 1) + new_msb
        if value == 0:
            self.update_flag(Flags.Z, 1)
        if value & 0x80:
            self.update_flag(Flags.N, 1)
        if self.opcode["address_mode"] == AddrMode.ADDR_ACCUMULATOR:
            self.reg_accumulator = value
        else:
            self.write(self.address_abs, value & 0xFF)
        return 0

    def op_rol(self):
        value = self.fetch()
        self.update_flag(Flags.C, value & 0x80)
        new_lsb = (value & 0x80) >> 7
        value = (value << 1) + new_lsb
        if value == 0:
            self.update_flag(Flags.Z, 1)
        if value & 0x80:
            self.update_flag(Flags.N, 1)
        if self.opcode["address_mode"] == AddrMode.ADDR_ACCUMULATOR:
            self.reg_accumulator = value
        else:
            self.write(self.address_abs, value & 0xFF)
        return 0

    def op_rts(self):
        self.stack_pointer += 1
        lo = self.read(0x0100 + self.stack_pointer)
        self.stack_pointer += 1
        hi = self.read(0x0100 + self.stack_pointer)
        self.program_counter = (hi << 8) | lo
        self.program_counter += 1
        return 0

    def op_jsr(self):
        self.program_counter -= 1
        self.write(0x0100 + self.stack_pointer, (self.program_counter >> 8) & 0x00FF)
        self.stack_pointer -= 1
        self.write(0x0100 + self.stack_pointer, self.program_counter & 0x00FF)
        self.stack_pointer -= 1
        self.program_counter = self.address_abs
        return 0

    def op_jmp(self):
        self.program_counter = self.address_abs
        return 0

    def op_bit(self):
        data = self.fetch()
        temp = self.reg_accumulator & data
        self.update_flag(Flags.Z, (temp & 0x00FF) == 0x00);
        self.update_flag(Flags.N, data & (1 << 7));
        self.update_flag(Flags.V, data & (1 << 6));




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
        return self.bus.read(address=address, read_only=False)

    def write(self, address, data):
        self.bus.write(address=address, data=data)




