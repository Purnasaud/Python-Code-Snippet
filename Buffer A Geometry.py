from osgeo import ogr

point = "POINT (12627.427 81231.821)"
geom = ogr.CreateGeometryFromWkt(point)
buffer = 50
poly = geom.Buffer(50)

print(geom.ExportToWkt(), "Buffer By", buffer , poly.ExportToWkt())
