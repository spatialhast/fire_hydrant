#!/usr/bin/python
# -*- coding: utf-8 -*-

# pip install pygeoj

import pygeoj


inputFileName = 'export.geojson'
outputFileName = 'UA-63-1-7'

inputFile = pygeoj.load(inputFileName)
f = open(outputFileName + '.kml','w')

f.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
f.write('<kml xmlns="http://earth.google.com/kml/2.2">' + '\n')
f.write('<Document>' + '\n')


f.write('  <Style id="placemark-blue">' + '\n')
f.write('    <IconStyle>' + '\n')
f.write('      <Icon>' + '\n')
f.write('        <href>http://mapswith.me/placemarks/placemark-blue.png</href>' + '\n')
f.write('      </Icon>' + '\n')
f.write('    </IconStyle>' + '\n')
f.write('  </Style>' + '\n')
f.write('  <Style id="placemark-brown">' + '\n')
f.write('    <IconStyle>' + '\n')
f.write('      <Icon>' + '\n')
f.write('        <href>http://mapswith.me/placemarks/placemark-brown.png</href>' + '\n')
f.write('      </Icon>' + '\n')
f.write('    </IconStyle>' + '\n')
f.write('  </Style>' + '\n')
f.write('  <Style id="placemark-green">' + '\n')
f.write('    <IconStyle>' + '\n')
f.write('      <Icon>' + '\n')
f.write('        <href>http://mapswith.me/placemarks/placemark-green.png</href>' + '\n')
f.write('      </Icon>' + '\n')
f.write('    </IconStyle>' + '\n')
f.write('  </Style>' + '\n')
f.write('  <Style id="placemark-orange">' + '\n')
f.write('    <IconStyle>' + '\n')
f.write('      <Icon>' + '\n')
f.write('        <href>http://mapswith.me/placemarks/placemark-orange.png</href>' + '\n')
f.write('      </Icon>' + '\n')
f.write('    </IconStyle>' + '\n')
f.write('  </Style>' + '\n')
f.write('  <Style id="placemark-pink">' + '\n')
f.write('    <IconStyle>' + '\n')
f.write('      <Icon>' + '\n')
f.write('        <href>http://mapswith.me/placemarks/placemark-pink.png</href>' + '\n')
f.write('      </Icon>' + '\n')
f.write('    </IconStyle>' + '\n')
f.write('  </Style>' + '\n')
f.write('  <Style id="placemark-purple">' + '\n')
f.write('    <IconStyle>' + '\n')
f.write('      <Icon>' + '\n')
f.write('        <href>http://mapswith.me/placemarks/placemark-purple.png</href>' + '\n')
f.write('      </Icon>' + '\n')
f.write('    </IconStyle>' + '\n')
f.write('  </Style>' + '\n')
f.write('  <Style id="placemark-red">' + '\n')
f.write('    <IconStyle>' + '\n')
f.write('      <Icon>' + '\n')
f.write('        <href>http://mapswith.me/placemarks/placemark-red.png</href>' + '\n')
f.write('      </Icon>' + '\n')
f.write('    </IconStyle>' + '\n')
f.write('  </Style>' + '\n')
f.write('  <Style id="placemark-yellow">' + '\n')
f.write('    <IconStyle>' + '\n')
f.write('      <Icon>' + '\n')
f.write('        <href>http://mapswith.me/placemarks/placemark-yellow.png</href>' + '\n')
f.write('      </Icon>' + '\n')
f.write('    </IconStyle>' + '\n')
f.write('  </Style>' + '\n')


f.write('  <name>' + outputFileName + '</name>' + '\n')
f.write('  <visibility>1</visibility>' + '\n')

i = 0

for feature in inputFile:
	if feature.properties['fire_operator'].encode('utf-8') == outputFileName:
		i = i + 1
		
		lat = str(feature.geometry.coordinates[1])
		lng = str(feature.geometry.coordinates[0])
		name = feature.properties['fire_hydrant:diameter'].encode('utf-8')
		
		note = feature.properties['note'].encode('utf-8')
		street = feature.properties['fire_hydrant:street'].encode('utf-8')
		housenumber = feature.properties['fire_hydrant:housenumber'].encode('utf-8')
		
		if 'fire_hydrant:pressure' in feature.properties:
			pressure = feature.properties['fire_hydrant:pressure'].encode('utf-8')
		else:
			pressure = '-'

		description = note + ' | ' + pressure + ' | ' + street + ', ' + housenumber
		
		#К-75	#placemark-red
		#К-100	#placemark-blue
		#К-125	#placemark-purple
		#К-150	#placemark-yellow
		#К-200	#placemark-pink
		#К-250	#placemark-brown
		#К-300	#placemark-green
		#К-400	#placemark-orange

		#Т-75	#placemark-red
		#Т-100	#placemark-blue
		#Т-125	#placemark-purple
		#Т-150	#placemark-yellow
		#Т-200	#placemark-pink
		#Т-250	#placemark-brown
		#Т-300	#placemark-green
		#Т-400	#placemark-orange

		if name == 'К-75' or name == 'Т-75':
			style = '#placemark-red'
		elif name == 'К-100' or name == 'Т-100':
			style = '#placemark-blue'	
		elif name == 'К-125' or name == 'Т-125':
			style = '#placemark-purple'
		elif name == 'К-150' or name == 'Т-150':
			style = '#placemark-yellow'
		elif name == 'К-200' or name == 'Т-200':
			style = '#placemark-pink'
		elif name == 'К-250' or name == 'Т-250':
			style = '#placemark-brown'
		elif name == 'К-300' or name == 'Т-300':
			style = '#placemark-green'
		elif name == 'К-400' or name == 'Т-400':
			style = '#placemark-orange'
		else:
			style = '#placemark-hotel'
			
		f.write('  <Placemark>' + '\n')
		f.write('    <name>' + name + '</name>' + '\n')
		f.write('    <description>' + description + '</description>' + '\n')
		f.write('    <styleUrl>' + style + '</styleUrl>' + '\n')
		f.write('    <Point><coordinates>' + lng + ',' + lat + '</coordinates></Point>' + '\n')
		f.write('  </Placemark>' + '\n')

	
f.write('</Document>' + '\n')
f.write('</kml>' + '\n')

f.close()

print 'total count: ' + str(i)










































