import os
from osgeo import ogr

daShapefile = r"C:\Users\Dell\Desktop\Python\Python GDAL\New ShapeFile\local_unit\local unit.dbf"

driver = ogr.GetDriverByName('ESRI Shapefile')

dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.

# Check to see if shapefile is found.
if dataSource is None:
    print ('Could not open %s' % (daShapefile) )
else:
    print ('Opened %s' % (daShapefile))
    layer = dataSource.GetLayer()
    featureCount = layer.GetFeatureCount()
    print('Total Number Of Feature in the shape file', featureCount)