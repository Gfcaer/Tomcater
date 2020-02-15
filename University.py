#!/usr/bin/env python
# coding: utf-8

from html.parser import HTMLParser

import bs4
import requests
from bs4 import BeautifulSoup


# 通过传入网址信息创建一个获取网页文本的函数
def getHTMLText(url):
    # 判断获取网页文本过程中是否有错误
    try:
        # 打开网址获取文本，并且把延迟设置成30s
        r = requests.get(url, timeout=30)
        # 获取状态码
        r.raise_for_status()
        # 设置文件编码
        r.encoding = r.apparent_encoding
        # 如果成功返回网页文本
        return r.text
    except:
        # 获取网页文本有错误则返回空文本
        return ""


# 通过传入空列表和网页文本信息创建一个在大学列表中加入大学信息的函数
def fillUnivList(ulist, html):
    # 用BeautifulSoup将网页文本以’html.parser‘煮成一锅粥
    soup = BeautifulSoup(html, "html.parser")
    # 通过网页源代码我们可以发现我们需要的信息都在tbody标签内，因此我们循环找出’tbody‘标签及其子标签的内容
    for tr in soup.find('tbody').children:
        # 通过bs4.element.Tag判断是否为tr标签
        if isinstance(tr, bs4.element.Tag):
            # 对于tr标签的我们拿到tr标签里的td标签
            tds = tr('td')
            # [<td>1</td>, <td><div align="left">清华大学</div></td>, <td>北京</td>, <td>95.3</td>...
            # 我们通过筛选出我们需要的td标签中的文本并将其用列表的方式加入我们传入的列表ulist中
            ulist.append([tds[0].string, tds[1].string,
                          tds[2].string, tds[3].string])


# 通过传入学校列表信息创建一个打印大学列表的函数
def printUnivList(ulist, province):
    # 打印标题
    print("中国最好大学排名2018({}地区)".center(45, '-').format(province))
    # 设置一个format格式化的模板
    # 注意：这里的{4}是因为utf8格式的英文和中文字节数不同，python会自动用英文来填
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
    # 充空白位置，我们用chr(12288)将其修改成用中文填充空白位置
    # 打印第一行
    print(tplt.format("排名", "学校名称", "地区", "总分", chr(12288)))
    if province == '安徽':
        print(tplt.format(1, '安徽师范大学花津校区', '安徽', 99.9, chr(12288)))
    # 循环取出列表中的每一所大学的信息，取出的大学信息是列表的形式(可以控制range(len(ulist))的长度来控制想要打印的学校的数量)
    for i in range(len(ulist)):
        # 将每一所大学的信息以列表的形式赋值给u
        u = ulist[i]
        # u[2]是地区，判断是否为安徽地区（可以自己更改地区信息，如果删除该判断，打印所有学校信息，也可以更改判断条件）
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))
    # if u[2] == province:
    # 如果为安徽地区，我们打印属于安徽地区的每一所大学的信息
    #    print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))


# 创建一个运行函数
def main(province='河北'):
    # 创建一个空列表，为填充大学信息列表做准备
    uinfo = []
    # 定义一个想要爬取的网页
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    # 传入想要爬取的网页获取该网页文本信息
    html = getHTMLText(url)
    # 给填充大学信息函数传值
    fillUnivList(uinfo, html)
    # 给打印大学信息函数传值
    printUnivList(uinfo, province=province)


main()

# main(province='北京')
