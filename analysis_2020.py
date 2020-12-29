import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import AutoMinorLocator
_ = sns.set_style('white')
pal = sns.color_palette()


df = pd.read_csv('books.csv')
df = df[df['date'].apply(lambda x: str(x)[-2:] == '20')]
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
_ = fig.savefig('demo2020.png', dpi=350)

graph = sns.catplot(x='race', hue='gender', col='genre', kind='count', data=demo)
for a in graph.axes[0]:
    for p in a.patches:
        height = p.get_height()
        if ~np.isnan(height):
            a.text(p.get_x() + p.get_width() / 2., height + 0.1, int(height), ha="center")
_ = plt.savefig('demo_facet2020.png', dpi=350)

fig = plt.figure()
graph = sns.histplot(data=df, x='year', discrete=True)
a = graph.axes
for p in a.patches:
    height = p.get_height()
    if height > 0.5:
        a.text(p.get_x() + p.get_width() / 2., height + 0.1, int(height), ha="center", size='xx-small')
# a.xaxis.set_minor_locator(AutoMinorLocator())
_ = plt.savefig('years_2020.png', dpi=350, bbox_inches='tight')

df = pd.read_csv('books.csv')
au = [(row['last'], row['first'], row['date']) for i, row in df.iterrows()]
au = [a for a in au if type(a[2]) == str]
before = [b[:2] for b in au if b[2][-2:] != '20']
new_aus = [a[:2] for a in au if a[2][-2:] == '20']
print("%d unique authors" %len(set(new_aus)))
new_aus = [a[:2] for a in au if a[:2] not in before]
print("%d unique new authors" %len(set(new_aus)))
