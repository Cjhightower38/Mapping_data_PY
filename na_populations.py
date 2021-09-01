import pygal

'''
Import Pygal, set wm as the variable that holds pygal.m.w.W()(remember
pygal.Worldmap()has been replaced with the below method,) add a title 
for the map, used the add() passed a dictonary which contains Pygal
two-digit country code as the keys and population as it's values, 
finally render the file to an .svg file.
'''

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca' : 34126000, 'us' : 309349000, 'mx':
	11342300})
	
wm.render_to_file('na_populations.svg')


