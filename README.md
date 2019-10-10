# UNSW-FakeNewsDetector
Repro for this Data competition: https://www.biendata.com/competition/falsenews/rules/

# 步骤一: 看综述理解问题描述
[综述1](https://mp.weixin.qq.com/s/Emlzfgoo99T9xAsTKJRQXg)

[综述2](https://mp.weixin.qq.com/s/5D5cfLC6flnn9fCYlMplMQ)

[综述3](https://dl.acm.org/citation.cfm?id=3305260)

[比赛规则](https://www.biendata.com/competition/falsenews/rules/)

[经验帖1](https://towardsdatascience.com/i-trained-fake-news-detection-ai-with-95-accuracy-and-almost-went-crazy-d10589aa57c)

[经验帖2](https://github.com/zhpmatrix/nlp-competitions-list-review/blob/master/WSDM_Cup_2019_%E7%9C%9F%E5%81%87%E6%96%B0%E9%97%BB%E7%94%84%E5%88%AB.md)

[第一名解决方案](https://github.com/zhpmatrix/nlp-competitions-list-review/blob/master/references/WSDM2019_Fake_News_Classification/report2.pdf)

# 步骤二: 构建特征池

中科院Kaggle全球文本匹配竞赛华人第1名团队-深度学习与特征工程
                                                                                
https://github.com/HouJP/kaggle-quora-question-pairs

ppt  视频文件
链接:https://pan.baidu.com/s/117mU2n_l5YckOrcIxvpqIA  密码:6cv7

[百度开放API](https://ai.baidu.com/tech/textcensoring)

[科大讯飞开放API](https://www.xfyun.cn/services/adFilterRecg)

[腾讯文本审核API](https://cloud.tencent.com/document/api/271/35502)

[怎么样抓取微信小程序](https://93nv.com/archives/63)

[微信小程序爬虫](https://vp.fact.qq.com/miniSearchResult?title=%E5%93%88%E5%93%88%E5%93%88&num=0&size=20&_=1568525989622)

[预处理和数据增广](https://zhpmatrix.github.io/2019/03/08/preprocess-augmentation-in-nlp/)

[kaggle 问题意图识别任务](https://www.kaggle.com/c/quora-question-pairs/discussion/34355)

[Kashgari文本分类包](https://github.com/BrikerMan/Kashgari)

[roberta_zh](https://github.com/brightmart/roberta_zh)

[pytorch-transformer](https://github.com/huggingface/pytorch-transformers)

[第二次讨论分工脑图](https://coggle.it/diagram/XX3DAxz2ip44C8k1/t/%E7%AC%AC%E4%B8%80%E6%AC%A1%E8%AE%A8%E8%AE%BA)

[NLP工具集HAN](https://github.com/hankcs/pyhanlp)

[gobbli](https://github.com/RTIInternational/gobbli)

[PaddleHub](https://github.com/PaddlePaddle/PaddleHub)

[X2Paddle](https://github.com/PaddlePaddle/X2Paddle)

```python
from urllib.request import urlopen
from urllib.parse import quote
import string
import json
def Convert(string): 
    li = list(string.split(",")) 
    return li 
tag = input("今天您想搜索什么?\n")

url = "https://vp.fact.qq.com/miniSearchResult?title=" + str(tag) + "&num=0&size=20&_=1568525989622"
url = quote(url, safe=string.printable)
response = urlopen(url, timeout=20)
result = response.read().decode('utf-8','ignore').replace(u'\xa9', u'')

output = []
temp = Convert(result)
index = 0
for item in temp:
    if "title" in item:
        dict = {}
        dict["title"] = item[9:-1] 
        dict["result"] = 0 if temp[index + 1][-2] == "假" else 1 if temp[index + 1][-2] == "真" else 2 
        output.append(dict)
    index += 1

print(output)
output_2 = json.dumps(output)


```

# 步骤三: 构建模型池
- [x] ALBert
- [ ] XLNET
- [ ] RoBERTa
- [ ] DilletBERT
- [ ] ERNIE

五种预训练模型

- 'text'
- 'pre_20_words'
- 'pre_40_words'
- 'demoj'
- 'first_sentence'
- 'last_centence'
- 'translate'
- 're_translate'

# 整合的数据网盘

https://drive.google.com/open?id=1MlsqS-QnVnisE0HHfcsK4bYkEmyXcc14
