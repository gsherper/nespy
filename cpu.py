from enum import Enum

class FLAGS(Enum):
    C = (1 << 0),  # Carry
    Z = (1 << 1),  # Zero
    I = (1 << 2),  # Disable Interrupts
    D = (1 << 3),  # Decimal Mode
    B = (1 << 4),  # Break
    U = (1 << 5),  # Unused
    V = (1 << 6),  # Overflow
    N = (1 << 7)   # Negative

class CPU:

    def __init__(self):
        self.reg_accumulator = None
        self.reg_x_index = None
        self.reg_y_index = None
        self.reg_status = None
        self.program_counter = None
        self.stack_pointer = None



        #SR Flgas Register (bit 7 to bit 0)
        self.flag_negative = None
        self.flag_overflow = None
        self.flag_break = None
        self.flag_decimal = None
        self.flag_interrupt = None
        self.flag_zero = None
        self.flag_carry = None

        self.non_maskable_interrupt = None
        self.iqr = None

    def read(self, address):
        return self.bus.read(address=address, read_only=False)

    def write(self, address, data):
        self.bus.write(address=address, data=data)



