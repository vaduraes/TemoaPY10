from temoa_rules import *
from temoa_initialize import *
from temoa_run import *
M = TemoaModel(name)

# ---------------------------------------------------------------
# Define sets. 
# Sets are collections of items used to index parameters and variables
# ---------------------------------------------------------------

# Define time periods
M.time_exist = Set(ordered=True) 
M.time_future = Set(ordered=True)
M.time_optimize = Set(ordered=True, initialize=init_set_time_optimize)
# Define time period vintages to track capacity installation
M.vintage_exist = Set(ordered=True, initialize=init_set_vintage_exist)
M.vintage_optimize = Set(ordered=True, initialize=init_set_vintage_optimize)
M.vintage_all = M.time_exist | M.time_optimize
SetUnion
M.vintage_all.subsets(expand_all_set_operators=False)

print("end")