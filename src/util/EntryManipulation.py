import requests

def parse_historical_date(input):
    return input.split(' ')[0]


def parse_tweet_date(input):
    split_input = input.split(' ')
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
              'Nov', 'Dec']
    return '{0}/{1}/{2}'.format(months.index(split_input[1])+1, split_input[2], split_input[len(split_input)-1])


def reformat_tweet_text(input):
    inp = input.replace('\n\n', ' ').replace('&amp;', '&').replace('\n', ' ')
    split = inp.split(' ')
    return ' '.join(split[:len(split)-1])


def delete(char, string):
    try:
        return string.replace(char, '')
    except TypeError:
        return string


class Stat:

    def __init__(self, url, params):
        try:
            self.data = requests.get(url, params).json()['resultSet']['rowSet']
        except requests.RequestException:
            self.data = None

    def get(self, index):
        try:
            return self.data[index]
        except AttributeError:
            return None
        except KeyError:
            return None