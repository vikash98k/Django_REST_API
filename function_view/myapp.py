import requests
import json

URL = "http://127.0.0.1:8000/stuinfo/"

def get_data(id=None):
	data={}
	if id is not None:
		data={'id':id}
	json_data=json.dumps(data)
	headers = {"content-Type":'application/json'}
	r =requests.get(url=URL,data=json_data,headers=headers)
	data = r.json()
	print(data)
#get_data()

def post_data():
	data={
	'name':'maya',
	'roll':45,
	'city':'kota'
	}
	headers = {"content-Type":'application/json'}
	json_data=json.dumps(data)
	r =requests.post(url=URL, headers=headers,data=json_data)
	data = r.json()
	print(data)
post_data()
def update_data():
	data={
	'id':3,
	'name':'Rohit',
	'city':'churu'
	}
	json_data=json.dumps(data)
	headers = {"content-Type":'application/json'}
	r =requests.put(url=URL,data=json_data,headers=headers)
	data = r.json()
	print(data)
#update_data()
def delete_data():
	data={
	'id':4
	}
	json_data=json.dumps(data)
	headers = {"content-Type":'application/json'}
	r =requests.delete(url=URL,data=json_data,headers=headers)
	data = r.json()
	print(data)
#delete_data()