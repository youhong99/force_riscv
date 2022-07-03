from riscv.EnvRISCV import EnvRISCV
from riscv.GenThreadRISCV import GenThreadRISCV
from base.Sequence import Sequence
from DV.riscv.trees.instruction_tree import LDST_All_instructions
from DV.riscv.trees.instruction_tree import LDST_Byte_instructions
from DV.riscv.trees.instruction_tree import LDST_Half_instructions
from DV.riscv.trees.instruction_tree import LDST_Word_instructions
from DV.riscv.trees.instruction_tree import LDST_Double_instructions
"""
The segment of imports acquire instruction group information
"""

class MyMainSequence(Sequence):
    def generate(self, **kwargs):
        for _ in range (100):
            instr = self.pickWeighted(LDST_All_instructions)

            page_addr = self.genVA(Size=0x2000, Align=0x1000)

            if instr in LDST_Byte_instructions:
                min_addr = 0xFFC
            elif instr in LDST_Half_instructions:
                min_addr = 0xFFC
            elif instr in LDST_Word_instructions:
                min_addr = 0xFFA
            elif instr in LDST_Double_instructions:
                min_addr = 0xFF6

            target_addr = page_addr + self.random32(min_addr, 0xFFF)
            self.genInstruction(instr, {"LSTarget":target_addr})

#The Main Sequence Class should be directed to the sequence to be executed
MainSequenceClass   = MyMainSequence
GenThreadClass      = GenThreadRISCV
EnvClass            = EnvRISCV
