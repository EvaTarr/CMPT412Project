# Eva Tarr, 11234313, ELT783
# Using the posts that relate to the trucker strike
# Checking to see if there is a correlation to post popularity (# of likes) and the sentiment connected to it
import pandas as pd
import matplotlib.pyplot as plt


def truckerPosts():
    file_path = "the-2022-trucker-strike-on-reddit-comments.csv"
    allTruckerPosts = pd.read_csv(file_path, encoding='utf-8')
    n = 50
    truckerPosts_cleaned = allTruckerPosts.dropna(axis=1, how='all')
    truckerPosts_sorted = truckerPosts_cleaned.sort_values(by='score', ascending=False)
    top_posts = truckerPosts_sorted.head(n)

    fig, leftAxis = plt.subplots(figsize=(20, 10))

    leftAxis.bar(top_posts['id'], top_posts['score'], color='skyblue', label='Score')
    leftAxis.set_xlabel('Post Title')
    leftAxis.set_ylabel('Score', color='skyblue')
    leftAxis.tick_params('y', colors='skyblue')

    rightAxis = leftAxis.twinx()
    rightAxis.plot(top_posts['id'], top_posts['sentiment'], color='orange', marker='o', label='Sentiment')
    rightAxis.set_ylabel('sentiment', color='orange')
    rightAxis.tick_params('y', colors='orange')

    plt.title(f'Top {n} Most Liked Posts with Sentiment')
    fig.tight_layout()
    fig.legend(loc='upper left', bbox_to_anchor=(0.8, 0.8))

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90, ha='right')

    plt.show()

#Run
truckerPosts()
