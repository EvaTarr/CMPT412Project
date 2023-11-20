# Eva Tarr, 11234313, ELT783

import pandas as pd
import matplotlib.pyplot as plt


def numOfCommentsAndPopularity():
    file_path_comments = "wallstreetbets-posts-and-comments-for-august-2021-comments.csv"
    file_path_posts = "wallstreetbets-posts-and-comments-for-august-2021-posts.csv"

    allComments = pd.read_csv(file_path_comments, encoding='utf-8')
    allPosts = pd.read_csv(file_path_posts, encoding='utf-8')

    comments_cleaned = allComments.dropna(axis=1, how='all')
    posts_cleaned = allPosts.dropna(axis=1, how='all')


    posts_commentNum = {}
    for i, row in posts_cleaned.iterrows():
        posts_commentNum[row['id']] = [row['score'], 0]
    for j, row in comments_cleaned.iterrows():
        commentUrl = str(row['permalink']).split("/")[6]
        if commentUrl in posts_commentNum.keys():
            posts_commentNum[commentUrl][1] += 1

    comment_ranges = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 70), (71, 80), (81, 90), (91, 100), (101, float('inf'))]
    grouped_comments = {}
    for post, data in posts_commentNum.items():
        score, num = data
        for start, end in comment_ranges:
            if start <= num <= end:
                if (start, end) not in grouped_comments:
                    grouped_comments[(start, end)] = {'allScores': 0, 'count': 0}
                grouped_comments[(start, end)]['allScores'] += score
                grouped_comments[(start, end)]['count'] += 1
                break

    xAxis = [f"{start}-{end}" for start, end in comment_ranges]
    yAxis = []
    for key, value in grouped_comments.items():
        yAxis.append(value['count'])

    yAxis2 = []
    for key, value in grouped_comments.items():
        average = value['allScores'] / value['count']
        yAxis2.append(average)


    fig, leftAxis = plt.subplots(figsize=(20, 12))
    leftAxis.bar(xAxis, yAxis, color='pink')
    leftAxis.set_xlabel('Number of Comments')
    leftAxis.set_ylabel('Number Of Posts')
    plt.xticks(rotation='vertical')

    rightAxis = leftAxis.twinx()
    rightAxis.plot(xAxis, yAxis2, color='red', marker='o', label='Average Score')
    rightAxis.set_ylabel('Average Score', color='red')
    rightAxis.tick_params('y', colors='red')

    plt.title("Number of Words in a Comment and their Average Scores")
    plt.show()

numOfCommentsAndPopularity()
