import tweepy
from datetime import date
from src.keys import *
import requests

url = 'https://health.hawaii.gov/coronavirusdisease2019/'
r = requests.get(url)
my_text = r.text

full_array = bytearray(my_text, 'utf-8')


pre_total_cases = full_array.partition(b'Total cases:</span> <span class="value">')
after_total_cases = pre_total_cases[2].partition(b' (')
after_new_cases = after_total_cases[2].partition(b' newly reported')
before_hawaii = after_new_cases[2].partition(b'Hawai&#8217;i County:</span> <span class="value">')
before_honolulu = before_hawaii[2].partition(b'</span></dd>\n<dd><span class="label">Honolulu County:</span> <span class="value">')
before_kauai = before_honolulu[2].partition(b'</span></dd>\n<dd><span class="label">Kaua&#8217;i County:</span> <span class="value">')
before_maui = before_kauai[2].partition(b'</span></dd>\n<dd><span class="label">Maui County:</span> <span class="value">')
before_deaths = before_maui[2].partition(b'Hawaii deaths:</span> <span class="value">')
after_deaths = before_deaths[2].partition(b'</span>')

#print(before_maui[2])

total_cases_incorrect = after_total_cases[0]
total_cases_correct = bytearray

for index, value in enumerate(total_cases_incorrect):
    total_cases_correct = bytearray.decode(total_cases_incorrect)
    if value not in range(48,58):
        total_cases_correct = bytearray.decode(total_cases_incorrect[0:index])
        break

new_cases = bytearray.decode(after_new_cases[0])
hawaii = bytearray.decode(before_honolulu[0])
honolulu = bytearray.decode(before_kauai[0])
kauai = bytearray.decode(before_maui[0])

maui_incorrect = before_deaths[0]
maui_correct = bytearray

for index, value in enumerate(maui_incorrect):
    maui_correct = bytearray.decode(maui_incorrect)
    if value not in range(48,58):
        maui_correct = bytearray.decode(maui_incorrect[0:index])
        break



deaths_incorrect = after_deaths[0]
deaths_correct = bytearray

for index, value in enumerate(deaths_incorrect):
    deaths_correct = bytearray.decode(deaths_incorrect)
    if value not in range(48,58):
        deaths_correct = bytearray.decode(deaths_incorrect[0:index])
        break


message = 'HI Coronavirus Stats for ' + str(date.today()) +'\
        \nTotal cases: ' + str(total_cases_correct) + '\
        \nNew cases: ' + str(new_cases) + '\
        \nHawai’i County: ' + str(hawaii) + '\
        \nHonolulu County: ' + str(honolulu) + '\
        \nKauai County: ' + str(kauai) + '\
        \nMaui County: ' + str(maui_correct) + '\
        \nTotal Deaths: ' + str(deaths_correct) + '\
        \nhttps://health.hawaii.gov/coronavirusdisease2019/'

print(str(total_cases_correct)+'hi')

account = tweepy.OAuthHandler(api_key, api_key_secret)

account.set_access_token(access_token, access_token_secret)

bot = tweepy.API(account)

bot.update_status(message)


