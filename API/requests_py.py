import requests
response = requests.get('https://codingninjas.in/api/v3/courses')
print(response.status_code)
print(response.encoding)
# print(response.text)
print(response.url)
print(response.headers)
print(response.headers['Date'])
print(response.headers['Server'])

