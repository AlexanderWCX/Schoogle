import requests
import json

#read in first postal code
postalCode = '730639'

#formulate the query to get information about the place identified by the postal code
url = 'https://developers.onemap.sg/commonapi/search?searchVal=' + postalCode + '&returnGeom=Y&getAddrDetails=Y&pageNum=1'

#use the get method found in requests to perform the query
res = requests.get(url)
res = res.text

#extract relevant data from the results
res = json.loads(res)
latitude1 = res['results'][0]['LATITUDE']
longitude1 = res['results'][0]['LONGITUDE']

#repeat for postal code 2
postalCode = '730638'
url = 'https://developers.onemap.sg/commonapi/search?searchVal=' + postalCode + '&returnGeom=Y&getAddrDetails=Y&pageNum=1'
res = requests.get(url)
res = res.text
res = json.loads(res)
latitude2 = res['results'][0]['LATITUDE']
longitude2 = res['results'][0]['LONGITUDE']

#formulate the query to get distance
start = latitude1 + ',' + longitude1
end = latitude2 + ',' + longitude2
routeType = 'walk'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI0ODAsInVzZXJfaWQiOjI0ODAsImVtYWlsIjoiZGFueWkxOTk4QGdtYWlsLmNvbSIsImZvcmV2ZXIiOmZhbHNlLCJpc3MiOi' \
        'JodHRwOlwvXC9vbTIuZGZlLm9uZW1hcC5zZ1wvYXBpXC92MlwvdXNlclwvc2Vzc2lvbiIsImlhdCI6MTU1MjQxMjkyMCwiZXhwIjoxNTUyODQ0OTIwLCJuYmYiOjE1NTI0MTI5MjAsImp0a' \
        'SI6IjZkMDRkYTZkZDhkZWE3NTcxM2Y4NDVlZDIwYTRhMzZiIn0.Di-ay6HpEavd9SYURG_azVQh96VJE_NgVWbT3s1QQ-A'
url = 'https://developers.onemap.sg/privateapi/routingsvc/route?start=' + start + '&end=' + end + '&routeType=' + routeType + \
      '&token=' + token

res = requests.get(url)
res = res.text

res = json.loads(res)
distance = res['route_summary']['total_distance']
distance = str(distance)
print(distance)