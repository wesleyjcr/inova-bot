import requests

from model import count_all_documents, insert_documents

BASE_URL = 'https://inova.coop.br/inovacoop-api'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
}
PARAMS = {
    'page': 0,
    'perPage': 10
}


def prepare_to_insert(page, diff):    
    data = requests.get(f'{BASE_URL}/{page}',params={'page': 0, 'perPage': diff}, headers=HEADERS, verify=False).json()
    for document in data['items']:
        data = {
            'id': document['id'],
            'path': f"{BASE_URL}/{page}/{document['path']}",
            'image': f"https:{document['image']['url']}",
            'title': document['title'],
            'description': document['description'],
            'sent': False
        }
        insert_documents(page, data)

def sync_db():
    elements = ['courses', 'innovation-practices', 'posts', 'innovation-radars']
    for page in elements:
        data = requests.get(f'{BASE_URL}/{page}',params={'page': 0, 'perPage': 1}, headers=HEADERS, verify=False)
        total_items = data.json()['totalItemsAllPages']
        total_items_database = count_all_documents(page)
        if total_items != total_items_database:
            diff = total_items - total_items_database
            prepare_to_insert(page,diff)
            

    

