import requests
import datetime
import time


class CurrentDailyGames:

    def __init__(self):
        self.url = 'http://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate='

        dateobj = datetime.date.fromtimestamp(time.time())

        self.date = '{0}%2F{1}%2F{2}'.format(dateobj.month, dateobj.day, dateobj.year)

        self.data = requests.get(self.url+self.date)

    def game_lines(self):
        return self.data.json()['resultSets'][0]['rowSet']


print(CurrentDailyGames().game_lines())