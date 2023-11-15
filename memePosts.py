# Eva Tarr, 11234313, ELT783

import pandas as pd
import matplotlib.pyplot as plt

def memePosts():
    file_path_posts = "one-year-of-doge-on-reddit-posts.csv"
    file_path_comments = "one-year-of-doge-on-reddit-comments.csv"

    allPosts = pd.read_csv(file_path_posts, encoding='utf-8')
    allComments = pd.read_csv(file_path_comments, encoding='utf-8')

    posts_cleaned = allPosts.dropna(axis=1, how='all')
    comments_cleaned = allComments.dropna(axis=1, how='all')

    fig, leftAxis = plt.subplots(figsize=(20, 10))

