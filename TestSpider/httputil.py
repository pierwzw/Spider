from urllib import request as rq
from urllib import parse as pr
from urllib.error import *
from http import cookiejar as cj



def getUrlData(url, filename):
    """
    获取url返回数据
    :param url:
    :param filename:
    :return:
    """
    try:
        # 可以设置超时时间
        file = rq.urlopen(url, timeout=1)
        # 返回与当前环境有关的信息
        info = file.info()
        code = file.getcode()
        utl = file.geturl()
        data = file.read()
        fhandle = open(filename, 'wb')
        bytenum = fhandle.write(data)
        return data
    except HTTPError as e:
        print(e.code, '\n', e.reason)
    except URLError as e:
        print(e.code, '\n', e.reason)
    finally:
        fhandle.close()


def getUrlData2(url, filename):
    try:
        file = rq.urlretrieve(url, filename=filename)
        data = file.read()
        return data
    except HTTPError as e:
        print(e.code, '\n', e.reason)
    except URLError as e:
        print(e.code, '\n', e.reason)


def getUrlData3(url, headers):
    """
    读取禁止爬虫的网页
    :param url:
    :return:
    """

    try:
        opener = rq.build_opener()
        # 必须转换成list,元组识别不了
        opener.addheaders = [headers]
        data = opener.open(url).read()
        return data
    except HTTPError as e:
        print(e.code, '\n', e.reason)
    except URLError as e:
        print(e.code, '\n', e.reason)


def getUrlDataByGet(url, key):
    """
    get方式获取网页内容
    :param url:
    :return:
    """

    try:
        key = rq.quote(key)
        url = url + key
        req = rq.Request(url)
        # 读取禁止爬虫的网页:req.add_header(headers[0], headers[1])
        data = rq.urlopen(req).read()
        return data
    except HTTPError as e:
        print(e.code, '\n', e.reason)
    except URLError as e:
        print(e.code, '\n', e.reason)


def getUrlDataByPost(url, postdata, *headers):
    """
    post方式获取网页内容
    :param url:
    :return:
    """

    try:
        postdata = pr.urlencode(postdata).encode('utf-8')
        req = rq.Request(url, postdata)
        # req.add_header(headers[0], headers[1])
        data = rq.urlopen(req).read()
        return data
    except HTTPError as e:
        print(e.code, '\n', e.reason)
    except URLError as e:
        print(e.code, '\n', e.reason)


def getUrlDataByProxy(proxy_addr, url):
    """
    通过代理ip获取内容（proxy_addr=ip:port）
    :param proxy_addr:
    :param url:
    :return:
    """

    try:
        proxy = rq.ProxyHandler({'http': proxy_addr})
        opener = rq.build_opener(proxy, rq.HTTPHandler)
        rq.install_opener(opener)
        data = rq.urlopen(url).read().decode('utf-8')
        return data
    except HTTPError as e:
        print(e.code, '\n', e.reason)
    except URLError as e:
        print(e.code, '\n', e.reason)


def getUrlDataWithLog(url):
    """
    开启debuglog
    :param url:
    :return:
    """

    try:
        httphd = rq.HTTPHandler(debuglevel=1)
        httpshd = rq.HTTPSHandler(debuglevel=1)
        opener = rq.build_opener(httphd, httpshd)
        rq.install_opener(opener)
        data = rq.urlopen(url)
        return data
    except HTTPError as e:
        print(e.code, '\n', e.reason)
    except URLError as e:
        print(e.code, '\n', e.reason)


def getWebPageWithCookie(url, url2, postdata, path, *headers):
    """
    通过cookie保存登录信息
    :param url:
    :param headers:
    :return:
    """

    req = rq.Request(url, postdata)
    req.add_header(headers[0], headers[1])
    #创建CookieJar对象
    cjar = cj.CookieJar()
    #创建cookie处理器， 并为其构建opener对象
    opener = rq.build_opener(rq.HTTPCookieProcessor(cjar))
    #将opener安装为全局,之后的urlopen也会默认使用安装的opener对象
    rq.install_opener(opener)
    file = opener.open(req)
    data = file.read()
    file = open(path+'/3.html', 'wb')
    file.write(data)
    file.close()
    #以下也会默认使用cookie
    data = rq.urlopen(url2).read()
    fhandle = open(path+'/4.html', 'wb')
    fhandle.write(data)
    fhandle.close()
























