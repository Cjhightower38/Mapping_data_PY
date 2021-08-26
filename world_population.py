# Importing json module to with with the info from the file.
import json

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
	
#Print the 2010 population for each country.
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(pop_dict['Value'])
		print(country_name + ': ' + str(population))
	
