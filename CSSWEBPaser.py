#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
以伪装浏览器访问的方式解析中国软件官网敏感信息

对于一些需要登录的网站，如果不是从浏览器发出的请求，则得不到响应。
所以，我们需要将爬虫程序发出的请求伪装成浏览器正规军。
具体实现：自定义网页请求报头。

1. 解析首页，得到所有的二级栏目主页面
2. 解析二级栏目主页面，得到所有的文章页面
3. 解析文章页面，得到关键字统计

"""

import re
import random
import string
import urllib.request

# 得到指定的URL页面中包含的所有URL地址


def get_urls_from_index(source_url):

    final_urls = set()

    html = get_url_content(source_url)
    url_re = re.compile(r'(?<=href=")\S+?html\Scss')

    url_list = url_re.findall(html)

    for i in range(len(url_list)):
        if url_list[i] not in final_urls:
            final_urls.add(url_list[i])
    return final_urls


# 根据URL，获取完整的内容
def get_url_content(url):
    # 判断获取网页文本过程中是否有错误
    try:
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/51.0.2704.63 Safari/537.36'
        }
        req = urllib.request.Request(url=url, headers=headers)
        res = urllib.request.urlopen(req)
        data = res.read()
        data = data.decode('utf-8')
        return data
    except:
        # 获取网页文本有错误则返回空文本
        return ""


# 根据URL，获取文章的内容
def artile_parser(articleUrl, keywords):

    # 获取文章所有内容
    articleUrl_msg = get_url_content(articleUrl)
    articleUrl_msg = str(articleUrl_msg)

    pattern = re.compile('articleContent.*?<h4>(.*?)</h4>.*?刊发时间：(.*?)</span>',
                         re.S)
    items = re.findall(pattern, articleUrl_msg)

    for item in items:
        print("文章标题: " + item[0])
        print("文章时间: " + item[1])
        keyStr = ""
        for keyword in keywords:
            keyword_count = word_count_in_str(articleUrl_msg, keyword)
            if keyword_count > 0:
                keyStr = keyStr + keyword + "[" + str(keyword_count) + "]"
        if len(keyStr) > 0:
            print("敏感信息: " + keyStr)
        else:
            print("敏感信息: 无")

    # 抓取本文所有的图片
    # getImg(articleUrl_msg)


# 统计字符串中某个词语出现的个数
def word_count_in_str(string, keyword):
    return len(string.split(keyword)) - 1


# 抓取制定网址的所有图片


def getImg(html):
    # <img src="/resource//uploads/images/20161107/079ff552e1204e8fbf2d639ebf0eee3d.jpg"

    img_re = re.compile(r'(?<=src=")\S+?jpg')

    img_list = img_re.findall(html)
    print("发现了%d张图片，正在下载......" % len(img_list))

    for i in range(len(img_list)):
        imgSrc = str(img_list[i])
        print("第[%d]张：%s" % (i, imgSrc))
        if imgSrc.startswith("file:"):
            print("图片位置错误，略过")
        else:
            imageName = 'D:\\workspace\\PythonTester\\out\\cssimages\\' + ''.join(
                random.sample(string.ascii_lowercase + string.digits,
                              16)) + '.jpg'
            urllib.request.urlretrieve("http://www.css.com.cn" + imgSrc,
                                       imageName)
    print("下载完成， 一共抓到了%d张图片" % len(img_list))


# 主函数
if __name__ == '__main__':
    print("正在分析中国软件官网， 请稍后......")
    url = "http://www.css.com.cn"

    # 关键字
    keywords = [
        "自主可控", "自主可靠", "安全可靠", "安可工程", "南风工程", "安可", "南风", "替代", "国产化",
        "打破国外垄断"
    ]

    urls = set()
    articles = set()
    counter = 0
    url_lists = get_urls_from_index(url)

    # print("首页解析完成， 找到"+str(len(url_lists))+"个URL地址")
    for aurl in url_lists:
        urls.add(url + aurl)
        aurls = get_urls_from_index(url + aurl)
        counter = counter + 1
        # print("解析第"+str(counter)+"个URL地址完成， 找到"+str(len(aurls))+"个URL地址")
        for burl in aurls:
            urls.add(url + burl)

    for curl in urls:
        curl.strip()
        lenght = len(curl)
        tmpStr = curl[lenght - 41:lenght]
        if tmpStr.find("/") == -1:
            articles.add(curl)

    print("分析完成， 共发现" + str(len(articles)) + "篇文章")

    articles_counter = 0
    for article in articles:
        articles_counter = articles_counter + 1
        print()
        print("正在解析第" + str(articles_counter) + "篇： " + article)
        artile_parser(article, keywords)
