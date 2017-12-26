from TestSpider import httputil as sp, spider as sp

url222 = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36')
fullheaders = {"Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language": " zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0", "Connection": "keep-alive",
               "referer": "http://www.163.com/"}
postdata = {'wd': 'spider'}
url = 'http://www.baidu.com'
proxy_addr = '124.205.155.154:9090'

key = '人工智能'
proxy = "125.211.202.26:53281"
pagestart = 1
pageend = 2
urllist = sp.getListUrl(key, pagestart, pageend, proxy, headers)
sp.getContent(urllist, proxy, headers)
# for i in range(1,30):
#     url="https://www.qiushibaike.com/8hr/page/"+str(i)
#     sp.crawContent(url, i, headers)
# url = 'http://blog.csdn.net/'
# linklist = sp.crawLink(url, headers)
# for link in linklist:
# print(link[0])

# for i in range(1, 79):
#     url = 'https://list.jd.com/list.html?cat=670,671,672&page='+str(i)
#     sp.crawImage(url, i, 'c:\\image\\')
# pattern = 'ha|pier'
# string = 'hahadfpierkghg'
# result = sp.testRegex(pattern, string)
# print(result)
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
