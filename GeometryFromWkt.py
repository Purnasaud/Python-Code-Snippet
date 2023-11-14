from osgeo import ogr

wkt = "POINT (1120351.5712494177 741921.4223245403)"
point = ogr.CreateGeometryFromWkt(wkt)
print(point)
#print ("%d,%d" % (point.GetX(), point.GetY()))

line = "LINESTRING (1116651.43937912 637392.696988746 0,1188804.01084985 652655.740953707 0,1226730.36252036 634155.081602239 0,1281307.30760719 636467.664021172 0)"
line1 = ogr. CreateGeometryFromWkt(line)
print(line1.GetX(), line1.GetY(2))
print(line1.GetPointCount())

pol ="POLYGON ((1154115.27456585 686419.444270136 0,1154115.27456585 653118.257437493 0,1165678.18666051 653118.257437493 0,1165678.18666051 686419.444270136 0,1154115.27456585 686419.444270136 0),(1149490.10972798 691044.609108003 0,1149490.10972798 648030.57611584 0,1191579.10975257 648030.57611584 0,1191579.10975257 691044.609108003 0,1149490.10972798 691044.609108003 0))"
poly1 = ogr.CreateGeometryFromWkt(pol)
print(poly1.GetPointCount())

poly2 = "MULTIPOLYGON (((1204067.05481481 634617.598086025 0,1204067.05481481 620742.103572424 0,1215167.45042569 620742.103572424 0,1215167.45042569 634617.598086025 0,1204067.05481481 634617.598086025 0)),((1179553.68117412 647105.543148266 0,1179553.68117412 626292.301377865 0,1194354.20865529 626292.301377865 0,1194354.20865529 647105.543148266 0,1179553.68117412 647105.543148266 0)))"
multiString1 = "MULTILINESTRING ((1214242.41745812 617041.971702131 0,1234593.14274473 629529.916764372 0),(1184641.36249577 626754.817861651 0,1219792.61526356 606866.609058823 0))"

l = ogr.CreateGeometryFromWkt(multiString1)
print(l.GetGeometryCount())

p = ogr.CreateGeometryFromWkt(poly2)

print(p.GetGeometryCount () )





