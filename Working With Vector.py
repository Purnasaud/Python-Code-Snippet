from osgeo import ogr
import os

DriverName = "ESRI Shapefile"      # e.g.: GeoJSON, ESRI Shapefile
FileName = 'test.shp'
driver = ogr.GetDriverByName(DriverName)
if os.path.exists(FileName):
     driver.DeleteDataSource(FileName)