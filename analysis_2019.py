import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

_ = sns.set_style('white')
pal = sns.color_palette()


df = pd.read_csv('books.csv')
df = df[df['date'].apply(lambda x: str(x)[-2:] == '19')]
demo = df[['race2', 'sex', 'Genre']]
demo = demo.rename(columns={'sex': 'gender', 'race2': 'race', 'Genre': 'genre'})

fig, axs = plt.subplots(1, 3, figsize=(12, 3), gridspec_kw={'width_ratios': [1, 1, 2]})
for ax, x in zip(axs, ['gender', 'genre', 'race']):
    a = sns.countplot(x=x, data=demo, ax=ax)
    for p in a.patches:
        height = p.get_height()
        if ~np.isnan(height):
            a.text(p.get_x() + p.get_width() / 2., height + 0.1, int(height), ha="center")
_ = fig.tight_layout()
_ = fig.savefig('demo.png', dpi=350)

graph = sns.catplot(x='race', hue='gender', col='genre', kind='count', data=demo)
for a in graph.axes[0]:
    for p in a.patches:
        height = p.get_height()
        if ~np.isnan(height):
            a.text(p.get_x() + p.get_width() / 2., height + 0.1, int(height), ha="center")
_ = plt.savefig('demo_facet.png', dpi=350)