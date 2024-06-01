import sys

class Bit:

    def __init__(self):
        self.rom = []
        self.ram = []
        self.stack = []
        self.d = 0000
        self.c = 0000
        self.b = 0000
        self.a = 0000
        
    def Conver_to_int(self, bits):
        for bit in bits:
            if bit not in ['0', '1']:
                raise ValueError("0010")
            if len(bits) > 4:
                raise ValueError("0011")
        return int(bits, 2)
        
    def run(self):
        try:
            with open("Run.aron4") as file:
                if len(file) > 63:
                    raise ValueError("0000")
                else:
                    self.rom = file
        except Exception:
            raise ValueError("0100")
                
    def execute(self):
        
        if self.d >= 63:
            if self.d >= len(self.rom):
                self.ram[self.Conver_to_int(self.d)] = self.rom[self.Conver_to_int(self.d)]
                self.d += 1
                return
        elif self.d <= 243:
            instruction = self.ram[self.Conver_to_int(self.d)]
            
        command = instruction[0] + instruction[1]
        ops = []
        for i in range(len(instruction) - 2):
            ops.append(instruction[i + 2])
        if command == "sb":
            self.c = self.a - self.c
            return
        elif command == "ad":
            self.c = self.a + self.c
            return
        elif command == "ld":
            self.a = self.ram[self.Conver_to_int(self.a) + self.Conver_to_int(self.b)]
            return
        elif command == "st":
            self.ram[self.Conver_to_int(self.a) + self.Conver_to_int(self.b)] = self.c
            return
        elif command == "jp":
            pass
        
            