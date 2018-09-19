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
    deliver_times         = [5,17] #5:00,17:00两次推送
    oldest_article        = 43200 #12*60*60
    mastheadfile          = "mh_pingwestcn.gif"
    coverfile             = "cv_pingwestcn.jpg"
    network_timeout       = 60

    feeds = [
            (u'PingWest中文网', 'https://www.pingwest.com/feed', True),
           ]
    
 