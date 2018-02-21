from math import sin, cos, sqrt, atan2, radians
import gmplot

# gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40000, marker=False) # circles

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

def getNearbyAdresses(distances, lats, longs, distance_km):
	n = len(distances)
	latitudes = []
	longitudes = []
	for i in range(n):
		for j in range(n):
			if j > i and distances[i][j] < distance_km:
				latitudes.append(lats[i])
				latitudes.append(lats[j])
				longitudes.append(longs[i])
				longitudes.append(longs[j])
	return latitudes, longitudes

def markLineBetweenNearbyAdresses(gmap, distances, lats, longs, distance_km):
	latitudes, longitudes = getNearbyAdresses(distances=distances, lats=lats, longs=longs, distance_km=distance_km)
	gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=5) # line between corners

def plotMarkers(gmap, lats, longs):
	for i in range(len(lats)):
		gmap.marker(lats[i], longs[i], title="Pessoa "+str(i+1))

def buildMapWithConditionalMarkers(map_name, lats, longs, distance_km): 
	gmap = gmplot.GoogleMapPlotter(-23.5515, -51.4614, 10) # TODO definir zoom, latitude e longitude automaticamente
	distances = getAllDistances(lats, longs)
	gmap.heatmap(lats, longs)
	plotMarkers(gmap, lats, longs)
	markLineBetweenNearbyAdresses(gmap, distances, lats, longs, distance_km)
	gmap.draw(map_name+".html")
	return gmap, distances 