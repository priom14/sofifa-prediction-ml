#Scraping EAFC24 data from sofifa


from bs4 import BeautifulSoup
import requests
import json
import time
import re

noPages = 289
offset = [int(x*60) for x in range(noPages)]

# print(offset)

player_list = []

st = time.time()
for i in offset:    
    url = f"https://sofifa.com/players?showCol%5B0%5D=pi&showCol%5B1%5D=ae&showCol%5B2%5D=hi&showCol%5B3%5D=wi&showCol%5B4%5D=pf&showCol%5B5%5D=oa&showCol%5B6%5D=pt&showCol%5B7%5D=bo&showCol%5B8%5D=bp&showCol%5B9%5D=gu&showCol%5B10%5D=vl&showCol%5B11%5D=wg&showCol%5B12%5D=rc&showCol%5B13%5D=tt&showCol%5B14%5D=bs&showCol%5B15%5D=wk&showCol%5B16%5D=tc&offset={i}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    print(f"fetching data for page - {i/60} ......")
    st_ft = time.time()
    players = soup.find('tbody').find_all('tr')
    for player in players:
        
        name = player.find('a').text
        position = player.find('div').text
        age, base, potential = player.find('td', {'class': 'd2', 'data-col': 'ae'}).text, player.find('td', {'class': 'd2', 'data-col': 'oa'}).text, player.find('td', {'class': 'd2', 'data-col': 'pt'}).text
        growth = int((re.split(r'[+-]', potential))[0]) - int((re.split(r'[+-]', base))[0])
        id = player.find('td', class_ = "d6").text
        hieght = player.find('td', {'class': 's10', 'data-col': 'hi'}).text
        wieght = player.find('td', {'class': 's10', 'data-col': 'wi'}).text
        foot = player.find('td', {'class': 's10', 'data-col': 'pf'}).text
        marketValue = player.find('td', {'class': 'd6', 'data-col': 'vl'}).text.replace("\u20ac", "")
        wage = player.find('td', {'class': 'd6', 'data-col': 'wg'}).text.replace("\u20ac", "")
        releaseClause = player.find('td', {'class': 'd6', 'data-col': 'rc'}).text.replace("\u20ac", "")
        
        # print(type(name))
        
        player_dict = {
            "name": f"{name}",
            "position": position,
            "age": age,
            "base": base,
            "potential": potential,
            "growth": growth,
            "id": id,
            "hieght": hieght,
            "weight": wieght,
            "foot": foot,
            "mValue": marketValue,
            "wage": wage,
            "rc": releaseClause
        }

    
        player_list.append(player_dict)
    end_ft = time.time()
    
    print(f"Data fetched in {end_ft-st_ft}")

end = time.time()
    
       
with open('player.json', 'w') as file:
    json.dump(player_list, file)

print(f"Total data fetched in {end - st} secs")
print(len(player_list))

