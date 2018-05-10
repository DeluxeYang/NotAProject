#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')#防止windows CMD下的乱码错误
from urllib import request, parse
import redis
import logging
from gevent import monkey; monkey.patch_all()
import gevent
import time

logging.basicConfig(filename = os.path.join(os.getcwd(), time.strftime('%Y-%m-%d-') + 'log.txt'),
        level = logging.WARN, filemode = 'a', format = '错误时间：%(asctime)s  %(message)s')

Redis_Pool=redis.ConnectionPool(host='127.0.0.1',port=6379,db=0)  
Sohu_Redis = redis.StrictRedis(connection_pool=Redis_Pool)  

START_URL = 'http://m.sohu.com/'#起始网址
MAIN_URL = 'm.sohu.com'
HEADERS = {#HTTP头
'User-Agent':'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25',
'Referer':'http://m.sohu.com'
}

def download_page(url, file_dir):# 获取所有页面中的a标签的链接
    print(gevent.getcurrent(),'\nURL: %s\n' % url)
    try:
        uhost = parse.urlparse(url)
        filename = file_dir + uhost.netloc + uhost.path.replace('/','_') + '.html'
        req = request.Request(parse.quote(url, safe='/:?='),headers=HEADERS)
        visit = request.urlopen(req, timeout=5)
        with open(filename, "wb") as f:#把访问的页面存储来下
            f.write(visit.read())
        code = visit.getcode()#获取状态码
        redirect = visit.geturl()#获取重定向链接
        uhost = parse.urlparse(redirect)
        if code in [200, 302]:#OK or Redirect
            if uhost.netloc.find(MAIN_URL) != -1:#返回的URL中包含主域名
                if not Sohu_Redis.get(url):
                    Sohu_Redis.set(url, filename)#访问过的页面，连通文件路径暂存在redis
                    Sohu_Redis.lpush('sohu_to_be_explored', url)#该页面是主站连接，已经下载好，可以去进一步检索
                print('访问成功'+'\n' + '-' * 50 + '\n') 
            else:
                print('访问成功,但为外链')
                print('\nRedirect URL: %s\n' % redirect, '\n' + '-' * 50 + '\n')
        else:
            print('Error Code: %s' % code,'\n' + '#' * 50 + '\n')
            write_log('warning', url, code )
    except Exception as e:
        print('Error', str(e),'\n' + '*' * 50 + '\n')
        write_log('error', url, str(e))

def write_log(log_type, url, message):
    logger = '\n错误链接：%s\n错误信息：%s\n%s\n' % (url, message, '-'*50)
    if log_type == 'error':
        logging.error(logger)
    elif log_type == 'warning':
        logging.warning(logger)

def gevent_worker():
    while True:
        to_be_visited = Sohu_Redis.brpop('sohu_to_be_visited', 0)[1].decode('utf-8')#从待访问列表取数据，阻塞
        if not Sohu_Redis.get(to_be_visited):
            download_page(to_be_visited, file_dir)

if __name__ == '__main__':
    try:
        file_dir = "temp/"
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        Sohu_Redis.lpush('sohu_to_be_visited', START_URL)
        #gevent_worker()
        gevent.joinall([gevent.spawn(gevent_worker) for i in range(10)])
    except Exception as e:
        print(str(e))