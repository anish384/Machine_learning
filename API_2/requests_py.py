import requests
from requests.auth import HTTPBasicAuth

a = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('nidhi@codingninjas.in','cnninjas123'))
print(a.status_code)
