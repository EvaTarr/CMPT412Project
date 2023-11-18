# Eva Tarr, 11234313, ELT783
# DONE
import pandas as pd
import matplotlib.pyplot as plt
def popularityAndSentiment():
    file_path = "reddit-r-nonewnormal-dataset-comments.csv"
    # number of posts to get (top n)
    n = 50
    # read file with utf-8
    allPosts = pd.read_csv(file_path, encoding='utf-8')
    # drop all empty columns
    Posts_cleaned = allPosts.dropna(axis=1, how='all')
    Posts_sorted = Posts_cleaned.sort_values(by='score', ascending=False)
    top_posts = Posts_sorted.head(n)
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

    plt.title(f'Top {n} Most Liked Comments with Sentiment')
    fig.tight_layout()
    # place the legend in the top right hand side
    fig.legend(loc='upper right', bbox_to_anchor=(0.95, 0.95))
    plt.show()

# run
popularityAndSentiment()
