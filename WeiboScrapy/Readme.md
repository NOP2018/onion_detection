# 爬取微博内容
参考大神 [@nghuyong](https://github.com/nghuyong/WeiboSpider/tree/simple) 的微博爬虫代码，使用 scrapy 和 mongodb爬取和存储数据。
目的是爬取洋葱故事会发布的假新闻和头条新闻发布的真新闻，以便后续作洋葱新闻鉴别（如果做得了的话），只需要原创微博内容数据，去除参考代码中爬取转评赞数据和评论数据的功能。
另外，其实我只需要新闻标题，所以在爬虫中对微博内容文本作了正则匹配。

使用时，只需在 spider 中填入需要爬取微博用户的 uid ，在 setting 中粘贴自己 cookies ，然后 scrapy crawl weibospider 即可。
