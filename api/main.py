from datetime import datetime

import requests
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
city = "Tashkent"
country = "Uzbekistan"
ROOT_URL = requests.get(f'http://api.aladhan.com/v1/calendarByCity/{year}/{month}?city={city}&country={country}&method=2')
# print(ROOT_URL.json())
print(day)
print(ROOT_URL.json()['data'][day-1]['date']['gregorian']['weekday']['en'])
print(ROOT_URL.json()['data'][1]['date']['readable'])
# print(ROOT_URL.json()['data'][0]['timings']['Dhuhr'])


