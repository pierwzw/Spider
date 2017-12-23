from TestSpider import spider as sp

url222 = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36')
postdata = {'wd': 'spider'}
url = 'http://www.baidu.com'
proxy_addr = '140.143.99.97:1080'

pattern = 'ha|pier'
string = 'hahadfpierkghg'
result = sp.testRegex(pattern, string)
print(result)
# data = sp.getUrlDataByProxy(proxy_addr, url)
# data = sp.getUrlDataWithLog(url)
# print(data)
# data = sp.getUrlDataByPost(url, postdata)
# print(data)
#
# #清除缓存
# rq.urlcleanup()
#
# #encode
# urlencoded = rq.quote('www.baidu.com')
# #decode
# rq.unquote(urlencoded)

