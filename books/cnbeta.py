#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return cnbeta

class cnbeta(BaseFeedBook):
    title                 = u'cnbeta'
    description           = u'提供科技资讯'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    deliver_times         = [5,17] #5:00,17:00两次推送
    oldest_article        = 43200 #12*60*60
    mastheadfile          = "mh_cnbeta.gif"
    coverfile             = "cv_cnbeta.jpg"
    network_timeout       = 60

    feeds = [
            (u'cnbeta资讯', 'http://feeds2.feedburner.com/cnbeta-full?format=xml', True),
           ]
    
 