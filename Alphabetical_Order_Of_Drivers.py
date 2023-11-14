from osgeo import ogr
cnt = ogr.GetDriverCount()
formatsList = []  # Empty List

for i in range(cnt):
    drive = ogr.GetDriver(i)
    driverName = drive.GetName()
    if not driverName in formatsList:
        formatsList.append(driverName)
formatsList.sort()

for drivers in formatsList:
    print(drivers)