# Eva Tarr, 11234313, ELT783

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def numOfWordsAndPopularity():
    # File path can change to the dataset we want to work with
    file_path_comments = "one-year-of-doge-on-reddit-comments.csv"
    allComments = pd.read_csv(file_path_comments, encoding='utf-8')             # Read the csv file
    comments_cleaned = allComments.dropna(axis=1, how='all')                    # Clean all the empty columns
    clean = comments_cleaned.dropna()                                           # Clean all of the empty rows

    lengthOfComment = {}
    for i, row in clean.iterrows():
        comment_text = str(row['body'])
        comment_name = row['id']
        comment_score = row['score']
        comment_total = 0
        for word in comment_text.split():
            if len(word) > 2:
                comment_total += 1
        lengthOfComment[comment_name] = (comment_total, comment_score)

    commentLengths = [length for length, _ in lengthOfComment.values()]
    commentScores = [score for _, score in lengthOfComment.values()]
    commentCoefficient = np.corrcoef(commentLengths, commentScores)[0, 1]

    print(commentCoefficient)


    # Ranged for the number of words
    word_ranges = [(0, 20), (21, 40), (41, 60), (61, 80), (81,100), (101,float('inf'))]
    grouped_scores = {}
    for post, data in lengthOfComment.items():
        words, score = data
        for start, end in word_ranges:
            if start <= words <= end:
                if (start, end) not in grouped_scores:
                    grouped_scores[(start, end)] = {'sum': 0, 'count': 0}
                grouped_scores[(start, end)]['sum'] += score
                grouped_scores[(start, end)]['count'] += 1
                break

    xAxis = [f"{start}-{end}" for start, end in word_ranges]            # Get all xAxis names
    yAxis = []
    for key, value in grouped_scores.items():                           # Get all yAxis names (left hand side)
        yAxis.append(value['count'])

    yAxis2 = []
    for key, value in grouped_scores.items():                           # get all second yAxis names (right hand side)
        average = value['sum'] / value['count']
        yAxis2.append(average)

    # Display the graph
    fig, leftAxis = plt.subplots(figsize=(20, 12))
    leftAxis.bar(xAxis, yAxis, color='pink')
    leftAxis.set_xlabel('Number Of Words')
    leftAxis.set_ylabel('Number Of Posts')
    plt.xticks(rotation='vertical')

    rightAxis = leftAxis.twinx()
    rightAxis.plot(xAxis, yAxis2, color='red', marker='o', label='Average Score')
    rightAxis.set_ylabel('Average Score', color='red')
    rightAxis.tick_params('y', colors='red')

    plt.title("Number of Words in a Comment and their Average Scores")
    plt.show()

numOfWordsAndPopularity()
