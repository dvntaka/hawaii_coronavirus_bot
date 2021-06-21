# Created follow a tutorial at: https://towardsdatascience.com/how-to-track-coronavirus-with-python-a5320b778c8e

from datetime import date
from urllib.request import Request, urlopen
import pandas as pd
import smtplib


def get_data():
    #req = Request('https://www.worldometers.info/coronavirus/#countries', headers={'User-Agent': 'Mozilla/5.0'})
    req = Request('https://www.worldometers.info/coronavirus/country/us/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    df = pd.read_html(webpage)[0]


    # class Coronavirus():
    #     def _init_(self):
    #         self.driver = webdriver.Chrome()
    #
    #     def get_data(self):
    #         self.driver.get('https://www.worldometers.info/coronavirus/country/us/')

    #df = pd.read_html('https://www.worldometers.info/coronavirus/#countries')[0]

    hi =  df.loc[df['USAState'].isin(['Hawaii'])] #df.loc[df['TotalCases'] == 'USA']# df[['TotalCases'] == 'USA']
    hi = hi.fillna(0)

    total_cases = int(hi.iloc[0]['TotalCases'])
    new_cases = int(hi.iloc[0]['NewCases'])
    total_deaths = int(hi.iloc[0]['TotalDeaths'])
    new_deaths = int(hi.iloc[0]['NewDeaths'])


    # categories = []
    # categories.append(total_cases)
    # categories.append(new_cases)
    # categories.append(total_deaths)
    # categories.append(new_deaths)
    #
    # for x in categories:
    #     if math.isnan(x):
    #         print('hi')
    #         x = '0'
    #     print(categories)

    print(new_cases)
    # /html/body/div[4]/div[1]/div/div[5]/div[1]/div/table#usa_table_countries_today
    # document.querySelector("#main_table_countries_today")
    # #main_table_countries_today
    # /html/body/div[3]/div[3]/div/div[3]/div[1]/div/table
    send_mail(total_cases,new_cases,total_deaths, new_deaths)


def send_mail(total_cases, new_cases, total_deaths, new_deaths):

    body = 'Total cases: ' + str(total_cases) + '\
        \nNew cases: ' + str(new_cases) + '\
        \nTotal deaths: ' + str(total_deaths) + '\
        \nNew deaths: ' + str(new_deaths) + '\
        \nCheck the link: https://www.worldometers.info/coronavirus/country/us'


    FROM = 'pythonbotsarefun@gmail.com'
    TO = 'dvntaka@yahoo.com'
    SUBJECT = 'HI Coronavirus Stats for ' + str(date.today())
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, TO, SUBJECT, TEXT)


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pythonbotsarefun@gmail.com', 'aT@8J8f!')


    server.sendmail(
    FROM,
    TO,
    message
    )
    print('Hey Email has been sent!')
    server.close()

if __name__=="__main__":
    get_data()
    #schedule.every().day.at("13:46").do(get_data)
    #schedule.every(10).seconds.do(get_data)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)