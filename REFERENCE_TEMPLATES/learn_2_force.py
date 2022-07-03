from riscv.EnvRISCV import EnvRISCV
from riscv.GenThreadRISCV import GenThreadRISCV
from base.Sequence import Sequence

"""
The following codes are imported to provide dictionary for list of instructions
"""

from base.InstructionMap import InstructionMap
from DV.riscv.trees.instruction_tree import *


class MainSequence(Sequence):
    def generate(self, **kargs):
        (count_opt, count_opt_valid) = self.getOption("instruction_count")
        if count_opt_valid:
            instruction_count = count_opt
        else:
            instruction_count = 20

        """
        The methodology used obtains value set for the instruction count to be generated
        If the parameter has not been set, a default value of "20" is set
        """

        instruction_group = (
            ALU_Int32_instructions
            if self.getGlobalState("AppRegisterWidth") == 32
            else ALU_Int64_instructions
        )

        """
        The set introduced lists the query information that consists of numeric values
        These numeric values can be converted to hexadecimal for easier understanding
        """

        record_attribute_numeric_set = {"Opcode","PA","VA","LSTarget","BRTarget"}
        record_dictionary_set = {"Dests","Srcs","Imms","Status","Addressing"}

        with open ("query.txt",'w') as record:
            for _ in range(instruction_count):
                instruction_selected = self.pickWeighted(instruction_group)
                record_id = self.genInstruction(instruction_selected)
                record_dict = self.queryInstructionRecord(record_id)

                """
                Instructions are then picked from the list provided and generated
                The total amount of instructions generated is based on the pre-set parameter value
                The instruction record ID is then used to query information into a dictionary
                """

                """
                The following segment of code performs formatting on the dictionary items
                The formatted information are outputted onto a text file
                """

                record.write(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                for key, value in record_dict.items():
                    for attribute in record_attribute_numeric_set:
                        if key == attribute:
                            value = hex(value)
                    for attribute in record_dictionary_set:
                        if key == attribute:
                            value = ""
                            for pointer in record_dict[key]:
                                value += ("%s:%s " % (pointer,record_dict[key][pointer]))
                    if value != "":
                        record.write("%10s\t\t\t : %s\n" % (key,value))
            

MainSequenceClass   = MainSequence
GenThreadClass      = GenThreadRISCV
EnvClass            = EnvRISCV
