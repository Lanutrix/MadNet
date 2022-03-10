import requests


def get_info_by_ip():
    try:
        ip = requests.get("http://jsonip.com/").json()
        response = requests.get(url=f'http://ip-api.com/json/{ip["ip"]}').json()
        # print(response)
        
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        pl=""
        for k, v in data.items():
            pl+=f'{k} : {v}\n'
        return pl
        
    except requests.exceptions.ConnectionError:
        return '[!] Please check your connection!'
        
