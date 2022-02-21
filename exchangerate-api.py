
import requests
from config import API_key
from pprint import pprint

# Where USD is the base currency you want to use
url = f'https://v6.exchangerate-api.com/v6/{API_key}/pair/USD/UZS'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object

# pprint(data.time_last_update_utc, data.base_code, data.target_code, data.conversion_rate)
print(f"exchange pair {data.get('base_code')} / {data.get('target_code')}\n"
      f"{data.get('time_last_update_utc')} updated\n"
      f"course is now {data.get('conversion_rate')}")

