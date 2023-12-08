# Settings Instructions

### Standard Filetree Structure

---

The following describes the initial structure of a folder before any processing has been performed.
```
├── gamestop
│    ├── processed
│    │   ├── plots
│    ├── six-months-of-gme-on-reddit-comments.csv
│    ├── six-months-of-gme-on-reddit-comments.csv.zip
│    ├── six-months-of-gme-on-reddit-posts.csv
│    ├── six-months-of-gme-on-reddit-posts.csv.zip
│    └── wallstreetbets.zip
```

The following describes a filetree after all processsing has been complete.
```
├── gamestop
│    ├── processed
│    │   ├── plots
│    │   │   ├── gamestop "wallstreetbets" subreddit: Top 10 Most Frequent High Scoring Entities over Low.png
│    │   │   ├── gamestop "wallstreetbets" subreddit: Top 10 Most Frequent High Scoring Entities over Moderate.png
│    │   │   ├── gamestop "wallstreetbets" subreddit: Top 10 Most Frequent Low Scoring Entities over High.png
│    │   │   └── gamestop "wallstreetbets" subreddit: Top 10 Most Frequent Low Scoring Entities over Moderate.png
│    │   ├── six-months-of-gme-on-reddit-comments_high-low-freq.csv
│    │   ├── six-months-of-gme-on-reddit-comments_high-moderate-freq.csv
│    │   ├── six-months-of-gme-on-reddit-comments_low-moderate-freq.csv
│    │   ├── six-months-of-gme-on-reddit-comments_low-high-freq.csv
│    │   ├── six-months-of-gme-on-reddit-comments_wallstreetbets.csv
│    │   ├── six-months-of-gme-on-reddit-comments_wallstreetbets_entities.csv
│    ├── six-months-of-gme-on-reddit-comments.csv
│    ├── six-months-of-gme-on-reddit-comments.csv.zip
│    ├── six-months-of-gme-on-reddit-posts.csv
│    ├── six-months-of-gme-on-reddit-posts.csv.zip
│    └── wallstreetbets.zip
```

### Settings Examples for 'entity_analysis.py'

---

**Download entities and perform Entity Analysis on \*comments.csv\* (six-months-of-gme-on-reddit-comments.csv)**
```
processed = False
topic = 'gamestop'
dataset = 'comments'
subreddit = 'wallstreetbets'
```
*Note: Subreddit name is essential here because it filters the data by subreddit.

**Perform Entity Analysis on \*entities.csv\* (six-months-of-gme-on-reddit-comments_wallstreetbets_entities.csv)**
```
processed = True
topic = 'gamestop'
dataset = 'entities'
subreddit = 'wallstreetbets'
```

### Settings Examples for 'graph_frequency.py'

---

**Graph on \*high-low-freq.csv\* (six-months-of-gme-on-reddit-comments_high-low-freq.csv)**
```
processed = True
topic = 'gamestop'
dataset = 'high-low-freq.csv'
subreddit = 'wallstreetbets'
```

**Perform Entity Analysis on \*low-moderate-freq.csv\* (six-months-of-gme-on-reddit-comments_low-moderate-freq.csv)**
```
processed = True
topic = 'gamestop'
dataset = 'low-moderate-freq.csv'
subreddit = 'wallstreetbets'
```