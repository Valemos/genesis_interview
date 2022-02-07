import pandas as pd

df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})

group_labels = df['grps'].unique()
groups = [df[df['grps'] == label] for label in group_labels]


for group in groups:
    sorted_group = group.sort_values(by="vals", ascending=False)

    print(sorted_group)
    target_values = sorted_group["vals"].values[:3]
    result = target_values.sum()
    label = sorted_group['grps'].values[0]
    print(f"label: {label} result: {result}")
