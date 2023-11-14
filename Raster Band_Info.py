from osgeo import gdal
# this allows GDAL to throw Python Exceptions
fn=r"C:\Users\Dell\Desktop\Python\Python GDAL\Raster Band\Raster\CompositBand.tif"
ds = gdal.Open(fn)
print(ds.RasterXsize)