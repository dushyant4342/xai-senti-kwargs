from utils.load_env import load_environment
from utils.helpers import save_to_excel
from agents.content_retriever import fetch_tweets
from agents.sentiment_analyzer import analyze_sentiment

def main():
    config = load_environment()
    df = fetch_tweets(config)
    #df.to_csv("fetched_twitter_data.csv",index =False)
    if not df.empty:
        print(f'fetched_tweets : {df} ')
        df = analyze_sentiment(df)
        path = save_to_excel(df)
        print(f"Saved final output to {path}")
    else:
        print("No tweets fetched.")

if __name__ == "__main__":
    main()
