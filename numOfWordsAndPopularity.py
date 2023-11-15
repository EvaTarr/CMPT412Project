# Eva Tarr, 11234313, ELT783

import pandas as pd
import matplotlib.pyplot as plt


def numOfWordsAndPopularity():
    file_path_comments = "the-reddit-climate-change-dataset-comments.csv"
    topN = 50

    allComments = pd.read_csv(file_path_comments, encoding='utf-8', nrows=1000000)
    comments_cleaned = allComments.dropna(axis=1, how='all')
    comments_sorted = comments_cleaned.sort_values(by='score', ascending=False)
    top_comments = comments_sorted.head(topN)

    lengthOfComment = {}
    for i, row in top_comments.iterrows():
        comment_text = row['body']
        comment_name = row['id']
        comment_total = 0
        for word in comment_text.split():
            if len(word) > 2:
                comment_total += 1
        lengthOfComment[id] = comment_total


numOfWordsAndPopularity()
