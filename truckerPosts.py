# Eva Tarr, 11234313, ELT783
# Using the posts that relate to the trucker strike
# Checking to see if there is a correlation to post popularity (# of likes) and the sentiment connected to it
import pandas as pd
import matplotlib.pyplot as plt
def truckerPosts():
    file_path = "the-2022-trucker-strike-on-reddit-comments.csv"
    # number of posts to get (top n)
    n = 50
    # read file with utf-8
    allTruckerPosts = pd.read_csv(file_path, encoding='utf-8')
    # drop all empty columns
    truckerPosts_cleaned = allTruckerPosts.dropna(axis=1, how='all')
    truckerPosts_sorted = truckerPosts_cleaned.sort_values(by='score', ascending=False)
    top_posts = truckerPosts_sorted.head(n)

    fig, leftAxis = plt.subplots(figsize=(20, 10))

    leftAxis.bar(top_posts['id'], top_posts['score'], color='lightsteelblue', label='Score')
    leftAxis.set_xlabel('Post ID')
    leftAxis.set_ylabel('Score', color='lightsteelblue')
    leftAxis.tick_params('y', colors='lightsteelblue')
    # rotate all the x ID's to be vertical for better readability
    plt.xticks(rotation='vertical')

    # create a right axis to display the sentiment values
    rightAxis = leftAxis.twinx()
    rightAxis.plot(top_posts['id'], top_posts['sentiment'], color='red', marker='o', label='Sentiment')
    rightAxis.set_ylabel('sentiment', color='red')
    rightAxis.tick_params('y', colors='red')

    plt.title(f'Top {n} Most Liked Posts with Sentiment')
    fig.tight_layout()
    # place the legend in the top right hand side
    fig.legend(loc='upper right', bbox_to_anchor=(0.95, 0.95))
    plt.show()

# run
truckerPosts()
