import requests
import json
from visualAPIException import VisualAPIException

class VisualAPI:

	def __init__(self,api_key,mode='live',api_version='v1'):
		
		self.base_uri='https://api.turingiq.com/'
		if not api_key:
			raise VisualAPIException('API key is not provided.')
		else:
			self.api_key = api_key
			authorization = "Bearer "+self.api_key
			self.headers = {"Authorization":authorization}

		if mode is 'live' or mode is 'sandbox':
			self.mode = mode
		else:
			raise VisualAPIException('mode can only be either \'live\' or \'sandbox\'. You provided: '+mode)			

		if api_version is not 'v1':
			raise VisualAPIException('Currenly only \'v1\' is supported for api_version')
		else:
			self.api_version = api_version


	def search(self,image_url,filters={},crop_box=[]):
		if(self.mode == 'live'):
			path = '/similar/search'
		else:
			path = '/demo-similar/search'

		crop = None
		if(crop_box):
			crop = ','.join(str(element) for element in self.crop_box)
		data = {"url":image_url,
				"crop": crop,
				'filter1':filters['filter1'] if 'filter1' in filters else None,
				'filter2':filters['filter2'] if 'filter2' in filters else None,
				'filter3':filters['filter3'] if 'filter3' in filters else None,
				}
		try:
			response = requests.post(self.base_uri+self.api_version+path,data=data,headers=self.headers)
			
			response = json.loads(response.text)
			if 'error' in response:
				# return (response['error'])
				raise VisualAPIException(response['error'])
			else:
				return response
		except Exception as e:
			print(e)

