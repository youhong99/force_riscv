from riscv.EnvRISCV import EnvRISCV
from riscv.GenThreadRISCV import GenThreadRISCV
from base.Sequence import Sequence
from DV.riscv.trees.instruction_tree import ALU_Int32_instructions
from DV.riscv.trees.instruction_tree import LDST_Int32_instructions

class MyMainSequence(Sequence):
    def generate(self, **kwargs):
        i100_seq = I100Sequence(self.genThread)
        i100_seq.run()
        f100_seq = F100Sequence(self.genThread)
        f100_seq.run()

class I100Sequence(Sequence):
    def generate(self, **kargs):
        for _ in range (100):
            instr = self.pickWeighted(ALU_Int32_instructions)
            self.genInstruction(instr)
            self.notice(">>>>> The instruction: {}".format(instr))

class F100Sequence(Sequence):
    def generate(self, **kargs):
        for _ in range (100):
            instr = self.pickWeighted(LDST_Int32_instructions)
            self.genInstruction(instr)
            self.notice(">>>>> The instruction: {}".format(instr))

#The Main Sequence Class should be directed to the sequence to be executed
MainSequenceClass   = MyMainSequence
GenThreadClass      = GenThreadRISCV
EnvClass            = EnvRISCV
