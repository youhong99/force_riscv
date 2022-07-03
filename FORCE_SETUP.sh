# !/bin/bash
#
        #Install required packages
        sudo apt-get update
        sudo apt-get install python3.8
        sudo apt-get install python3-dev
        sudo apt-get install g++
        sudo apt install git

echo Successful package installation -------------------------------
sleep 2

        #Setup force-riscv
        cd
        FORCE_RISCV_CHECK="./force-riscv/"
        if [ ! -d "$FORCE_RISCV_CHECK" ]; then
                git clone https://github.com/openhwgroup/force-riscv.git force-riscv
        fi

echo Successful force-riscv git cloning ----------------------------
sleep 2

        cd force-riscv/
        echo Current Directory is /force-riscv/
        export FORCE_CC=/usr/bin/g++
        export FORCE_PYTHON_VER=3.8
        export FORCE_PYTHON_LIB=/usr/lib/x86_64-linux-gnu/
        export FORCE_PYTHON_INC=/usr/include/python3.8

        #./setup

        source setenv.bash
        make
        make tests
        #./utils/regression/master_run.py
        #./utils/regression/unit_tests.py #Require long simulation time

echo Successful force-riscv setup ----------------------------------
sleep 2

        #Setup riscv-toolchains
        cd
        TOOLCHAIN_CHECK="./riscv-toolchains-rvv-1.0.0/"
        if [ ! -d "$TOOLCHAIN_CHECK" ]; then
                git clone https://github.com/Imperas/riscv-toolchains.git --branch rvv-1.0.0
                mv riscv-toolchains riscv-toolchains-rvv-1.0.0
        fi

        export TOPDIR=$(pwd)
        export RISCV_TUPLE=riscv64-unknown-elf
        export RISCV_PREFIX=${RISCV_TUPLE}-
        export RISCV_TOOLCHAIN=${TOPDIR}/riscv-toolchains-rvv-1.0.0/Linux64
        export PATH=${PATH}:${RISCV_TOOLCHAIN}/bin

echo Successful riscv-toolchain setup ------------------------------
sleep 2

        #Setup riscvOVPsim
        cd
        OVPSIM_CHECK="./imperas-riscv-tests/"
        if [ ! -d "$OVPSIM_CHECK" ]; then
                git clone https://github.com/riscv-ovpsim/imperas-riscv-tests
        fi

        cd imperas-riscv-tests
        make help
        make clean simulate verify postverify XLEN=32 RISCV_DEVICE=I

echo Successful riscvOVPsim setup ----------------------------------
sleep 2

        cd
