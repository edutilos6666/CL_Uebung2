import requests

url = "http://www.discoversdk.com/blog/10-interesting-python-modules-to-learn-in-2016"
r = requests.get(url)
print("status code = " , r.status_code)
print("encoding = ", r.encoding)
print("headers = ", r.headers)
