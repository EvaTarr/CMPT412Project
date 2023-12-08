import os
import json
import pandas as pd

from words import get_entitites, entity_frequencies
from preprocessing import write_to_file, process_by_chunk, filter_column_by_value, stratify, sample, entities


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

# declare paths and file
folder = os.listdir(os.path.join(directory, topic, 'processed')) if processed else os.listdir(os.path.join(directory, topic))
files = [file for file in folder if file.endswith(dataset+'.csv')]
filename = None if len(files) != 1 else files[0]
assert filename is not None, '0 or more than 1 files were found.'
raw_path = os.path.join(directory, topic, filename)
processed_path = os.path.join(directory, topic, 'processed', filename)
filepath = raw_path if not processed else processed_path

if not processed:
    # open and filter by subreddit
    df = process_by_chunk(filepath, func=filter_column_by_value, chunksize=chunksize, column='subreddit.name', value=subreddit)
    print(df[['sentiment', 'score']].corr())

    # save entity sentiment df to csv
    output_suffix = f'_{subreddit}' + '.csv'
    write_to_file(df.to_csv(index=False), processed_path.replace('.csv', output_suffix))

    # stratify the dataframe by score column with intervals. Ex, [-inf, 0, 10, +inf]
    df = stratify(df, 'score', [-float('inf'), -30, 400, float('inf')], ['low', 'moderate', 'high'])

    # sample each strata
    high_df = sample(df[df['stratum'] == 'high'], 'stratum', group=True, frac_samples=0.10, random_state=18)
    low_df = sample(df[df['stratum'] == 'low'], 'stratum', group=True, frac_samples=0.10, random_state=18)

    # perform entity sentiment processing using Google Cloud
    high_df = entities(high_df, 'body', sentiment=False)
    low_df = entities(low_df, 'body', sentiment=False)

    # join entity json responses from high and low entity analysis to original df
    df = df.join(pd.concat([high_df, low_df])['entities'])

    # save entity sentiment df to csv for later use
    output_suffix = f'_{subreddit}_entities' + '.csv'
    write_to_file(df.to_csv(index=False), processed_path.replace('.csv', output_suffix))

else:
    # read csv
    df = pd.read_csv(filepath)

    # stratify the existing dataset by score column with intervals. Ex, [-inf, 0, 10, +inf]
    df = stratify(df, 'score', [-float('inf'), -10, 10, float('inf')], ['low', 'moderate', 'high'])
    output_suffix = f'_{subreddit}' + '.csv'
    write_to_file(df.to_csv(index=False), processed_path.replace('.csv', output_suffix))


# perform analysis
# ======================================================================================================================

# extract high, moderate, and low stratum from data
high_df = df[df['stratum'] == 'high']
low_df = df[df['stratum'] == 'low']
moderate_df = df[df['stratum'] == 'moderate']


# high-moderate frequency comparision
# ----------------------------------------------------------------------------------------------------------------------
entities = get_entitites(high_df, 'entity_sentiment')
high_freq_df = entity_frequencies(high_df, entities, 'body')
moderate_freq_df = entity_frequencies(moderate_df, entities, 'body')

freq_df = high_freq_df.merge(moderate_freq_df, left_index=True, right_index=True, suffixes=('_high', '_moderate'))
freq_df['normalized_difference'] = (freq_df['normalized_high']-freq_df['normalized_moderate'])*100

output_suffix = '_high-moderate-freq' + '.csv'
write_to_file(freq_df.to_csv(), processed_path.replace('.csv', output_suffix))


# high-low frequency comparision
# ----------------------------------------------------------------------------------------------------------------------
low_freq_df = entity_frequencies(low_df, entities, 'body')

freq_df = high_freq_df.merge(low_freq_df, left_index=True, right_index=True, suffixes=('_high', '_low'))
freq_df['normalized_difference'] = (freq_df['normalized_high'] - freq_df['normalized_low']) * 100

output_suffix = '_high-low-freq' + '.csv'
write_to_file(freq_df.to_csv(), processed_path.replace('.csv', output_suffix))


# low-moderate frequency comparision
# ----------------------------------------------------------------------------------------------------------------------
entities = get_entitites(low_df, 'entities')
low_freq_df = entity_frequencies(low_df, entities, 'body')
moderate_freq_df = entity_frequencies(moderate_df, entities, 'body')

freq_df = low_freq_df.merge(moderate_freq_df, left_index=True, right_index=True, suffixes=('_low', '_moderate'))
freq_df['normalized_difference'] = (freq_df['normalized_low'] - freq_df['normalized_moderate']) * 100

output_suffix = '_low-moderate-freq' + '.csv'
write_to_file(freq_df.to_csv(), processed_path.replace('.csv', output_suffix))


# low-high frequency comparision
# ----------------------------------------------------------------------------------------------------------------------
high_freq_df = entity_frequencies(high_df, entities, 'body')

freq_df = low_freq_df.merge(high_freq_df, left_index=True, right_index=True, suffixes=('_low', '_high'))
freq_df['normalized_difference'] = (freq_df['normalized_low'] - freq_df['normalized_high']) * 100

output_suffix = '_low-high-freq' + '.csv'
write_to_file(freq_df.to_csv(), processed_path.replace('.csv', output_suffix))