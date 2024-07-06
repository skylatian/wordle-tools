''' simple example script to get initial data from the API given a puzzle ID'''

from pprint import pprint
import requests

from config import cookie as imported_cookie

# initial credit to https://www.reddit.com/r/crossword/comments/14h59a2/comment/kgeawqb/
# (https://github.com/sinakhalili/sinakhalili.com)

COOKIE = imported_cookie

ID = 1791 # puzzle ID (not consecutive, but unique)

ENDPOINT = f"https://www.nytimes.com/svc/games/state/wordleV2/latests?puzzle_ids={ID}"

headers = {
    'Cookie': f'NYT-S=${COOKIE}'
}

response = requests.get(
    ENDPOINT,
    headers=headers,
    timeout=10
).json()

pprint(response['states'])