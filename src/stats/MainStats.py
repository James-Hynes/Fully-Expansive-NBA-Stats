
from src.util.EntryManipulation import Stat

class LeagueLeaders(Stat):

    def __init__(self, StatCategory='PTS'):
        params = {
            'LeagueID': '00',
            'PerMode': 'PerGame',
            'Scope': 'S',
            'Season': '2015-16',
            'SeasonType': 'Regular Season',
            'StatCategory': StatCategory
        }

        url = 'http://stats.nba.com/stats/leagueleaders?'
        super().__init__(url, params)
        self.data = self.data.json()['resultSet']['rowSet']


class TeamStats(Stat):

    def __init__(self):
        params = {
            'Conference': '',
            'DateFrom': '',
            'DateTo': '',
            ''
            'LeagueID': '00'
        }
        url = 'http://stats.nba.com/stats/leaguedashteamstats?'

        super().__init__()
print(LeagueLeaders().get(0))

