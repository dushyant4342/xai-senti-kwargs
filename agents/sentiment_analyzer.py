from transformers import pipeline
import numpy as np #<2.0
import pandas as pd


def analyze_sentiment(df):
    sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    results = sentiment_pipeline(df["content"].tolist(), truncation=True)

    print(results)

    df["sentiment"] = [res["label"] for res in results]
    df["score"] = [res["score"] for res in results]
    return df




# data = [
#     {
#         "date": "2025-04-01T10:12:34Z",
#         "keyword": "onecard",
#         "title": "Love using OneCard",
#         "content": "Love using OneCard. It's fast and the app is smooth!",
#         "comments": "",  # You can fill this later if replies are fetched
#         "url": "https://twitter.com/user123/status/1234567890123456789"
#     },
#     {
#         "date": "2025-04-01T11:45:00Z",
#         "keyword": "onescore",
#         "title": "Onescore needs improvement",
#         "content": "Onescore needs better transparency on how scores are calculated.",
#         "comments": "",
#         "url": "https://twitter.com/user456/status/9876543210987654321"
#     }
# ]

# df = pd.DataFrame(data)

# print(analyze_sentiment(df))