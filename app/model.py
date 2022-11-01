import requests

BASE_URL = 'https://inova.coop.br/inovacoop-api'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
}

def sync_db():
    params = {
        'page': 0,
        'perPage': 20
    }
    data = requests.get(f'{BASE_URL}/posts',params=params, headers=HEADERS, verify=False)
    return(data)

