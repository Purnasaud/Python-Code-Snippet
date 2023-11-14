from osgeo import ogr

wkt = "LINESTRING (1181866.263593049 615654.4222507705, 1205917.1207499576 623979.7189589312, 1227192.8790041457 643405.4112779726, 1224880.2965852122 665143.6860159477)"
geom = ogr.CreateGeometryFromWkt(wkt)
# Get Envelope returns a tuple (minX, maxX, minY, maxY)
env = geom.GetEnvelope()
print(env)
print ("minX: %d, minY: %d, maxX: %d, maxY: %d" %(env[0],env[2],env[1],env[3]))


#print "in X: ",env1[0], "Max X: ", env1[1], "Min Y: ", env1[2], "Max Y:", poly[3])
 