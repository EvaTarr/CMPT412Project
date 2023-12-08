import json
import pandas as pd


def get_entitites(df: pd.DataFrame, column: str):
    json_data = df[column].dropna().to_list()
    data = [json.loads(s) for s in json_data]
    normalized_df = pd.json_normalize(data, 'entities')
    return pd.Series(list(set(normalized_df['name'])))


def entity_frequencies(df: pd.DataFrame, entities: pd.Series, column: str):
    df['tokenized'] = df[column].str.split()
    exploded_df = df.explode('tokenized')
    word_counts = exploded_df['tokenized'].value_counts()
    entity_counts = pd.DataFrame(word_counts[word_counts.index.isin(entities)])
    entity_counts['normalized'] = entity_counts.apply(lambda x: x/len(df))
    return entity_counts


def entity_averages(df: pd.DataFrame, column: str) -> pd.DataFrame:
    json_data = df[column].to_list()
    data = [json.loads(s) for s in json_data]
    normalized_df = pd.json_normalize(data, 'entities')

    entity_counts = normalized_df['name'].value_counts()
    normalized_counts = normalized_df['name'].value_counts(normalize=True)

    salience_df = normalized_df.groupby('name')['salience'].mean()
    sentiment_score_df = normalized_df.groupby('name')['sentiment.score'].mean()
    sentiment_magnitude_df = normalized_df.groupby('name')['sentiment.magnitude'].mean()

    analysis_df = pd.DataFrame({
        'name': entity_counts.index.values,
        'count': entity_counts,
        'count.normalized': normalized_counts
    })

    for grouped_df in [salience_df, sentiment_score_df, sentiment_magnitude_df]:
        analysis_df = analysis_df.merge(grouped_df, left_index=True, right_index=True)

    analysis_df = analysis_df.reset_index(drop=True)

    return analysis_df
