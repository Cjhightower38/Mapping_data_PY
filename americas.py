import pygal

# wm = pygal.Worldmap() has been replaced with down below pg.m.w.W()
'''
Store pygal.m.w.World() in the wm variable, add a tiltle for the map,
use wm.add() to label and separately color code each America, and render
to americas.svg for veiwing.
'''

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])
    
wm.render_to_file('americas.svg')

