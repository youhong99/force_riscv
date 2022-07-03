from riscv.EnvRISCV import EnvRISCV
from riscv.GenThreadRISCV import GenThreadRISCV
from base.Sequence import Sequence
from base.SequenceLibrary import SequenceLibrary

class MainSequence(Sequence):
    def generate(self, **kargs):
        seq_library = MySequenceLibrary(self.genThread)

        for _ in range(4):
            current_sequence = seq_library.chooseOne()
            current_sequence.run()

        for current_sequence in seq_library.getPermutated():
            current_sequence.run()
			
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

