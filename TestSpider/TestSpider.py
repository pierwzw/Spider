from TestSpider import spider

url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36')
data = spider.getUrlData4(url, headers)
print(data)
#
# #清除缓存
# rq.urlcleanup()
#
# #encode
# urlencoded = rq.quote('www.baidu.com')
# #decode
# rq.unquote(urlencoded)

