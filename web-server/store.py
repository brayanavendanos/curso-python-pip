import requests as rqst

def get_categories():
    r = rqst.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])
    
