# Reminder i18n is replaced with maps.world
from pygal.maps.world import COUNTRIES

'''
Define a function with the parameter as country_name then loop COUNTRIES
storing the two-digit code in the variable code and the name of the
country in the name variable(key-pair value.) If the name variable is 
equal to the country_name parameter the two-digit code is printed to
screen and if not None is returned(return None is the same as else:None)
'''

def get_country_code(country_name):
	'''Return the Pygal two-digit country code for the given country.'''
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	# If the country wasn't found, return None.
	return None
	
print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))
