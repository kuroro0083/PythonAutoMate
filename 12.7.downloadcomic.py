import requests, bs4, os, time
from pathlib import Path

count = 1
max = 100
baseUrl = 'https://xkcd.com/'
startUrl = 'https://xkcd.com/1'
while(not startUrl.endswith('#') and count <= max):
    # get next url
    startUrl = baseUrl + str(count)

    # open start url
    print('opening: %s' % startUrl)
    try:
        res = requests.get(startUrl)
        res.raise_for_status()
        bs = bs4.BeautifulSoup(res.text, 'html.parser')
    except Exception as exc:
        bs = None
        print('Can\'t open url %s' % startUrl)
        print(exc)

    # get image url and download image
    if bs:
        elemImg = bs.select('#comic img')
        if elemImg:
            print('Downloading image from %s' % startUrl)
            imgUrl = "https:" + elemImg[0].attrs['src']
            try:
                imgRes = requests.get(imgUrl)
                imgRes.raise_for_status()
                imgFile = open(Path(Path.cwd(), 'file/12.7.xkcd/', str(count) + '.' + os.path.basename(imgUrl)), 'wb')
                for chunk in imgRes.iter_content(10000):
                    imgFile.write(chunk)
                imgFile.close()
            except Exception as exc:
                print('Can\'t download image, url %s' % startUrl)
                print(exc)
        else:
            print('Can\'t find image from %s' % startUrl)

        count += 1
    print('========== sleeping =========')
    time.sleep(3)

# print(preUrl.endswith('#'))
# print(preUrl)
