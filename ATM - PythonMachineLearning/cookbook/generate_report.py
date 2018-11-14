import sqlite3
import json
import pandas as pd


experiments = ['./atm.db']  ###  path to atm's generated db
df = pd.DataFrame(columns=['experiment', 'method', 'id', 'accuracy', 'SD', 'cohen_kappa', 'f1', 'mcc', 'roc_auc', 'ap'])


def find_best(my_db):
    df_sub = pd.DataFrame(columns=['experiment', 'method', 'id', 'accuracy', 'SD', 'cohen_kappa', 'f1', 'mcc', 'roc_auc', 'ap'])
    conn = sqlite3.connect(my_db)
    cur = conn.cursor()

    cur.execute("SELECT classifiers.id, classifiers.metrics_location, classifiers.cv_judgment_metric, classifiers.cv_judgment_metric_stdev, "
                "hyperpartitions.method, max(classifiers.cv_judgment_metric)as best_seen FROM hyperpartitions "
                "LEFT JOIN classifiers on classifiers.hyperpartition_id = hyperpartitions.id "
                "GROUP BY hyperpartitions.method")

    rows = cur.fetchall()

    for i in range(len(rows)):
        if None not in rows[i]:
            metrics = rows[i][1]
            with open('./'+metrics) as f:  ###  path to atm's generated db
                for line in f:
                    data=json.loads(line)
            subs = data['test']

            df_sub.loc[i] = [my_db, rows[i][4], rows[i][0], subs['accuracy'], rows[i][3],
                         subs['cohen_kappa'], subs['f1'], subs['mcc'], subs['roc_auc'], subs['ap']]

    return df_sub

for eval in experiments:
    df = df.append(find_best(eval))

df = df.sort_values('experiment')
df.to_csv('ResultSummary.csv', index=False)