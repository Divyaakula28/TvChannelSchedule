import requests
from .views import*

n=views.get["name"]
print(n)
	url = "https://indian-tv-schedule.p.rapidapi.com/searchChannel"
	querystring = {"lang":"Telugu"}
	headers = {
    'x-rapidapi-host': "indian-tv-schedule.p.rapidapi.com",
    'x-rapidapi-key': "8b3ed7e76cmsh2ce38fcd37b82b4p1164d2jsn6fa39b33ac0b"
    }
	response = requests.request("GET", url, 	headers=headers, params=querystring)
	print(response.text)


###########
url = "https://indian-tv-schedule.p.rapidapi.com/Schedule"	
	querystring = {"channel":"Zee TV HD"}	
	headers = {
	    'x-rapidapi-host': "indian-tv-schedule.p.rapidapi.com",
	    'x-rapidapi-key': "8b3ed7e76cmsh2ce38fcd37b82b4p1164d2jsn6fa39b33ac0b"
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)	
	x=response.text