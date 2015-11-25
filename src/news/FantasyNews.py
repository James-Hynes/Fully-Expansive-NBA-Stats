import requests


class RotowirePlayerStatlines:

    def __init__(self):
        self.url = 'http://stats.nba.com/feeds/RotoWirePlayers-583598/masterslimlist.json'

        self.data = requests.get(self.url)

    def get_statlines_data(self, lim=None):
        if lim:
            return [statline for e, statline in enumerate(self.data.json()['ListItems']) if e < lim]
        else:
            return self.data.json()['ListItems']

    def get_statline(self, statline_num=0):
        return self.data.json()['ListItems'][statline_num]

    def set_headlines_as_dict(self):
        return {'{0} {1}'.format(line['FirstName'], line['LastName']): line for line in self.data.json()['ListItems']}

    @staticmethod
    def normalized_statline_text(statline_data):
        return "{0} {1}".format(statline_data['ListItemCaption'], statline_data['ListItemDescription'])

    @staticmethod
    def timestamp_statline(statline_data):
        return statline_data['ListItemPubDate']


c = RotowirePlayerStatlines()
print(c.set_headlines_as_dict())
