# Eva Tarr, 11234313, ELT783

import pandas as pd
import matplotlib.pyplot as plt


def numOfComments():
    file_path_comments = "reddit-r-bitcoin-data-for-jun-2022-comments.csv"
    file_path_posts = "reddit-r-bitcoin-data-for-jun-2022-posts.csv"
    topN = 100

    allComments = pd.read_csv(file_path_comments, encoding='utf-8')
    allPosts = pd.read_csv(file_path_posts, encoding='utf-8')

    Posts_cleaned = allPosts.dropna(axis=1, how='all')
    Comments_cleaned = allComments.dropna(axis=1, how='all')
    Posts_sorted = Posts_cleaned.sort_values(by='score', ascending=False)
    top_posts = Posts_sorted.head(topN)

    posts_commentNum = {}
    for j, posts in top_posts.iterrows():
        postID = posts['id']
        posts_commentNum[postID] = 0

    for i, row in Comments_cleaned.iterrows():
        link = row['permalink']
        splitLink = link.split('/')
        if splitLink[6] in posts_commentNum:
            posts_commentNum[splitLink[6]] += 1

    fig, leftAxis = plt.subplots(figsize=(20, 10))

    leftAxis.bar(posts_commentNum.keys(), posts_commentNum.values(), color='lightsteelblue', label='Number of comments')
    leftAxis.set_xlabel('Post ID')
    leftAxis.set_ylabel('Number of comments', color='lightsteelblue')
    leftAxis.tick_params('y', colors='lightsteelblue')
    # rotate all the x ID's to be vertical for better readability
    plt.xticks(rotation='vertical')

    plt.title("Number of comments on a post")
    plt.show()

numOfComments()
