import urllib.request as rq

#
url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36')
print(headers)
opener = rq.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
fhandle = open('c:\\3.html', 'wb')
bytenum = fhandle.write(data)
fhandle.close()

# file = rq.urlopen("http://www.baidu.com")
# data = file.read()
# dataline = file.readline()
#
# #返回与当前环境有关的信息
# info = file.info
# code = file.getcode()
# utl = file.geturl()
#
#
#
#
#
# filename = rq.urlretrieve('www.baidu.com', filename='c:\\2.html')
#
# #清除缓存
# rq.urlcleanup()
#
# #encode
# urlencoded = rq.quote('www.baidu.com')
# #decode
# rq.unquote(urlencoded)

