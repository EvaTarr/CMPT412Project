# Eva Tarr, 11234313, ELT783


from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
def timeOfCreationAndScore():
    file_path = "the-antiwork-subreddit-dataset-posts.csv"

    allPosts = pd.read_csv(file_path, encoding='utf-8')
    columns_cleaned = allPosts.dropna(axis=1, how='all')
    Posts_cleaned = columns_cleaned.dropna()
    Posts_sorted = Posts_cleaned.sort_values(by='created_utc', ascending=True)

    months = {}
    monthsNum = {}
    for i, row in Posts_sorted.iterrows():
        monthName = str(datetime.utcfromtimestamp(row['created_utc']).month) + str(datetime.utcfromtimestamp(row['created_utc']).year)
        if monthName in months:
            months[monthName] += row['score']
            monthsNum[monthName] += 1
        else:
            months[monthName] = row['score']
            monthsNum[monthName] = 1

    for key in months.keys():
        months[key] /= monthsNum[key]

    fig, leftAxis = plt.subplots(figsize=(20, 10))
    leftAxis.bar(months.keys(), months.values(), color='lightsteelblue', label='Score')
    leftAxis.set_xlabel('Post ID')
    leftAxis.set_ylabel('Score', color='lightsteelblue')
    leftAxis.tick_params('y', colors='lightsteelblue')
    # rotate all the x ID's to be vertical for better readability
    plt.xticks(rotation='vertical')

    plt.title("Time of creation and the comment score")
    plt.show()


timeOfCreationAndScore()
