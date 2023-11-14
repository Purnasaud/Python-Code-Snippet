from osgeo import gdal
file =r"C:\Users\Dell\Desktop\Python\Python GDAL\Raster Band\Raster\CompositBand.tif"
rb = gdal.Open(file)

noband = rb.RasterCount
for bands in range(1, (noband + 1)):
    print('Printing band No: ' , bands , )
    band = rb.GetRasterBand(bands)
    stats= band.GetStatistics(True, True)
    print("Band: " , bands , "Information")
    print("Minimum Value: " , stats[0], "Maximum Value : ", stats[1], "Mean : " , 
    stats[2],"Standard Deviation : ", stats[3])
    print('')
    