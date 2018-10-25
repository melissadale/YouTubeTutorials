import sqlite3
import pprint
import ast

conn = sqlite3.connect('../../atm.db')
cur = conn.cursor()

# Tables in atm.db:
# classifiers, dataruns, datasets, hyperpartitions
# cur.execute("SELECT * FROM classifiers")
# rows = cur.fetchall()
# for row in rows:
#     print(row)


# show top 5 classifiers
best = cur.execute("SELECT id, metrics_location, cv_judgment_metric FROM classifiers "
                   "ORDER BY cv_judgment_metric DESC "
                   "LIMIT 5")
top = []
for b in best:
    # print(b)
    top.append(b[1])

###################
my_location = '../../' + top[0]

with open(my_location) as f:
    best_of_best = f.readlines()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(ast.literal_eval(best_of_best[0]))