# Eva Tarr, 11234313, ELT783

import pandas as pd
import matplotlib.pyplot as plt


def numOfWordsAndPopularity():
    file_path_comments = "one-year-of-doge-on-reddit-comments.csv"
    topN = 50

    allComments = pd.read_csv(file_path_comments, encoding='utf-8')
    comments_cleaned = allComments.dropna(axis=1, how='all')
    comments_sorted = comments_cleaned.sort_values(by='score', ascending=False)
    top_comments = comments_sorted.head(topN)

    lengthOfComment = {}
    sentiments = []
    for i, row in top_comments.iterrows():
        comment_text = row['body']
        comment_name = row['id']
        comment_total = 0
        for word in comment_text.split():
            if len(word) > 2:
                comment_total += 1
        lengthOfComment[comment_name] = comment_total
        sentiments.append(row['sentiment'])

    comments = [str(comment) for comment in lengthOfComment.keys()]
    commentLength = list(lengthOfComment.values())
    fig, leftAxis = plt.subplots(figsize=(20, 12))
    leftAxis.bar(comments, commentLength, color='pink')
    leftAxis.set_xlabel('Comment')
    leftAxis.set_ylabel('Comment Length')
    plt.xticks(rotation='vertical')

    rightAxis = leftAxis.twinx()
    rightAxis.plot(comments, sentiments, color='red', marker='o', label='Sentiment')
    rightAxis.set_ylabel('score', color='red')
    rightAxis.tick_params('y', colors='red')

    plt.title("Number of words in a comment")
    plt.show()

numOfWordsAndPopularity()
