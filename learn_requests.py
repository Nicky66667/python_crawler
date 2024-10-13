#https://mp.weixin.qq.com/s?__biz=Mzg2NzYyNjg2Nw==&mid=2247489896&idx=1&sn=a4686a0cefb12a9bc5d41b062327f545&chksm=ceb9e374f9ce6a622723e99c8e6c04dc25b268d474f259f85ec8da73d755f0de562bb584c63c&cur_album_id=2448798954764255234&scene=189#wechat_redirect

import requests

x = requests.get('https://www.bilibili.com/')

print(x.text)
