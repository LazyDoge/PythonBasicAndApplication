from pprint import pprint

import requests

get = requests.get("http://8.8.8.8")

pprint(get.text)
