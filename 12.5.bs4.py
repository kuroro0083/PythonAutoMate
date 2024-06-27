import requests, bs4
url = "https://weather.cma.cn/web/weather/59316.html"
res = requests.get(url)
res.raise_for_status()
# print(res.text)
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)
elem = noStarchSoup.select('span')
len = len(elem)
for e in elem:
    print(str(e))
# txt = elem[0].getText()
# print(txt)
