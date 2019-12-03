from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2019,1,1)
end_date = dt.date(2019,12,1)

limit = 100
lang = 'english'

tweets = query_tweets("Indonesia", begindate = begin_date, enddate = end_date, limit = limit, lang = lang)

df = pd.DataFrame(t.__dict__ for t in tweets)
df.to_excel('Tweets.xlsx')