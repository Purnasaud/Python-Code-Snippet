from osgeo import gdal

file = r"C:\Users\Dell\Desktop\Python\Python GDAL\Raster Band\Raster\CompositBand.tif"

fc= gdal.Open(file)

# Printing Basics Raster Information
print(fc.RasterXSize, fc.RasterYSize)
print(fc.GetProjection() )
print(fc.GetGeoTransform())

# Print Raster Band Information
print("Total Number Of Band We Have Are: ", fc.RasterCount)
band1 = fc.GetRasterBand(1)

print(band1.GetStatistics(True, True) )

