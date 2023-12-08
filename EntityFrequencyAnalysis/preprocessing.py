import os
import time

import pandas as pd
from gcloud_language import GoogleCloudNL
from tqdm import tqdm


def write_to_file(content: str, filepath: str) -> None:
    with open(filepath, 'w') as file:
        file.write(content)


def process_by_chunk(filepath: str, chunksize: int, func, **kwargs) -> pd.DataFrame:
    file_size = os.path.getsize(filepath)
    results = []
    with open(filepath, 'rb') as file:
        for chunk in pd.read_csv(file, chunksize=chunksize * 10, iterator=True):
            results.append(func(chunk, **kwargs))
            current_position = file.tell()
            progress = (current_position / file_size) * 100
            print(f"\r({process_by_chunk.__name__}) Progress: {progress:.2f}%", end='')
        print()

    return pd.concat(results)


def filter_column_by_value(chunk: pd.DataFrame, **kwargs) -> pd.DataFrame:
    return chunk[chunk[kwargs.get('column')] == kwargs.get('value')]


def stratify(df: pd.DataFrame, column: str, intervals: list, interval_labels: list) -> pd.DataFrame:
    df['stratum'] = pd.cut(df[column], bins=intervals, labels=interval_labels)
    return df


def sample(df: pd.DataFrame, column: str, group=False, n_samples=None, frac_samples=None, random_state=None) -> pd.DataFrame:
    sampled_df = pd.DataFrame()
    if group:
        grouped_df = df.groupby(column, observed=True)
        for group, subset in grouped_df:
            if n_samples is not None:
                sample = subset.sample(n_samples, random_state=random_state)
            elif frac_samples is not None:
                sample = subset.sample(frac=frac_samples, random_state=random_state)
            else:
                raise ValueError('n_samples or frac_samples must be specified.')
            sampled_df = pd.concat([sampled_df, sample])
    else:
        if n_samples is not None:
            sampled_df = df.sample(n_samples, random_state=random_state)
        elif frac_samples is not None:
            sampled_df = df.sample(frac=frac_samples, random_state=random_state)
        else:
            raise ValueError('n_samples or frac_samples must be specified.')

    return sampled_df


# Google Cloud Natural Language Processing
# ======================================================================================================================

def entities(df: pd.DataFrame, column: str, sentiment=False) -> pd.DataFrame:
    gcl = GoogleCloudNL()
    if sentiment:
        new_column = 'entity_sentiment'
        func = gcl.entity_sentiment_to_json
    else:
        new_column = 'entities'
        func = gcl.entities_to_json

    assert len(df) > 0, "the dataframe must not be empty."
    assert new_column not in df.columns, f'entities already processed'
    tqdm.pandas(desc="Progress")

    message = f'A maximum of {len(df)} api requests are to be processed. Confirm if you want to continue (y): '

    print()
    if input(message).lower() == 'y':
        df[new_column] = [{} for _ in range(len(df))]

        for i, row in tqdm(df.iterrows(), total=df.shape[0], desc="Progress"):
            df.at[i, new_column] = func(row[column])

            time.sleep(0.111)
    else:
        print('Requests canceled.')

    print()
    print(f'Report: {len(df)} request were made.')

    return df