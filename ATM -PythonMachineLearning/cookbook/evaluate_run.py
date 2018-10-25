import atm.database as db
from utilities import *


eval = db.Database('sqlite', '../../atm.db')

################## database and datarun
# print_hp_summary(eval, 1)
# print_summary(eval, 1)
print_method_summary(eval, 1)