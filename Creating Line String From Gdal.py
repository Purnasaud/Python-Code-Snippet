from osgeo import ogr
line = ogr. Geometry(ogr.wkbLineString)

line.AddPoint(1231244 , 82732727)
line.AddPoint(5344171,  71636)
line.AddPoint(423521 , 6453637)
line.AddPoint(7654 , 8765)
x = line.ExportToWkt()

print(x)