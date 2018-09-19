#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from base import BaseFeedBook

def getBook():
    return Xueqiu

class Xueqiu(BaseFeedBook):
    title                 = u'雪球'
    description           = u'雪球是一个社交投资网络，「今日话题」是雪球用户每日发布的投资交流精选。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_xueqiu.gif"
    coverfile             = "cv_xueqiu.jpg"
    deliver_times         = [6,17] #6:00,17:00两次推送
    oldest_article        = 39600 #11*60*60
    network_timeout       = 60

    feeds = [ (u'今日话题', 'http://xueqiu.com/hots/topic/rss', True) ]