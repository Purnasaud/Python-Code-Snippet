from osgeo import ogr

wkt = "POINT (1234.55555 4564646.335335)"

pt = ogr.CreateGeometryFromWkt(wkt)

buffer_Distance = 50

buffering = pt.Buffer(buffer_Distance)

print('Buffer of a Given Point With Buffer Distance of', buffering)

print(buffering.ExportToWkt())