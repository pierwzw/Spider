import urllib.request as rq


def getUrlData(url, filename):
    file = rq.urlopen(url)
    # 返回与当前环境有关的信息
    info = file.info()
    code = file.getcode()
    utl = file.geturl()
    data = file.read()
    fhandle = open(filename, 'wb')
    bytenum = fhandle.write(data)
    fhandle.close()
    return data


def getUrlData2(url, filename):
    file = rq.urlretrieve(url, filename=filename)
    data = file.read()
    return data


def getUrlData3(url, headers):
    """
    读取禁止爬虫的网页
    :param url:
    :return:
    """

    opener = rq.build_opener()
    opener.addheaders = headers
    data = opener.open(url).read()
    return data


def getUrlData4(url, headers):
    """
    读取禁止爬虫的网页2
    :param url:
    :return:
    """

    req = rq.Request(url)
    req.add_header(headers)
    data = rq.urlopen(req).read()
    return data
