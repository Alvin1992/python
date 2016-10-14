#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyquery import PyQuery as pq
import urllib2


class QSBK:
    """获取糗事百科的糗事"""
    def __init__(self):
        self.nextPage = 1  # 当前页码
        self.jokes = []   # 存放糗事，每一个元素就是一页糗事的列表
        self.userAgent = 'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64)' # 用户代理
        self.enabled = False # 决定程序是否继续执行

    def getPage(self, page):
        """获取某一页页面的代码"""
        try:
            req = urllib2.Request('http://www.qiushibaike.com/hot/page/' + str(page))
            req.add_header('User-Agent', self.userAgent)
            page = urllib2.urlopen(req).read().decode('utf-8')
            return page
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u'请求服务器失败，原因：', e.reason
            elif hasattr(e, 'code'):
                print u'不能完成请求，错误代码：', e.code
            return None

    def getJokes(self, page):
        """获取某一页的糗事列表"""
        response = self.getPage(page)
        if not response:
            print u'页面加载失败......'
            return None

        html = pq(response)
        allJokes = html('.article')  # 获取每个糗事最外层的元素

        jokesContainer = []  # 存放每页的糗事

        for joke in allJokes:
            joke = pq(joke)
            # 获取糗事内容，作者，神评论，点赞数，评论数
            jokeInfo = {
                "content": joke.find('.content span').html(),
                "author": joke.find('.author h2').html(),
                "comment": joke.find('.main-text').html(),
                "upvote": joke.find('.stats-vote i').html(),
                "commentNum": joke.find('.stats-comments i').html()
            }
            jokesContainer.append(jokeInfo)
        return jokesContainer

    def loadPage(self):
        """是否要加载新一页"""
        # 如果当前为看的页数少于2页，则加载新一页
        if self.enabled:
            if len(self.jokes) < 2:
                # 获取新一页
                jokes = self.getJokes(self.nextPage)
                # 将这一页糗事放到糗事列表中
                self.jokes.append(jokes)
                # 将页码加1表示下次要读取的页数
                self.nextPage += 1

    def getOneJoke(self, jokesContainer, page):
        """按下回车输出一个糗事"""
        # 遍历一页的糗事
        for joke in jokesContainer:
            # 等待用户输入
            cmd = raw_input()
            # 每当输入回车一次，判断一下是否要加载新页面
            self.loadPage()
            # 如果输入Q则程序结束
            if cmd == 'Q':
                self.enabled = False
                return
            print u'\n-----------第%s页 作者：%s 好评：%s 评论数：%s-------------' % (page, joke['author'], joke['upvote'], joke['commentNum'])
            try:
                print ('\n' + joke['content'].replace('<br />', '\n') + '\n')
            except UnicodeEncodeError, e:
                print u'编码错误'
            print u'-----------------------------------------------------------------'
            if not joke['comment']:
                print u'\n没有神评论'
            else:
                print u'\n神评论 %s' % joke['comment']

    def start(self):
        print u'正在读取糗事百科，按回车查看新段子，按Q退出'
        # 开启程序
        self.enabled = True
        # 加载一页内容
        self.loadPage()
        # 当前读到第几页
        curPage = 0
        while self.enabled:
            if len(self.jokes) > 0:
                # 取出一页糗事
                jokes = self.jokes[0]
                # 页数加1
                curPage += 1
                # 将取出的删除
                del self.jokes[0]
                # 输出这一页的糗事
                self.getOneJoke(jokes, curPage)

spider = QSBK()
spider.start()
