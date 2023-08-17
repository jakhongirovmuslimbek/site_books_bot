import requests
import config

url = config.MYURL

headers = {
    'Authorization': f'token {config.MYTOKEN}'
}

def get_categories():
    http = f"{url}category_all/"
    categories = requests.get(http, headers=headers)
    return categories.json()


def user_create(telegram_id):
    http = f"{url}user_create/"
    users = requests.post(http, data={
        "telegram_id": telegram_id
    }, headers=headers)
    if users.status_code == 201:
        return True
    else: 
        return False


def get_by_category_id(id):
    http = f"{url}by_category_id/{id}/"
    r = requests.get(http, headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        return []    


def get_book(id):
    http = f"{url}book_id/{id}/" 
    r = requests.get(http, headers=headers)
    return r.json()
