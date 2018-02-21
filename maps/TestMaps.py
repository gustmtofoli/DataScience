import Maps

distance_km = 50
lats = [-23.5515, -23.4209995, -23.3209995, -23.65515]
longs = [-51.4614, -51.9330558, -51.3614, -51.59330558]

gmap, distances = Maps.buildMapWithConditionalMarkers(map_name="testMap", lats=lats, longs=longs, distance_km=distance_km)

Maps.printDistancesMatrix(distances=distances)