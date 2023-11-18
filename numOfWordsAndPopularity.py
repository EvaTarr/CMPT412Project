# Eva Tarr, 11234313, ELT783
# DONE
import pandas as pd
import matplotlib.pyplot as plt


def numOfWordsAndPopularity():
    file_path_comments = "reddit-r-nonewnormal-dataset-comments.csv"

    allComments = pd.read_csv(file_path_comments, encoding='utf-8')
    comments_cleaned = allComments.dropna(axis=1, how='all')
    clean = comments_cleaned.dropna()

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

    xAxis = [f"{start}-{end}" for start, end in word_ranges]
    yAxis = []
    for key, value in grouped_scores.items():
        yAxis.append(value['count'])

    yAxis2 = []
    for key, value in grouped_scores.items():
        average = value['sum'] / value['count']
        yAxis2.append(average)
    print(yAxis2)

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
