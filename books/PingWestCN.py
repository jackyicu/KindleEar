#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return PingWestCN

class PingWestCN(BaseFeedBook):
    title                 = u'PingWest中文网'
    description           = u'提供中文科技新闻'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    deliver_times         = [6,17] #6:00,17:00两次推送
    oldest_article        = 39600 #11*60*60
    mastheadfile          = "mh_pingwestcn.gif"
    coverfile             = "cv_pingwestcn.jpg"
    network_timeout       = 60
    fetch_img_via_ssl     = False
    feeds = [
            (u'PingWest中文网', 'http://www.pentitugua.com/rss.xml', True),
           ]
    
    # def soupbeforeimage(self, soup):
    #     # 更换另一个图库，因为RSS中的图库已经被封
    #     for img in soup.find_all('img', attrs={'src':True}):
    #         if img['src'].startswith('http://ptimg.org:88'):
    #             img['src'] = img['src'].replace('http://ptimg.org:88','http://pic.yupoo.com')
