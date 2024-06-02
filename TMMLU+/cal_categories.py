import os

import pandas as pd

# read ./subject.tsv with columns subject	name	category

grouped_categories = {
    "STEM": [
        "physics",
        "chemistry",
        "biology",
        "computer science",
        "math",
        "engineering",
    ],
    "humanities": ["history", "philosophy", "law"],
    "social sciences": [
        "politics",
        "culture",
        "economics",
        "geography",
        "psychology",
        "education",
    ],
    "other (business, health, misc.)": ["other", "business", "health"],
}

category2name = pd.read_csv('./subject.tsv', sep='\t', header=None)
category2name.columns = ['subject', 'name', 'category']
category2name = category2name.drop('name', axis=1)


results = pd.DataFrame(columns=['model', 'STEM',  'social sciences', 'humanities', 'other (business, health, misc.)', 'average'])

for file in os.listdir('./'):
    if file.endswith('.tsv') and file.startswith('tmmluplus_'):
        print("=" * 80)
        df = pd.read_csv(file, sep='\t', header=None)
        model_name = df[0][0]
        print(f"Model: {model_name}")
        df.columns = ['model', 'subject', 'performance']
        df = df.merge(category2name, on='subject')

        df['group'] = None
        for category, subjects in grouped_categories.items():
            df.loc[df['category'].isin(subjects), 'group'] = category
        assert df['group'].notnull().all()

        # calculate average performance per group
        grouped = df.groupby('group')['performance'].mean().round(2)

        # add average of each group to the dataframe
        grouped['average'] = grouped.mean().round(2)

        # pretty print the results without
        print(grouped.to_string())

        grouped['model'] = model_name
        grouped_df = grouped.to_frame().T
        results = pd.concat([results, grouped_df], ignore_index=True)
print("=" * 80)
markdown_table = results.to_markdown(index=False)

with open('benchmark.md', 'w') as f:
    f.write(markdown_table)
