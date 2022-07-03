#!/bin/bash
#Read test template from command line argument
force-riscv/bin/friscv -t $1 | tee friscv.log

ELF_FILE=$(basename $1 | sed 's/.py//').Default.ELF

RISCV_OVPSIM=imperas-riscv-tests/riscv-ovpsim/bin/Linux64/riscvOVPsim.exe 

${RISCV_OVPSIM} \
--program ${ELF_FILE} \
--controlfile ./force-riscv/target/riscvOVPsim_rv64gc/riscvOVPsim.ic \
--addressbits 64 \
--finishonopcode 0x0000006f \
--override riscvOVPsim/cpu/simulateexceptions=T \
--override riscvOVPsim/cpu/defaultsemihost=F \
--cover basic --showuncovered --extensions RVI,RVM,RVIC \
--reportfile riscvOVPsim.coverage.txt \
| tee riscvOVPsim.basic.log
