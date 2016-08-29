import requests
from bs4 import BeautifulSoup

player_url = 'https://www.google.com/#q='
options_url = 'https://football.fantasysports.yahoo.com/f1/draftanalysis?tab=SD&pos={POSITION}&sort=DA_AP'


player_map = {'QB': [], 'WR': [], 'RB': [], 'TE': [], 'K': [], 'DEF': []}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


for position, players in player_map.items():
    url = options_url.replace('{POSITION}', position)
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    with open(position + '.txt', 'w') as f:
        for player_name in soup.select('.Nowrap.name.F-link'):
            import pdb; pdb.set_trace()
            html = requests.get(player_url + player_name.text.replace(' ', '+'), headers=headers).text
            soup = BeautifulSoup(html, 'html.parser')
            result = soup.select('#resultStats')[0].text
            final_result = result.replace('About ', '').replace(' results', '').replace(',', '')
            print(player_name + " | " + final_result)
