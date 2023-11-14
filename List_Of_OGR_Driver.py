from osgeo import  ogr
cnt = ogr.GetDriverCount()
print("Total Number of Driver Count", cnt)
formatsList = []  # Empty List

for i in range(cnt):
    driver = ogr.GetDriver(i)
    print('Driver Reference = : ', driver)
    driverName = driver.GetName()
    if not driverName in formatsList:
        formatsList.append(driverName)

formatsList.sort() # Sorting the messy list of ogr drivers

for i in formatsList:
    print (i)