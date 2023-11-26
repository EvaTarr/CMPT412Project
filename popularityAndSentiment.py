# Eva Tarr, 11234313, ELT783

import pandas as pd
import matplotlib.pyplot as plt
def popularityAndSentiment():
    # File path can change to the dataset we want to work with
    file_path = "reddit-r-bitcoin-data-for-jun-2022-comments.csv"
    n = 50  # number of posts to get (top n)
    allPosts = pd.read_csv(file_path, encoding='utf-8')  # Read the file
    Posts_cleaned = allPosts.dropna(axis=1, how='all')  # remove all empty columns
    Posts_sorted = Posts_cleaned.sort_values(by='score', ascending=False)  # Organize based on score
    top_posts = Posts_sorted.head(n)  # Only extract the top n

    correlation_coefficient = Posts_sorted['score'].corr(Posts_sorted['sentiment'])
    print(correlation_coefficient)
    # Show graph
    fig, leftAxis = plt.subplots(figsize=(20, 10))
    leftAxis.bar(top_posts['id'], top_posts['score'], color='lightsteelblue', label='Score')
    leftAxis.set_xlabel('Post ID')
    leftAxis.set_ylabel('Score', color='lightsteelblue')
    leftAxis.tick_params('y', colors='lightsteelblue')
    plt.xticks(rotation='vertical')

    # right hand side yAxis will be the sentiment
    rightAxis = leftAxis.twinx()
    rightAxis.plot(top_posts['id'], top_posts['sentiment'], color='red', marker='o', label='Sentiment')
    rightAxis.set_ylabel('sentiment', color='red')
    rightAxis.tick_params('y', colors='red')
    plt.title(f'Top {n} Most Liked Comments with Sentiment')
    fig.tight_layout()
    fig.legend(loc='upper right', bbox_to_anchor=(0.95, 0.95))
    plt.show()


popularityAndSentiment()
