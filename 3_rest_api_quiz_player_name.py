import requests

team = input('Insert team name: ')
url_footbal = f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={team}'
data = requests.get(url_footbal)
players = data.json()['player']

for player in players:
    print(f"Player name: {player['strPlayer']}")
