import requests
import urllib.request
page = urllib.request.urlopen('https://www.verizon.com/content/vcg/services/error.model.json')
page = page.read().decode("utf-8") 
print(type(page))
page = page.count("errorId")
print(page)
