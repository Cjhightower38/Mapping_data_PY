# Importing json module to with with the info from the file.
import json

import pygal

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

'''	
Because some populations have decimal values by converting the string
pop_dict['Value'] into a float and then a integer will correct the 
ValueError. Added a empty dictionary to country codes(cc) and population
in a format Pygal expects. The get_country_code() is store in the 
variable code and printed to screen if the two-digit code is found the 
code is returned if not the Error message is printed to screen. Used 
country codes as a dictionary with code as the key and populations for 
the value and commented-out the print statement. Also added a title and 
passed the add() cc_populations dictionary which contains the country 
codes and population values.
'''

cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))	
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = population	
#			print(code + ': '+ str(population))
#		else:
#			print('ERROR - ' + country_name)

'''
Group the countries into 3 population levels by creating three empty
dictionaries and the store each item in cc_populations into a key-value
pair cc is the key and pop is the value(pay close attention to how line
two should read.) Add if-elif-else to add the each country to it's
correct dictionary. Print the len of each list and use wm.add() to add
each group to the map.
'''
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop <1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop
		
# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

			
wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'
wm.add('0-10', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
	
