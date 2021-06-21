import pandas as pd
import tweepy
from datetime import date
from urllib.request import Request, urlopen
from src.keys import *

req = Request('https://www.worldometers.info/coronavirus/country/us/', headers={'User-Agent': 'Mozilla/5.0',
                                                                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',})

webpage = urlopen(req).read()

df = pd.read_html(webpage)[0]

hi = df.loc[df['USAState'].isin(['Hawaii'])]
hi = hi.fillna(0)

total_cases = int(hi.iloc[0]['TotalCases'])
new_cases = int(hi.iloc[0]['NewCases'])
total_deaths = int(hi.iloc[0]['TotalDeaths'])
new_deaths = int(hi.iloc[0]['NewDeaths'])

message = 'HI Coronavirus Stats for ' + str(date.today()) +'\
        \nTotal cases: ' + str(total_cases) + '\
        \nNew cases: ' + str(new_cases) + '\
        \nTotal deaths: ' + str(total_deaths) + '\
        \nNew deaths: ' + str(new_deaths) + '\
        \nCheck the link: https://www.worldometers.info/coronavirus/country/us'

account = tweepy.OAuthHandler(api_key, api_key_secret)

account.set_access_token(access_token, access_token_secret)

bot = tweepy.API(account)

bot.update_status(message)