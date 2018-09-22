#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return wsjcn

class wsjcn(BaseFeedBook):
    title                 = u'华尔街见闻'
    description           = u'提供财经资讯'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    # deliver_times         = [5,17] #5:00,17:00两次推送
    oldest_article        = 1 #12*60*60
    mastheadfile          = "mh_wsjcn.gif"
    coverfile             = "cv_wsjcn.jpg"
    network_timeout       = 60

    feeds = [
            (u'华尔街见闻', 'https://dedicated.wallstreetcn.com/rss.xml', True),
           ]
    
 