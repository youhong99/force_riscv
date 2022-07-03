from riscv.EnvRISCV import EnvRISCV
from riscv.GenThreadRISCV import GenThreadRISCV
from base.Sequence import Sequence
from base.SequenceLibrary import SequenceLibrary
from riscv.Utils import LoopControl
from DV.riscv.trees.instruction_tree import *

class MainSequence(Sequence):
    def singularLoop(self, current_sequence):
        current_sequence.run()
        
    def genInstructionLoop(self, loopGpr, loopCount, current_sequence):

        # Generate Thread for Inner Loop
        inner_loop_ctrl_seq = LoopControl(self.genThread)

        # Initate the inner loop sequence, inner loop is looped for 2 times
        inner_loop_ctrl_seq.start(LoopReg=loopGpr, LoopCount=loopCount)
        current_sequence.run()
        inner_loop_ctrl_seq.end()

    def generate(self, **kargs):

        # Select and reserve specific register for looping
        (loop_gpr, inner_loop_gpr) = self.getRandomRegisters(2, "GPR", "0")
        loop_ctrl_seq = LoopControl(self.genThread)
        seq_library = MySequenceLibrary(self.genThread)
        sequenceSelected = seq_library.chooseOne()

        # Initate the outer loop sequence, outer loop is looped for 3 times
        loop_ctrl_seq.start(LoopReg=loop_gpr, LoopCount=3)
        """
            Upon initating loop sequence, a register is reserved
            LUI is used to clear the register followed by ADDI to add
            loop count offset to the register
        """
        self.genInstructionLoop(inner_loop_gpr, 2, sequenceSelected)
        #self.singularLoop(sequenceSelected)
        """
            Upon arriving at the end of a sequence,
            ADDI -1 is used to reduce the loop counter
            BNEZ is then used to provide looping
        """
        loop_ctrl_seq.end()

"""
Sequence Library
    Creates a list of sequences to select from
    The list of sequences utilized are adopted from
    DV/risc/sequences/BasicSequences
"""
class MySequenceLibrary(SequenceLibrary):
    def createSequenceList(self):
        self.seqList = [
            (
                "Bunch_of_ALU_Int",
                "DV.riscv.sequences.BasicSequences",
                "Your Description",
                20,
            ),
            (
                "Bunch_of_LDST",
                "DV.riscv.sequences.BasicSequences",
                "Your Description",
                20,
            ),
        ]

MainSequenceClass = MainSequence
GenThreadClass = GenThreadRISCV
EnvClass = EnvRISCV

