import re
from urllib import request as rq
from urllib import parse as pr
from urllib.error import *


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

