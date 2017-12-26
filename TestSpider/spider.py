import os
import re
import time
import threading
import queue
from urllib import request as rq
from urllib import error
from http import cookiejar as ck


def crawImage(url, page, path):
    """
    爬取京东笔记本图片
    :param url:
    :param page:
    :return:
    """

    html1 = rq.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result = re.compile(pat1).findall(html1)
    result1 = result[0]
    pat2 = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)
    x = 1
    if not os.path.exists(path):  # 判断是否存在新文件夹，否则创建  
        os.mkdir(path)
    for imageurl in imagelist:
        imagename = path + str(page) + str(x) + '.jpg'
        imageurl = 'http://' + imageurl
        try:
            rq.urlretrieve(imageurl, filename=imagename)
            x += 1
        except error.URLError as e:
            x += 1


def crawLink(url, headers):
    """
    爬取网页的所有链接
    :param url:
    :param headers:
    :return:
    """

    opener = rq.build_opener()
    opener.addheaders = [headers]
    rq.install_opener(opener)
    file = rq.urlopen(url)
    data = str(file.read())
    # 链接正则
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    # 去重
    link = list(set(link))
    return link


def crawContent(url, page, headers):
    """
    爬取网页文章
    :param url:
    :param page:
    :param headers:
    :return:
    """

    try:
        # 模拟成浏览器
        opener = rq.build_opener()
        opener.addheaders = [headers]
        # 将opener安装为全局
        rq.install_opener(opener)
        data = rq.urlopen(url).read().decode("utf-8")
        # 构建对应用户提取的正则表达式
        userpat = 'target="_blank" title="(.*?)">'
        # 构建段子内容提取的正则表达式
        contentpat = '<div class="content">(.*?)</div>'
        # 寻找出所有的用户
        userlist = re.compile(userpat, re.S).findall(data)
        # 寻找出所有的内容
        contentlist = re.compile(contentpat, re.S).findall(data)
        x = 1
        for user, content, i in zip(userlist, contentlist, [i for i in range(len(userlist))]):
            content = content.replace("\n", "")
            print('用户%d%d是:%s\n内容是%s' % (page, (i + 1), user, content))
    except error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        else:
            print(e.reason)


