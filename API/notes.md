# API
---
## Why we need API?
---
- We need only a chunk of huge dataset
- Data is very dynamic i.e it changes very frequently
    - Example - weather conditions (this changes frequently)
---
## We can access api through some websites only
---
# Examples of APIs
---
1. google maps api -> uber using this api
2. facebook
3. weather apis
4. youtube apis
5. twitter apis

---
# Elements of an API
---
- Access
- Request
    - Methods
    - parameters
- Response
---

# HTTPS
---
- in order to get api, we need to make a request call to retrieve data from any website 
- **url is reference to a specific web page** 
- HTTPS - (Hyper text transfer protocol)
---
# Methods of HTTPS
---
1) GET -> read method
2) POST -> write method
---

# HTTPS Libraries
---
these are in python

1) httplib
2) urllib
3) requests
---
# Requests
---
```py 
import requests
response = requests.get('https://codingninjas.in/api/v3/courses')
print(response.status_code)
print(response.encoding)
# print(response.text)
print(response.url)
print(response.headers)
print(response.headers['Date'])
print(response.headers['Server'])

```
---
# Response Object Attributes
---
- Status code
    - 200 - successful (any answer starts with 2xx is successful)
    - 404 - fail (any answer starts with 4xx is fail)
- encoding
    - utf-8 like this 
- url
- text
- headers

