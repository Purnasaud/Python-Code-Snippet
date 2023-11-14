from osgeo import ogr

shapefile = r"C:\Users\Dell\Desktop\Python\Python GDAL\New ShapeFile\local_unit\Local Unit"

driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 0)
layer = dataSource.GetLayer()
layer.SetSpatialFilter("'DISTRICT' = 'ACHHAM'")
for feature in layer:
    print (feature.GetField("DISTRICT"))
layer.ResetReading()