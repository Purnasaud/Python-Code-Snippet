from osgeo import ogr

wkt ="LINESTRING (1234 5678, 91011 121314, 151617 181920, 212223 242526)"

geom = ogr.CreateGeometryFromWkt(wkt)
print(geom)
NumberOfPoint = geom.GetPointCount()

print('Number Of Point In the Given Geometry is: ', NumberOfPoint)