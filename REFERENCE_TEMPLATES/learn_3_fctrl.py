"""
This template passes the listed tests to master_run utility script 
alongside the options set

./utils/regression/master_run.py -f <fctrl_file> -c <config_file>
"""

control_items = [
    {
        "fname": "learn_1_force.py",
    },
    {
        "fname": "learn_2_force.py",
        "options":{"max-instr":30000,"iterations":1}
    }
]
