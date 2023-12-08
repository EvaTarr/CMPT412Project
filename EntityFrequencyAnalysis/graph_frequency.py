import os
import matplotlib.pyplot as plt
import pandas as pd
import json

# import config variables
file = open("config.json")
config = json.load(file)
directory = config.get("directory")
chunksize = config.get("chunksize")
file.close()

# settings
# ----------------------------------------------------------------------------------------------------------------------
processed = True
topic = ''
dataset = ''
subreddit = ''
# ----------------------------------------------------------------------------------------------------------------------

# declare paths and search dataset based on topic, dataset, and whether the file has been processed already.
folder = os.listdir(os.path.join(directory, topic, 'processed')) if processed else os.listdir(os.path.join(directory, topic))
files = [file for file in folder if file.endswith(dataset+'.csv')]
filename = None if len(files) != 1 else files[0]
assert filename is not None, '0 or more than 1 files were found.'
raw_path = os.path.join(directory, topic, filename)
processed_path = os.path.join(directory, topic, 'processed', filename)
filepath = raw_path if not processed else processed_path

# plot frequency
# ======================================================================================================================
df = pd.read_csv(os.path.join(directory, topic, 'processed', [file for file in folder if file.endswith('entities.csv')][0]))

# Get labels and bin ranges for each
labels = list(df['stratum'].dropna().unique())
bins = {}
for label in labels:
    scores = df[df['stratum'] == label]['score']
    bins[label] = (int(scores.min()), int(scores.max()))

df = pd.read_csv(filepath).sort_values('normalized_difference', ascending=True)[0:10]

# settings to configure direct stratum comparison
top = '' # ex, High
bottom = '' # ex, Moderate

# graph data and export image to directory
# ----------------------------------------------------------------------------------------------------------------------
title = f'{topic} "{subreddit}" subreddit: Top 10 Most Frequent {top} Scoring Entities over {bottom}'

top = top.lower()
bottom = bottom.lower()

positions = list(range(len(df['tokenized'])))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 7))

# structure entity comparision as bar graph comparing each entites normalized frequency
plt.bar(positions, df[f'normalized_{top}'], width=width, label=f'{top} Score: ' + str(bins.get(top)), alpha=0.7, color='b')
plt.bar([p + width for p in positions], df[f'normalized_{bottom}'], width=width, label=f'{bottom} Score: ' + str(bins.get(bottom)), alpha=0.7, color='r')

# assign graph labels and formattting
ax.set_ylabel('Normalized Frequency (Entity Frequency/Total Comments)')
ax.set_title(title)
ax.set_xticks([p + width/2 for p in positions])
ax.set_xticklabels(df['tokenized'])
plt.xticks(rotation=45)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))
ax.legend()

# save graph as image to directory
plt.savefig(os.path.join(directory, topic, 'processed', 'plots', title+'.png'))
