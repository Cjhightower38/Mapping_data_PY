# Importing json module to with with the info from the file.
import json

from country_codes import get_country_code

'''
Store the downloaded json file in a variable. Open and rename the file
as (f) then create a different variable to store the file using the 
json.load(). Now itterate through each iteam in the variable or json 
list inside a dictonary and if the key is equal to 2010 the name and 
population are printed to screen. Next covert the srings into numerical
values by using the int() and the srt().
'''
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
	
#Because some populations have decimal values by converting the string
#pop_dict['Value'] into a float and then a integer will correct the 
#ValueError.
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))

# The get_country_code() is store in the variable code and printed to
# screen if the two-digit code is found the code is returned if not the 
# Error message is printed to screen.		
		code = get_country_code(country_name)
		if code:
			print(code + ': '+ str(population))
		else:
			print('ERROR - ' + country_name)
	
