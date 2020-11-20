import os


# URL_HERE = "https://revgeocode.search.hereapi.com/v1/revgeocode"
# API_KEY_HERE = 'DTefltZHcbSfUzgnavsqWrZbsPZgEJ3EFHyz-EDcqBc'
# API_IP_TOKEN = "0b334fd91614f7"

URL_HERE = os.environ.get("URL_HERE")
API_KEY_HERE = os.environ.get("API_KEY_HERE")
API_IP_TOKEN = os.getenv("API_IP_TOKEN")
