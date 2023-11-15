# Eva Tarr, 11234313, ELT783
# Checking to see if there is a correlation between number of comments and their average score

import pandas as pd
import matplotlib.pyplot as plt

def conributorsAndAverageScore():
    file_path_comments = "the-reddit-climate-change-dataset-comments.csv"
    topN = 50

    allComments = pd.read_csv(file_path_comments, encoding='utf-8',nrows=1000000)
    comments_cleaned = allComments.dropna(axis=1, how='all')

    post_comments = {}
    post_score = {}
    print("format data...")
    for i, row in comments_cleaned.iterrows():
        user_ID = row['created_utc']
        user_score = row['score']
        if user_ID in post_comments:
            post_comments[user_ID] += 1
            post_score[user_ID] += user_score
        else:
            post_comments[user_ID] = 1
            post_score[user_ID] = user_score

    print("sort data...")
    sorted_comments = dict(sorted(post_comments.items(), key=lambda item: item[1], reverse=True)[:topN])

    users = [str(user) for user in sorted_comments.keys()]
    numOfPosts = list(sorted_comments.values())
    scores = []
    for user in sorted_comments:
        scores.append(post_score[user]/sorted_comments[user])
    print("create graph...")
    fig, leftAxis = plt.subplots(figsize=(20, 12))

    leftAxis.bar(users, numOfPosts, color='pink')
    leftAxis.set_xlabel('Users')
    leftAxis.set_ylabel('Number of Comments')
    plt.xticks(rotation='vertical')

    rightAxis = leftAxis.twinx()
    rightAxis.plot(users, scores, color='red', marker='o', label='Average Score')
    rightAxis.set_ylabel('score', color='red')
    rightAxis.tick_params('y', colors='red')

    plt.title("Number of comments and Average Score")
    plt.show()

conributorsAndAverageScore()
