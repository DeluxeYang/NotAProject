#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')#防止windows CMD下的乱码错误
from bs4 import BeautifulSoup
import redis
from gevent import monkey; monkey.patch_all()
import gevent
from urllib import request, parse

Redis_Pool=redis.ConnectionPool(host='127.0.0.1',port=6379,db=0)  
Sohu_Redis = redis.StrictRedis(connection_pool=Redis_Pool) 
URL_FILTER = [None, '#', '/', '#top']#url过滤
START_URL = 'http://m.sohu.com/'#起始网址

def check_page(url):
    print(gevent.getcurrent(),'URL: %s\n' % url)
    filename = Sohu_Redis.get(url).decode('utf-8')
    try:
        f= open(filename, "r", encoding= 'utf-8')
        text = f.read()#打开文件
        links = get_all_links(text)
        for link in links:
            href = link.get('href')
            if href in URL_FILTER:#过滤
                continue
            if href.find('javascript', 0, 10) != -1:#过滤JavaScript
                continue
            whole_url = get_whole_url(href)#短链接前加上 m.sohu.com
            if not Sohu_Redis.get(whole_url):
                Sohu_Redis.lpush('sohu_to_be_visited', whole_url)
    except OSError as e:
        Sohu_Redis.lpush('sohu_to_be_visited', url)#如果打开失败，则需要重新下载，放入visit队列
    finally:
        f.close()

def get_all_links(text):# 获取所有页面中的a标签的链接
    soup = BeautifulSoup(text,"html.parser")
    return soup.find_all('a')

def get_whole_url(url):#获取完整url
    uhost = parse.urlparse(url)
    if uhost.netloc == "":#如果没有主url，则加上
        url = parse.urljoin(START_URL, url)
    elif uhost.scheme == '':#如果没有主url的情况下，也没有http，则加上http
        url = parse.urljoin('http:', url)#用于域名：//s.m.sohu.com/，并不知道这是怎么回事
    return url


def gevent_worker():
    while True:
        to_be_explored = Sohu_Redis.brpop('sohu_to_be_explored', 0)#从待访问列表取数据，阻塞
        check_page(to_be_explored[1].decode('utf-8'))

if __name__ == '__main__':
    try:
        #gevent_worker()
        gevent.joinall([gevent.spawn(gevent_worker) for i in range(20)])
    except Exception as e:
        print(str(e))