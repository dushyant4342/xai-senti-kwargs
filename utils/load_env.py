from dotenv import load_dotenv
import os

def load_environment():
    load_dotenv()
    config = {
        "bearer_token": os.getenv("TWITTER_BEARER_TOKEN"),
        "start_date": os.getenv("START_DATE"),
        "end_date": os.getenv("END_DATE"),
        "keywords": ['onescore']
    }
    print(f'config : {config}')
    return config