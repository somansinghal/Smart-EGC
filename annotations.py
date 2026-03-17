import wfdb

ann = wfdb.rdann('100', 'atr', pn_dir='mitdb')

print("Annotation symbols:", ann.symbol[:20])