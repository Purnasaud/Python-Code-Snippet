from osgeo import ogr

file = r"C:\Users\Dell\Desktop\Python\Python GDAL\New ShapeFile\local_unit\Local Unit"
driver = ogr.GetDriverByName('Esri Shapefile')

dataSource = driver. Open(file, 0)# Opening File

if dataSource is None:
    print('File Couldnt open')
else:
    print('Open', file)
    layer = dataSource.GetLayer()
    featureCount = layer.GetFeatureCount()
    print('Number of Feature in the given data is', featureCount)
