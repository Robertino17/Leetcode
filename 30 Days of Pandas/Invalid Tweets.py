import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets["is_greater"] = tweets["content"].apply(lambda x: 1 if len(x) > 15 else 0)
    mask = tweets["is_greater"] == 1
    return tweets.loc[mask, ["tweet_id"]]