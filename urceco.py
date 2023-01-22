import requests

def send_document(path):
    url = 'https://so.urceco.de/upload/' 
    data = {
        "Accept": "application/json",
        "Linx-Randomize": "yes",
        'Linx-Expiry': '604800'
    }
    file = open(path, 'rb').read()
    response = requests.put(url, headers=data, data=file).json()['url']
    print(response)
    return response
