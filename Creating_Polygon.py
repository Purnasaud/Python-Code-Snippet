from osgeo import ogr

ring = ogr.Geometry(ogr.wkbLinearRing)

ring.AddPoint(155252, 7266262)
ring.AddPoint(8777 , 6366333)
ring.AddPoint(87666 ,65432)

ring.AddPoint(77777, 82772722)
ring.AddPoint(766544, 765432)
ring.AddPoint(155252, 7266262)
poly = ogr.Geometry(ogr.wkbPolygon)

poly.AddGeometry(ring)

poly1 = poly.ExportToWkt()
print(poly1)
