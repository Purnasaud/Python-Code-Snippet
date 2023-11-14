from osgeo import ogr

shapefile = r"C:\Users\Dell\Desktop\Python\Python GDAL\New ShapeFile\local_unit\Local Unit"

dataSource = ogr.Open(shapefile)
daLayer = dataSource.GetLayer(0)
layerDefinition = daLayer.GetLayerDefn()


for i in range(layerDefinition.GetFieldCount()):
    print (layerDefinition.GetFieldDefn(i).GetName())