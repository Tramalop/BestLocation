import requests as rq # take files from urls
import json # read Json files

url_pap  = "https://www.pap.fr/annonce/locations-nice-06"
response = rq.get(url_pap)  
print(response)