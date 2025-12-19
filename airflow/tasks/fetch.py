import requests

def fetch_data(url):
    
    try:
        response = requests.get(url)
    except:
        return
    
    if response.status_code != 200:
        print("Error! Could not load data from the API")
        return 

    data = response.json()
    return data