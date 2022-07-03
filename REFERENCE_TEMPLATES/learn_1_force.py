from riscv.EnvRISCV import EnvRISCV
from riscv.GenThreadRISCV import GenThreadRISCV
from base.Sequence import Sequence

class MainSequence(Sequence):
    def generate(self, **kargs):
        self.genInstruction("ADD##RISCV",   {"rd":5, "rs1":5, "rs2":6})
        self.genInstruction("SW##RISCV" ,   {"LSTarget": 0x11000000}) 
        self.genInstruction("SW##RISCV" ,   {"NoPreamble": 1})
        """
        Load/Store uses a register as pointer
        Load upper integer (LUI) first loads
        Add immediate (ADDIW) then adds a random pointer value
        The pointer is then summed with a offset to obtain the specified target

        If NoPreamble attribute is set, no preamble instructions will be generated

        The Load/Store target needs to be aligned (divisible by 4)
        Otherwise an exception occurs

        The store is Little Endian
        """

        self.genInstruction("SUB##RISCV")
        self.genInstruction("ADD##RISCV")
        self.genInstruction("SUB##RISCV")
        self.genInstruction("LW##RISCV" ,   {"LSTarget": 0x11000000})
        self.genInstruction("BEQ##RISCV",   {"CondTaken": "0"})
        self.genInstruction("BGE##RISCV",   {"BRTarget": 0x80011040, "SpeculativeBnt": True})

        """
        The branch parameter "CondTaken" if set to 1
        sometimes result in a unresolved constraint

        Speculative BNT performs processing of branched/unbranched instruction
        """


""" 
Output Files
sim.log                     : simulation results for each instruction generated
<test_template>.Default.S   : full program including setup codes
                              main program starts from address 0x80011000
                              <Code_Address>:<Code_Opcode> <Instruction>
"""

MainSequenceClass   = MainSequence
GenThreadClass      = GenThreadRISCV
EnvClass            = EnvRISCV
