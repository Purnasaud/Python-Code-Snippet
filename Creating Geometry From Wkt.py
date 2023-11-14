from osgeo import ogr
WKT = "POINT (12345678.9888888 4352662533.665665)"
point = ogr.CreateGeometryFromWkt(WKT)
print('Geometry From Wkt', point)