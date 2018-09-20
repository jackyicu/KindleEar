#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Huxiu

class Huxiu(BaseFeedBook):
    title                 = u'虎嗅网'
    description           = u'在虎嗅，不错过互联网的每个重要时刻。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    deliver_times         = [5,17] #5:00,17:00两次推送
    oldest_article        = 43200 #12*60*60
    mastheadfile          = "mh_huxiu.gif"
    coverfile             = "cv_huxiu.jpg"
    network_timeout       = 60

    feeds = [
            (u'虎嗅网', 'https://www.huxiu.com/rss/0.xml', True),
           ]
    
 