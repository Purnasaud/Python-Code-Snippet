from osgeo import ogr

## Shapefile available?
driverName = "ESRI Shapefile"
drv = ogr.GetDriverByName( driverName )
if drv is None:
    print ("%s driver not available.\n" % driverName)
else:
    print  ("%s driver IS available.\n" % driverName)

## PostgreSQL available?
driverName = "PostgreSQL"
drv = ogr.GetDriverByName( driverName )
if drv is None:
    print ("%s driver not available.\n" % driverName)
else:
    print ("%s driver IS available.\n" % driverName)

# Not Available
driverName = "FileGDB"
drv = ogr.GetDriverByName( driverName )
if drv is None:
    print ("%s driver not available.\n" % driverName)
else:
    print ("%s driver IS available.\n" % driverName)    

# Not Available    
driverName = "SDE"
drv = ogr.GetDriverByName( driverName )
if drv is None:
    print ("%s driver not available.\n" % driverName)
else:
    print ("%s driver IS available.\n" % driverName)    
    