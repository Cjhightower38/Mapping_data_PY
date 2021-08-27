'''
In pygal 20.0.0 pygal.i18n was replaced by pygal.maps.world. After
importing with maps.world() and using sorted() to sort through the keys
both the countries two digit code and corresponding country name.
'''

#from pygal.i18n import COUNTRIES

#for country_code in sorted(COUNTRIES.keys()):
#	print(country_code, COUNTRIES[country_code])

from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()): 
	print(country_code, COUNTRIES[country_code])
	
