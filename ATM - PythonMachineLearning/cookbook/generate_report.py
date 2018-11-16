import sqlite3
import json
import pandas as pd
import pickle


experiments = ['../atm.db']  ###  path to atm's generated db - can be a list of result dbs for different experiments
df = pd.DataFrame(columns=['experiment', 'method', 'id', 'accuracy', 'SD', 'cohen_kappa', 'f1', 'mcc', 'roc_auc', 'ap', 'parameters'])


def find_best(my_db):
    df_sub = pd.DataFrame(columns=['experiment', 'method', 'id', 'accuracy', 'SD', 'cohen_kappa', 'f1', 'mcc', 'roc_auc', 'ap', 'parameters'])
    conn = sqlite3.connect(my_db)
    cur = conn.cursor()

    cur.execute("SELECT classifiers.id, classifiers.metrics_location, classifiers.model_location, classifiers.cv_judgment_metric, classifiers.cv_judgment_metric_stdev, "
                "hyperpartitions.method, max(classifiers.cv_judgment_metric)as best_seen FROM hyperpartitions "
                "LEFT JOIN classifiers on classifiers.hyperpartition_id = hyperpartitions.id "
                "GROUP BY hyperpartitions.method")

    rows = cur.fetchall()

    for i in range(len(rows)):
        if None not in rows[i]:
            metrics = rows[i][1]
            models = rows[i][2]
            with open('../'+metrics) as f:  ###  path to atm's metrics
                for line in f:
                    data=json.loads(line)
            subs = data['test']

            best_model = pickle.load(open('../'+models, "rb"))
            best_params = best_model.params

            df_sub.loc[i] = [my_db, rows[i][4], rows[i][0], subs['accuracy'], rows[i][3],
                         subs['cohen_kappa'], subs['f1'], subs['mcc'], subs['roc_auc'], subs['ap'], best_params]

    return df_sub

for eval in experiments:
    df = df.append(find_best(eval))

df = df.sort_values('experiment')
df.to_csv('ResultSummary.csv', index=False)