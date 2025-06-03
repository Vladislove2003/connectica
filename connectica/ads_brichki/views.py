import requests

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from rest_framework.parsers import JSONParser

from .serializers import AdSerializer


class UsersAdsView(TemplateView):
	template_name = 'ads_brichki/base.html'
	extra_context = {
		'users': None,
		'ads': None,
	}


	url_users = 'http://127.0.0.1:8000/users/api/users/?format=json'
	response = requests.get(url_users)
	if response.status_code == 200:
		extra_context['users'] = response.json()
		

	def post(self, request, *args, **kwargs):
		self.extra_context['ads'] = []

		url_ads = f'http://127.0.0.1:8000/api/ads/'\
				  f'?format=json&pk={request.POST['user_id']}'
		response = requests.get(url_ads)

		if response.status_code == 200:
			response = response.json()

			for data in response:
				ad_data = {
					"brand": data['brand']['name'], 
					"model": data['model']['name'], 
					"generation": data['generation']['name'], 
					"engine_type": data['engine_type']['name'], 
					"boost_type": data['boost_type']['name'], 
					"drive": data['drive']['name'],
					"body":data['body']['name'], 
					"mileage":data['mileage'], 
					"price":data['price'],
					}
				serializer = AdSerializer(data=ad_data)
				if serializer.is_valid():
					ad = serializer.create(ad_data)
					self.extra_context['ads'].append(ad)

		return render(request, 'ads_brichki/base.html', 
			context=self.extra_context)