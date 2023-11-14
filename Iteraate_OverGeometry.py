from osgeo import ogr

wkt = "MULTIPOINT (1181866.263593049 615654.4222507705, 1205917.1207499576 623979.7189589312, 1227192.8790041457 643405.4112779726, 1224880.2965852122 665143.6860159477)"
geom = ogr.CreateGeometryFromWkt(wkt)
for i in range(0, geom.GetGeometryCount()):
    g = geom.GetGeometryRef(i)
    print ("%i). %s" %(i, g.ExportToWkt()))