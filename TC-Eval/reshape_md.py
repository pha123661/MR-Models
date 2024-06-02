import pandas as pd

# Read markdown table into a pandas DataFrame
df = pd.read_table('benchmark.md', sep='|')
df.columns = df.columns.str.strip()
df = df.drop(columns=[''])

# append column "metric" after "task_name" with an underscore
df['task_name'] = df['task_name'].str.strip()
df['metric'] = df['metric'].str.strip()
df['task_name'] = df[['task_name', 'metric']].apply(lambda x: x.iloc[0] + '_' + x.iloc[1], axis=1)
df = df.drop('metric', axis=1)
df = df.dropna(axis=1, how='all')
df = df.iloc[1:]

df = df.set_index('task_name')
df = df.T
df = df.reset_index()
df = df.rename(columns={'index': 'model'})
df.columns.name = None

# try to convert columns to float
for col in df.columns:
    if col == 'model':
        continue
    df[col] = df[col].astype(float).apply(lambda x: f'{100*x:.2f}%')


with open('benchmark_T.md', 'w') as f:
    f.write(df.to_markdown(index=False))