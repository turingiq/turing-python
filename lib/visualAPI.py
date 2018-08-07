import requests
import json
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.turingAPIException import TuringAPIException

class VisualAPI:

	def __init__(self,api_key,mode='live',api_version='v1'):
				
		if not api_key:
			raise TuringAPIException('API key is not provided.')
		else:
			self.api_key = api_key
			authorization = "Bearer "+self.api_key
			self.headers = {"Authorization":authorization}

		if mode is 'live' or mode is 'sandbox':
			self.mode = mode
		else:
			raise TuringAPIException('mode can only be either \'live\' or \'sandbox\'. You provided: '+mode)			

		if api_version is not 'v1':
			raise TuringAPIException('Currenly only \'v1\' is supported for api_version')
		else:
			self.api_version = api_version

		self.base_uri='https://api.turingiq.com/'+self.api_version


	def autocrop(self,image_url):
		end_point = self.base_uri+'/autocrop'
		data = {"url":image_url}

		try:
			response = requests.post(end_point,headers=self.headers,data=data)
			if response.status_code==200 or (response.status_code>=400 and response.status_code<500):
				response = json.loads(response.text)
			return response
		except Exception as e:
			print(e)


	def search(self,image_url,filters={},crop_box=[]):
		if(self.mode == 'live'):
			path = '/similar/search'
		else:
			path = '/demo-similar/search'

		end_point = self.base_uri+path
		crop = None
		if(crop_box):
			crop = ','.join(str(element) for element in crop_box)
		data = {"url":image_url,
				"crop": crop,
				'filter1':filters['filter1'] if 'filter1' in filters else None,
				'filter2':filters['filter2'] if 'filter2' in filters else None,
				'filter3':filters['filter3'] if 'filter3' in filters else None,
				}
		try:
			response = requests.post(end_point,headers=self.headers,data=data)
			if response.status_code==200 or (response.status_code>=400 and response.status_code<500):
				response = json.loads(response.text)	
			return response
		except Exception as e:
			print(e)


	def recommendations(self,id,filters={}):
		if(self.mode == 'live'):
			path = '/similar/'+str(id)
		else:
			path = '/demo-similar/'+str(id)

		end_point = self.base_uri+path
		params = {
				'filter1':filters['filter1'] if 'filter1' in filters else None,
				'filter2':filters['filter2'] if 'filter2' in filters else None,
				'filter3':filters['filter3'] if 'filter3' in filters else None,
				}
		try:
			response = requests.get(end_point,headers=self.headers,params=params)
			if response.status_code==200 or (response.status_code>=400 and response.status_code<500):
				response = json.loads(response.text)
			return response
		except Exception as e:
			print(e)


	def insert(self,id,image_url,filters={},metadata={}):
		if(self.mode == 'live'):
			path = '/similar/create'
		else:
			path = '/demo-similar/create'

		end_point = self.base_uri+path
		data = {'id':id,
				'url':image_url,
				'filter1':filters['filter1'] if 'filter1' in filters else None,
				'filter2':filters['filter2'] if 'filter2' in filters else None,
				'filter3':filters['filter3'] if 'filter3' in filters else None,
				}
		for key in metadata:
			data[key] = metadata[key]
		try:
			response = requests.post(end_point,headers=self.headers,data=data)
			if response.status_code==200 or (response.status_code>=400 and response.status_code<500):
				response = json.loads(response.text)
			return response
		except Exception as e:
			print(e)

	def update(self,image_url=None,filters={},metadata={}):
		return self.insert(image_url,filters,metadata)


	def delete(self,id):
		if(self.mode == 'live'):
			path = '/similar/'+str(id)
		else:
			path = '/demo-similar/'+str(id)

		end_point = self.base_uri+path
		try:
			response = requests.delete(end_point,headers=self.headers)
			if response.status_code==200 or (response.status_code>=400 and response.status_code<500):	
				response = json.loads(response.text)
			return response
		except Exception as e:
			print(e)