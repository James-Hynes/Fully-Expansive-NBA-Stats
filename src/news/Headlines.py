import requests
import datetime
import time
from src.util.EntryManipulation import parse_historical_date, parse_tweet_date, reformat_tweet_text


class NBABroadHeadlines:

    def __init__(self):
        self.url = 'http://stats.nba.com/feeds/StatsBeyondTheNumbersV2-594371/json.js'

        self.data = requests.get(self.url)

    def all_headlines_as_dict(self):
        return {entry['ListItemCaption']: {'ListItemLink': entry['ListItemLink'], 'ListItemPubDate':
            entry['ListItemPubDate'], 'ListItemCaption': entry['ListItemCaption']} for entry in
                self.data.json()['ListItems']}


class NBAHistory:

    def __init__(self):
        self.url = 'http://stats.nba.com/feeds/StatsV2History-589801/json.js'

        self.data = requests.get(self.url)

        date_obj = datetime.date.fromtimestamp(time.time())

        self.formatted_date = '{0}/{1}/{2}'.format(date_obj.month, date_obj.day, date_obj.year)

    def all_headlines(self):
        return {parse_historical_date(entry['ListItemPubDate']): {'ListItemCaption': entry['ListItemCaption'],
                                                                  'ListenItemLink': entry['ListItemLink'],
                                                                  'ListItemDescription': entry['ListItemDescription'],
                                                                  'ListItemPubDate': entry['ListItemPubDate']}
                for entry in self.data.json()['ListItems']}

    def today_headlines(self):
        return [{'ListItemCaption': entry['ListItemCaption'], 'ListenItemLink': entry['ListItemLink'],
                'ListItemDescription': entry['ListItemDescription'], 'ListItemPubDate': entry['ListItemPubDate']}
                for entry in self.data.json()['ListItems'] if parse_historical_date(entry['ListItemPubDate']) ==
                self.formatted_date]


class NBAPrecheckedTweets:

    def __init__(self):
        self.url = 'http://api.massrelevance.com/NBADMR/nbacomnewstweets.json'

        self.data = requests.get(self.url)

    @staticmethod
    def tweet_text(tweet):
        return reformat_tweet_text(tweet['text'])

    @property
    def all_tweets_as_list(self):
        return [{'created_at': entry['created_at'], 'id': entry['id'], 'favorite_count': entry['favorite_count'],
                 'lang': entry['lang'], 'retweet_count': entry['retweet_count'], 'text': entry['text'],
                 'truncated': entry['truncated'], 'user': entry['user']} for entry in self.data.json()]

    @property
    def all_tweets_as_dict(self):
        return {parse_tweet_date(entry['created_at']): {'created_at': entry['created_at'], 'id': entry['id'],
                                                        'favorite_count': entry['favorite_count'],
                                                        'lang': entry['lang'], 'retweet_count': entry['retweet_count'],
                                                        'text': entry['text'], 'truncated': entry['truncated'],
                                                        'user': entry['user']} for entry in self.data.json()}


print(NBAHistory().all_headlines())