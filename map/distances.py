from math import sin, cos, sqrt, atan2, radians
import gmplot

# Apucarana: -23.5515, -51.4614
# Maringa: -23.4209995,-51.9330558

# gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40000, marker=False) # circles
# gmap.scatter(marker_lats, marker_lngs, 'k', marker=True) # corner markers

def printDistancesMatrix(distances):
	for k in range(len(distances)):
		print(distances[k])

def distance(coord1, coord2):
	R = 6373.0
	lat1 = radians(coord1[0])
	lon1 = radians(coord1[1])
	lat2 = radians(coord2[0])
	lon2 = radians(coord2[1])
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
	c = 2 * atan2(sqrt(a), sqrt(1-a))
	distance = R * c
	return distance

def getAllDistances(lats, longs):
	distances = [[0 for i in range(len(lats))] for i in range(len(lats))]
	for i in range(0, len(lats)-1):
		for j in range(len(lats)-1, i, -1):
			d = distance([lats[i], longs[i]], [lats[j], longs[j]])
			distances[i][j] = d
	return distances

def getNearbyAdresses(distances, lats, longs):
	latitudes = []
	longitudes = []
	for i in range(len(distances)):
		for j in range(len(distances)):
			if j > i:
				if distances[i][j] < 50:
					latitudes.append(lats[i])
					latitudes.append(lats[j])
					longitudes.append(longs[i])
					longitudes.append(longs[j])
	return latitudes, longitudes

def markLineBetweenNearbyAdresses(distances, lats, longs):
	latitudes, longitudes = getNearbyAdresses(distances=distances, lats=lats, longs=longs)
	gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=5) # line between corners

def plotMarkers(lats, longs):
	for i in range(len(lats)):
		gmap.marker(lats[i], longs[i], title="Pessoa "+str(i+1))

lats = [-23.5515, -23.4209995, -23.3209995, -23.65515]
longs = [-51.4614, -51.9330558, -51.3614, -51.59330558]

distances = [[0 for i in range(len(lats))] for i in range(len(lats))]
distances = getAllDistances(lats, longs)

gmap = gmplot.GoogleMapPlotter(-23.5515, -51.4614, 10)
gmap.heatmap(lats, longs)
plotMarkers(lats, longs)
markLineBetweenNearbyAdresses(distances, lats, longs)
gmap.draw("mymap.html")

printDistancesMatrix(distances)