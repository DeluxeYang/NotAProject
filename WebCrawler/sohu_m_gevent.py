#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    题目：
    请设计一个系统，自动完成对于手机搜狐(http://m.sohu.com/)系统可靠性的检测。
    具体要求：
    1. 递归检测所有m.sohu.com域名的页面以及这些页面上的链接的可达性，即有没有出现不可访问情况。
    2. m.sohu.com域名页面很多，从各个方面考虑性能优化。
    3. 对于错误的链接记录到日志中，日志包括：URL，时间，错误状态等。
    要求：不使用框架。 加分项：使用并发方式实现。
'''
import os
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')#防止windows CMD下的乱码错误
import time
from urllib import request, parse
from bs4 import BeautifulSoup
import logging
import queue
from gevent import monkey; monkey.patch_all()
import gevent

START_URL = 'http://m.sohu.com/'#起始网址
MAIN_URL = 'm.sohu.com'
HEADERS = {#HTTP头
'User-Agent':'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25',
'Referer':'http://m.sohu.com'
}

logging.basicConfig(filename = os.path.join(os.getcwd(), time.strftime('%Y-%m-%d-') + 'log.txt'),
        level = logging.WARN, filemode = 'a', format = '错误时间：%(asctime)s  %(message)s')

CHECKED_NUM = 0#已记录的url的数
CHECKED_DICT = {}#辅助数据结构1：字典————用来记录url
URL_QUEUE = queue.Queue(maxsize = 0)##辅助数据结构2：队列————用于递归检索所有网页
URL_FILTER = [None, '#', '/', '#top']#url过滤

def check_page_links(url):   
    print(gevent.getcurrent(),'\n进入页面： %s\n' % url)
    global CHECKED_NUM
    links = get_all_links(url)# 提取页面链接
    for link in links:
        href = link.get('href')
        if href in URL_FILTER:#过滤
            continue
        if href.find('javascript', 0, 10) != -1:#过滤JavaScript
            continue
        if href not in CHECKED_DICT:#将以检查过的连接存入dict，查找时间为O(1)
            CHECKED_NUM += 1
            CHECKED_DICT[href] = CHECKED_NUM#dict存入格式为 href=num
            url = get_whole_url(href)#短链接前加上 m.sohu.com
            print('第%d个url: %s' % (CHECKED_DICT[href], url))
            check_url(url)#检测可达性

def get_all_links(url):# 获取所有页面中的a标签的链接
    text = request.urlopen(url).read()
    soup = BeautifulSoup(text,"html.parser")
    return soup.find_all('a')

def get_whole_url(url):#获取完整url
    uhost = parse.urlparse(url)
    if uhost.netloc == "":#如果没有主url，则加上
        url = parse.urljoin(START_URL, url)
    elif uhost.scheme == '':#如果没有主url的情况下，也没有http，则加上http
        url = parse.urljoin('http:', url)#用于域名：//s.m.sohu.com/，并不知道这是怎么回事
    return url

def check_url(url):#检测当前url的可达性，且如果该url是主域名下的，则放入队列
    print(gevent.getcurrent(),'\nURL: %s\n' % url)
    try:
        req = request.Request(parse.quote(url, safe='/:?='),headers=HEADERS)#quote处理url中的中文
        open_url = request.urlopen(req, timeout=5)#发起Request
        code = open_url.getcode()#获取状态码
        redirect = open_url.geturl()#获取重定向链接
        uhost = parse.urlparse(redirect)
        if code in [200, 302]:#OK or Redirect
            if uhost.netloc.find(MAIN_URL) != -1:#返回的URL中包含主域名
                #URL_QUEUE.put(redirect)
                print('访问成功'+'\n' + '-' * 50 + '\n') 
            else:
                print('访问成功,但重定向为外链，不加入队列')
                print('\nRedirect URL: %s\n' % redirect, '\n' + '-' * 50 + '\n')
        else:
            print('Error Code: %s' % code,'\n' + '#' * 50 + '\n')
            write_log('warning', url, code )
    except Exception as e:
        print(str(e),'\n' + '*' * 50 + '\n')
        write_log('error', url, str(e))

def write_log(log_type, url, message):
    logger = '\n错误链接：%s\n错误信息：%s\n%s\n' % (url, message, '-'*50)
    if log_type == 'error':
        logging.error(logger)
    elif log_type == 'warning':
        logging.warning(logger)

def gevent_worker():
    global CHECKED_NUM
    count = 0
    while True:
        if URL_QUEUE.empty() == False:  #如果queue不为空
            url = URL_QUEUE.get()       #从queue中取数据
            check_page_links(url)       
            URL_QUEUE.task_done()
            count = 0
        else:
            time.sleep(1)#如果queue为空，等待1秒
            count += 1
            if count > 5:#等待超过5次，退出
                break

if __name__ == '__main__':
    try:
        start = time.time()
        URL_QUEUE.put(START_URL)
        gevent.joinall([gevent.spawn(gevent_worker) for i in range(20)])
    except Exception as e:
        print(str(e))
    finally:
        print(time.time()-start)
