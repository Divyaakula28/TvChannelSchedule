from django.shortcuts import render
from django.http import HttpResponse
import requests
import numpy as np
import json


# Create your views here.
def loc(req):
	if req.method=='POST':
		channel=req.POST['select']
		url = "https://indian-tv-schedule.p.rapidapi.com/TodaySchedule"
		querystring = {"channel":channel}
		headers = {
   			'x-rapidapi-host': "indian-tv-schedule.p.rapidapi.com",
   			'x-rapidapi-key': "6966652bc2msh4a15d38b3376026p16047ejsnb10766d15552"
   			}
		response = requests.request("GET", url, headers=headers, params=querystring)
		k1=response.text
		k2 = json.loads(k1)
		length=len(k2)
		time=list(k2.keys())
		r=[]
		s=[]
		for i in range(len(time)):
			o=time[i]
			j=o[0]+o[1]
			k=o[3]+o[4]
			r.append(j)
			s.append(k)
		hr= [int(i) for i in r]
		mn= [int(i) for i in s]
	
		new_d = {}
		for sub in k2.values():
			for key, value in sub.items():
				new_d.setdefault(key, []).append(value)
		programs=list(new_d.values())[0]
		typep=list(new_d.values())[2]
		diss=list(new_d.values())[1]
		return render(req,'search3.html',{'time':time,'programs':programs,'diss':diss,'type':typep,'hr':hr,'mn':mn})
	return render(req,'drop.html')


def drop(req):
	if req. method=='POST':
		name=req.POST['lang']
		url = "https://indian-tv-schedule.p.rapidapi.com/searchChannel"
		querystring = {"lang":name}
		headers = {
    'x-rapidapi-host': "indian-tv-schedule.p.rapidapi.com",
    'x-rapidapi-key': "8b3ed7e76cmsh2ce38fcd37b82b4p1164d2jsn6fa39b33ac0b"
    }
		response = requests.request("GET", url, headers=headers, params=querystring)
		x=response.text
		x=x.replace('[','')
		x=x.replace(']','')
		x=x.replace('"','')	
		x=(x.split(","))
		x.sort()
		return render(req,'search1.html',{'x':x}) 		
	return render(req, 'search0.html')
	
	
def home(req):
	return render(req,'all.html')
	
def nav(req):
	return render(req,'h1.html')
	
def dis(req):
	return render(req,'discriptive.html')

def test(req):
	return render(req,"h1.html")	



	

	