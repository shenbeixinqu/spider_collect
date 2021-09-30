import gopup as gp
# 微博热搜
weibo_hot = gp.weibo_hot_search_list()
zhihu_hot = gp.zhihu_hot_search_list()
history_today = gp.history_daily()
# print(weibo_hot)
# print(zhihu_hot)
# print(history_today)

covid_163_df = gp.covid_163(indicator="中国实时数据")
print(covid_163_df)