# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class TweetsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #_id = Field()  # 微博id
    weibo_url = Field()  # 微博URL
    created_at = Field()  # 微博发表时间
    #like_num = Field()  # 点赞数
    #repost_num = Field()  # 转发数
    #comment_num = Field()  # 评论数
    content = Field()  # 微博内容
    #user_id = Field()  # 发表该微博用户的id
    #crawl_time = Field()  # 抓取时间戳

class InformationItem(Item):
    """ 个人信息 """
    _id = Field()  # 用户ID
    nick_name = Field()  # 昵称
    gender = Field()  # 性别
    province = Field()  # 所在省
    city = Field()  # 所在城市
    brief_introduction = Field()  # 简介
    birthday = Field()  # 生日
    tweets_num = Field()  # 微博数
    follows_num = Field()  # 关注数
    fans_num = Field()  # 粉丝数
    sex_orientation = Field()  # 性取向
    sentiment = Field()  # 感情状况
    vip_level = Field()  # 会员等级
    authentication = Field()  # 认证
    person_url = Field()  # 首页链接
    crawl_time = Field()  # 抓取时间戳
    labels = Field()  # 标签
