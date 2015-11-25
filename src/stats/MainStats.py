import requests


class LeagueLeaders:

    def __init__(self, **kwargs):
        params = kwargs

        self.url = 'http://stats.nba.com/stats/leagueleaders?'

        self.data = requests.get(self.url, params)