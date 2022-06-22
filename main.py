from bs4 import BeautifulSoup
import requests as rq 
from datetime import datetime
import os
from tabulate import tabulate
import numpy as np

response = rq.get('https://www.time.ir/')
resp = response.text

soap = BeautifulSoup(resp, 'html.parser')

date_foramt = 1
dates = ['jalali', 'miladi small', 'qamari small']

while True:
    inp = input('>> ')
    inp = inp.strip()

    if inp == 'date':
        div = soap.find_all('span', class_ = 'show date')
        date= div[date_foramt - 1].text
        print(date)
        continue
    
    elif inp == 'date numeric':
        div = soap.find_all('span', class_ = 'show numeral')
        date= div[date_foramt - 1].text
        print(date)
        continue

    elif inp == 'time':
        print(datetime.now().strftime('%H:%M:%S'))
        continue

    elif inp == 'exit':
        break
    
    elif 'date format' in inp:
        if int(inp.split(' ')[-1]) % 3 == 0 and int(inp.split(' ')[-1]) != 0:
            date_foramt = 3
            print('date foramt changed to:', date_foramt)
            continue

        elif int(inp.split(' ')[-1]) != 0:
            date_foramt = int(inp.split(' ')[-1]) % 3
            print('date foramt changed to:', date_foramt)
            continue

        else:
            print('Invalid date format')
            continue
    
    elif inp == 'help':
        print('date - show date')
        print('date numeric - show date in numeric form')
        print('time - show time')
        print('exit - exit program')
        print('date format [number] - change date format|\n\t\t\t\t\t | - 1 : jalali\n\t\t\t\t\t | - 2 : miladi\n\t\t\t\t\t | - 3 : qamari')
        print('help - show help')
        print('clear - clear screen')
        print('ping - ping server')
        print('full status - show full status')
        print('calendar - show calendar')
        continue
    
    elif inp == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    
    elif inp == 'ping':
        print('Pong')
        continue
    
    elif inp == 'full status':
        div = soap.find_all('span', class_ = 'show date')
        date= div[date_foramt - 1].text
        print('date:', date)
        div = soap.find_all('span', class_ = 'show numeral')
        date= div[date_foramt - 1].text
        print('date numeric:', date)
        print('time:', datetime.now().strftime('%H:%M:%S'))
        print('date format:', date_foramt)
        continue

    elif inp == 'calendar':
        div = soap.find_all('div', class_ = 'dayHeader')
        days_header = []
        for i in div:
            days_header.append(i.text)
        
        div = soap.find_all('div', class_ = 'dayList')
        days = []
        for i in div:
            dyna = i.find_all('div', class_ = f'{dates[date_foramt - 1]}')
            for j in dyna:
                days.append(j.text)


        final_days_header = []
        for i in days_header[0]:
            if i != '\n':
                final_days_header.append(i)

        # print('\n')

        # for counter, i in enumerate(days):
        #     print(i, end = ' | ')
        #     if counter % 7 == 0 and counter != 0:
        #         print('\n')

        # print('\n')
        
        days = np.reshape(days, (-1, 7))
        
        print(tabulate(days, final_days_header, tablefmt = 'fancy_grid'))

    elif inp == 'what is this':
        print('This is a simple program that shows date and time in different formats.')
        print('You can change date format by typing "date format [number]"')
        print('made with python3 In partnership with Copilot :)')

    else:
        print('Invalid command')

# Telegram: @iliyaFaramarzi
# instagram: faramarziiliya
# github: iliyaFaramarzi