import os
import pandas as pd

mypath = os.path.normcase(r"C:\Users\Aharon T\Desktop\sample files")

# get list of files
files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        if len(row) == 0:
            continue
# build list of dataframes, adding "challenge" column
dfs = [pd.read_csv(os.path.join(mypath, f)).assign(challenge=f) for f in files]

# concatenate dataframes into one
df = pd.concat(dfs, ignore_index=True)

# write to csv
df.to_csv('all_entrants.csv')