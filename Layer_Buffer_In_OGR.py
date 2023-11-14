from osgeo import ogr

shapefile = r"C:\Users\Dell\Desktop\Python\Python GDAL\New ShapeFile\local_unit\Local Unit"


driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 0)
layer = dataSource.GetLayer()
#layer.SetAttributeFilter("DISTRICT = 'ACHHAM'")
print(layer)
for feature in layer:
    field = feature.GetField('GaPa_NaPa')
    if field == 'Ramaroshan':
        print(field)
        geom = feature.GetGeometryRef()
       # print(geom.ExportToWkt())
       # wkt_Foemat = geom.CreateGeometryFromWkt(geom)
       # print(wkt_format)
        #geom = feature.GetGeometryRef()
        bufferDistance = 50
        buffer = geom.Buffer(50)
        print("Achham District is Buffer by", buffer.ExportToWkt())
 
layer.ResetReading()