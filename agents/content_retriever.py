import requests
import pandas as pd

def fetch_tweets(config):
    headers = {"Authorization": f"Bearer {config['bearer_token']}"}
    tweets_data = []

    for keyword in config['keywords']:
        query = f"{keyword} lang:en -is:retweet"
        url = "https://api.twitter.com/2/tweets/search/recent"
        params = {
            "query": query,
            "tweet.fields": "created_at,author_id,text,conversation_id",
            "start_time": config["start_date"],
            "end_time": config["end_date"],
            "max_results": 11,
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error: Status Code {response.status_code}")
            print(f"Response: {response.text}")
            continue


        if response.status_code == 200:
            print(f"Connection Established") #1 requests / 15 mins PER USER
            for tweet in response.json().get("data", []):
                tweets_data.append({
                    "date": tweet["created_at"],
                    "keyword": keyword,
                    "title": tweet["text"].split(".")[0],
                    "content": tweet["text"],
                    "comments": "",  # optional enhancement
                    "url": f"https://twitter.com/{tweet['author_id']}/status/{tweet['id']}"
                })

    return pd.DataFrame(tweets_data)
