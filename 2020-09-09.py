from urllib import request
import re

url = "http://picture.10yan.com/"

user_agent = 'Chrome/4.0 (compatible; MSIE 5.5; Windows NT)'

def getHtml(url):
    req = request.Request(url, headers={'User-Agent':user_agent})
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    response.close()
    #print(html)
    return html

def getImg(html):
    patternImg = re.compile('<img src="http:(.*?)".*?>')
    jpglist = re.findall(patternImg, html)
    i = 0
    for item in jpglist:
        patternJpeg = re.compile('.*\.jpe{0,1}g', re.I)
        if patternJpeg.findall(item):
            try:
                request.urlretrieve("http:"+
                                    patternJpeg.findall(item)[0],
                                    "%d.jpg"%i)
            except:
                pass
        i+=1

html = getHtml(url)
getImg(html)