def use_proxy(proxy_addr, url):
    """
    设置代理
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
    except error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        # 延迟处理
        time.sleep(10)
    except Exception as e:
        print('exception:' + str(e))
        time.sleep(1)


def useno_proxy(url, headers):
    """
    :param proxy_addr:
    :param url:
    :return:
    """

    try:
        opener = rq.build_opener()
        opener.addheaders = [headers]
        rq.install_opener(opener)
        file = rq.urlopen(url)
        data = file.read().decode('utf-8')
        # data = rq.urlopen(url).read().decode('utf-8')
        return data
    except error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        # 延迟处理
        time.sleep(10)
    except Exception as e:
        print('exception:' + str(e))
        time.sleep(1)


def getListUrl(key, pagestart, pageend, proxy, headers):
    """
    获取所有文章的链接
    :param key:
    :param pagestart:
    :param pageend:
    :param proxy:
    :return:
    """

    try:
        urllist = []
        keycode = rq.quote(key)
        for page in range(pagestart, pageend + 1):
            url = "http://weixin.sogou.com/weixin?query=" + keycode + "&_sug_type_=&s_from=input&_sug_=y&type=2&page=" + str(
                page) + "&ie=utf8"
            data1 = useno_proxy(url, headers)
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'
            urllist.append(re.compile(listurlpat, re.S).findall(data1))
        print("共取到" + str(len(urllist)) + "页")
        return urllist
    except error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        # 延迟处理
        time.sleep(10)
    except Exception as e:
        print('exception:' + str(e))
        time.sleep(1)


def getContent(urllist, proxy, headers):
    """
    获取文章内容
    :param urllist:
    :param proxy:
    :return:
    """

    html1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>微信文章页面</title>
            </head>
            <body>'''
    fh = open('c:\\weixin\\1.html', 'wb')
    fh.write(html1.encode('utf-8'))
    fh.close()
    # 'ab'为以追加方式写入
    fh = open('c:\\weixin\\1.html', 'ab')
    for i in range(0, len(urllist)):
        for j in range(0, len(urllist[i])):
            try:
                url = urllist[i][j].replace('amp;', '')
                data = useno_proxy(url, headers)
                titlepat = "<title>(.*?)</title>"
                contentpat = 'id="js_content">(.*?)id="js_sg_bar"'
                title = re.compile(titlepat).findall(data)
                content = re.compile(contentpat, re.S).findall(data)
                thistitle = "此次没有获取到"
                thiscontent = "此次没有获取到"
                if title != []:
                    thistitle = title[0]
                if content != []:
                    thiscontent = content[0]
                dataAll = "<p>标题为:" + thistitle + "</p><p>内容为:" + thiscontent + "</p><br>"
                fh.write(dataAll.encode('utf-8'))
                print("第" + str(i) + "个网页处理第" + str(i) + "次处理")  # 便于调试
            except error.URLError as e:
                if hasattr(e, 'code'):
                    print(e.code)
                if hasattr(e, 'reason'):
                    print(e.reason)
                # 延迟处理
                time.sleep(10)
            except Exception as e:
                print('exception:' + str(e))
                time.sleep(1)
    fh.close()
    html2 = '''</body>
            </html>
            '''
    fh = open("c:\\weixin\\1.html", "ab")
    fh.write(html2.encode("utf-8"))
    fh.close()


listurl = []


# 线程1，专门获取对应网址并处理为真实网址
class geturl(threading.Thread):
    def __init__(self, key, pagestart, pageend, proxy, urlqueue):
        threading.Thread.__init__(self)
        self.pagestart = pagestart
        self.pageend = pageend
        self.proxy = proxy
        self.urlqueue = urlqueue
        self.key = key

    def run(self):
        page = self.pagestart
        # 编码关键词key
        keycode = rq.quote(key)
        # 编码"&page"
        pagecode = rq.quote("&page")
        for page in range(self.pagestart, self.pageend + 1):
            url = "http://weixin.sogou.com/weixin?type=2&query=" + keycode + pagecode + str(page)
            # 用代理服务器爬，解决IP被封杀问题
            data1 = use_proxy(self.proxy, url)
            # 列表页url正则
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat, re.S).findall(data1))
        # 便于调试
        print("获取到" + str(len(listurl)) + "页")
        for i in range(0, len(listurl)):
            # 等一等线程2，合理分配资源
            time.sleep(7)
            for j in range(0, len(listurl[i])):
                try:
                    url = listurl[i][j]
                    # 处理成真实url，读者亦可以观察对应网址的关系自行分析，采集网址比真实网址多了一串amp
                    url = url.replace("amp;", "")
                    print("第" + str(i) + "i" + str(j) + "j次入队")
                    self.urlqueue.put(url)
                    self.urlqueue.task_done()
                except error.URLError as e:
                    if hasattr(e, "code"):
                        print(e.code)
                    if hasattr(e, "reason"):
                        print(e.reason)
                    time.sleep(10)
                except Exception as e:
                    print("exception:" + str(e))
                    time.sleep(1)


# 线程2，与线程1并行执行，从线程1提供的文章网址中依次爬取对应文章信息并处理
class getcontent(threading.Thread):
    def __init__(self, urlqueue, proxy):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.proxy = proxy

    def run(self):
        html1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>微信文章页面</title>
        </head>
        <body>'''
        fh = open("c:\\2.html", "wb")
        fh.write(html1.encode("utf-8"))
        fh.close()
        fh = open("c:\\2.html", "ab")
        i = 1
        while (True):
            try:
                url = self.urlqueue.get()
                data = use_proxy(self.proxy, url)
                titlepat = "<title>(.*?)</title>"
                contentpat = 'id="js_content">(.*?)id="js_sg_bar"'
                title = re.compile(titlepat).findall(data)
                content = re.compile(contentpat, re.S).findall(data)
                thistitle = "此次没有获取到"
                thiscontent = "此次没有获取到"
                if (title != []):
                    thistitle = title[0]
                if (content != []):
                    thiscontent = content[0]
                dataall = "<p>标题为:" + thistitle + "</p><p>内容为:" + thiscontent + "</p><br>"
                fh.write(dataall.encode("utf-8"))
                print("第" + str(i) + "个网页处理")  # 便于调试
                i += 1
            except error.URLError as e:
                if hasattr(e, "code"):
                    print(e.code)
                if hasattr(e, "reason"):
                    print(e.reason)
                time.sleep(10)
            except Exception as e:
                print("exception:" + str(e))
                time.sleep(1)
        fh.close()
        html2 = '''</body>
        </html>
        '''
        fh = open("c:\\2.html", "ab")
        fh.write(html2.encode("utf-8"))
        fh.close()


# 并行控制程序，若60秒未响应，并且存url的队列已空，则判断为执行成功
class conrl(threading.Thread):
    def __init__(self, urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue

    def run(self):
        while (True):
            print("程序执行中")
            time.sleep(60)
            if (self.urlqueue.empty()):
                print("程序执行完毕！")
                exit()


def crawWithFullHeaders(url, filename, fullheaders):
    """
    浏览器伪装技术
    :param url:
    :param fullheaders:
    :return:
    """

    cjar = ck.CookieJar()
    proxy = rq.ProxyHandler({'http': '127.0.0.1:8888'})
    opener = rq.build_opener(proxy, rq.HTTPHandler, rq.HTTPCookieProcessor(cjar))
    headall = []
    for key, value in fullheaders.items():
        item = key, value
        headall.append(item)
    opener.addheaders = headall

    rq.install_opener(opener)
    data = rq.urlopen(url).read()
    fhandle = open(filename, 'wb')
    fhandle.write(data)
    fhandle.close()


if __name__ == '__main__':
    key = "人工智能"
    proxy = "127.0.0.1:8889"
    proxy2 = ""
    pagestart = 1  # 起始页
    pageend = 2  # 抓取到哪页
    urlqueue = queue.Queue()
    # 创建线程1对象，随后启动线程1
    t1 = geturl(key, pagestart, pageend, proxy, urlqueue)
    t1.start()
    # 创建线程2对象，随后启动线程2
    t2 = getcontent(urlqueue, proxy)
    t2.start()
    # 创建线程3对象，随后启动线程3
    t3 = conrl(urlqueue)
    t3.start()
