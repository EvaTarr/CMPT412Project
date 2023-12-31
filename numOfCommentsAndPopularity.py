# Eva Tarr, 11234313, ELT783

import pandas as pd
import matplotlib.pyplot as plt
def numOfCommentsAndPopularity():
    # File names change based on which data you want to run for
    # BOTH NEED TO BE FROM THE SAME SUBREDDIT
    file_path_comments = "one-year-of-tsla-on-reddit-comments.csv"
    file_path_posts = "one-year-of-tsla-on-reddit-posts.csv"

    allComments = pd.read_csv(file_path_comments, encoding='utf-8')     # Read all the comments
    allPosts = pd.read_csv(file_path_posts, encoding='utf-8')           # Read all the posts
    comments_cleaned = allComments.dropna(axis=1, how='all')            # Remove all empty columns
    posts_cleaned = allPosts.dropna(axis=1, how='all')                  # Remove all empty rows

    posts_commentNum = {}
    for i, row in posts_cleaned.iterrows():
        posts_commentNum[row['id']] = [row['score'], 0]
    for j, row in comments_cleaned.iterrows():
        commentUrl = str(row['permalink']).split("/")[6]
        if commentUrl in posts_commentNum.keys():
            posts_commentNum[commentUrl][1] += 1
    removeMe = []
    for post in posts_commentNum.keys():
        if posts_commentNum[post] == 0:
            removeMe.append(post)
    # remove all posts that are empty for the sake of cleaning data that does not result in a value
    for post in removeMe:
        posts_commentNum.pop(post)

    # Interchangeable ranged (one for by 10 one for by 5)
    comment_ranges_by10 = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 70), (71, 80), (81, 90), (91, 100), (101, float('inf'))]
    comment_ranges = [(0, 5), (6, 10), (11, 15), (16, 20), (21, 25), (26, 30), (31, 35), (36, 40), (41, 45), (46, 50),(51, float('inf'))]
    grouped_comments = {}

    # Group all the posts based on the number of comments they have
    for post, data in posts_commentNum.items():
        score, num = data
        for start, end in comment_ranges:
            if start <= num <= end:
                if (start, end) not in grouped_comments:
                    grouped_comments[(start, end)] = {'allScores': 0, 'count': 0}
                grouped_comments[(start, end)]['allScores'] += score
                grouped_comments[(start, end)]['count'] += 1
                break

    xAxis = [f"{start}-{end}" for start, end in comment_ranges]     # Get all the names for the xAxis
    yAxis = []
    for key, value in grouped_comments.items():                     # Get all the names for the yAxis (left hand side)
        yAxis.append(value['count'])

    yAxis2 = []
    for key, value in grouped_comments.items():                     # Get all the name for the 2nd yAxis (right hand side)
        average = value['allScores'] / value['count']
        yAxis2.append(average)


    # Display the graph
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
