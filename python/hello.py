import urllib.request
response = urllib.request.urlopen('https://python.org')
print(response.read().decode('utf-8'))
