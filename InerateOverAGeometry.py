from osgeo import ogr

geomcol = "GEOMETRYCOLLECTION (POINT (-122.23 47.09 0),LINESTRING (-122.6 47.14 0,-122.48 47.23 0))"

geom = ogr.CreateGeometryFromWkt(geomcol)
no = geom.GetGeometryCount()
for i in range(0, no):
    ref = geom.GetGeometryRef(i)
    #print(ref)
    print(i , ref.ExportToWkt())
    


wkt = "MULTIPOINT (1181866.263593049 615654.4222507705, 1205917.1207499576 623979.7189589312, 1227192.8790041457 643405.4112779726, 1224880.2965852122 665143.6860159477)"
geom = ogr.CreateGeometryFromWkt(wkt)
for i in range(0, geom.GetGeometryCount()):
    g = geom.GetGeometryRef(i)
    print(g)
   # print( "%i). %s" %(i, g.ExportToWkt()))

