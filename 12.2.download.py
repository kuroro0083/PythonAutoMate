import requests

dUrl = "http://ufile.gd-baoyang.com/cover/1717556993-6179911d-8f03-3a30-a392-ef19cd9ea1e4.jpg"
res = requests.get(dUrl)
# print(type(res))

img = open('./file/12.2.jpg', 'bw')
for chunk in res.iter_content(10000):
    img.write(chunk)


