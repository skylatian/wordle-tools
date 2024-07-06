from pycookiecheat import BrowserType, chrome_cookies
import requests
from pprint import pprint

# https://github.com/n8henrie/pycookiecheat

url = 'https://www.nytimes.com/games/wordle/index.html'

#browsers = ['BRAVE', 'CHROME', 'CHROMIUM', 'FIREFOX', 'SLACK']

#print("1: BRAVE, 2: CHROME, 3: CHROMIUM, 4: FIREFOX, 5: SLACK")

#input_browser = int(input("Enter the browser number (or press enter for default, Chrome): ") or '2')

#browser = (browsers[input_browser - 1])
#print(browser)

# Uses Chrome's default cookies filepath by default
cookies = chrome_cookies(url)

r = requests.get(url, cookies=cookies)
cookie = cookies['NYT-S']
# Using an alternate browser

#cookie = chrome_cookies(url, browser=BrowserType.CHROME)['NYT-S']

pprint(cookie)