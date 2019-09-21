# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:40:47 2019

@author: 24583
"""
import pandas as pd
import jieba
import jieba.analyse
import jieba.posseg as posg




data = pd.read_csv("train.csv")

"""
sentence = data.iloc[1]

# 1.基于TF-IDF算法进行关键词抽取
# 人名
kw=jieba.analyse.extract_tags(sentence,topK=10,withWeight=True,allowPOS=('nr'))
# 地名
kw1=jieba.analyse.extract_tags(sentence,topK=10,withWeight=True,allowPOS=('ns'))
# 机构团体
kw2=jieba.analyse.extract_tags(sentence,topK=10,withWeight=True,allowPOS=('nt'))
# 其他专名
kw3=jieba.analyse.extract_tags(sentence,topK=10,withWeight=True,allowPOS=('nz'))
# 时间
kw4=jieba.analyse.extract_tags(sentence,topK=10,withWeight=True,allowPOS=('t'))


# 2.基于TextRank算法进行关键词抽取
kw5=jieba.analyse.textrank(sentence,topK=10,withWeight=True,allowPOS=('ns'))

words = posg.cut(sentence)
for word, flag in words:
    print('%s, %s' % (word, flag))

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def preprocess(sent):
    sent = nltk.word_tokenize(sentence)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(sentence)

# pyhanlp
result = HanLP.extractKeyword(sentence, 20)
print(result)
"""


# 3. pyhanlp
from pyhanlp import *
StandardTokenizer = JClass("com.hankcs.hanlp.tokenizer.StandardTokenizer")

sentences = data.iloc[:,1]

"""
def name_entity_recognition(sentences):
    segment = HanLP.newSegment().enableNameRecognize(True);
    for sentence in sentences:
        term_list = segment.seg(sentence)
        print(term_list)
        #print([i.word for i in term_list])

name_entity_recognition(sentences)

print(HanLP.segment(sentence))
"""
# 词性标注
# 人名 'nr'
# 地名 'ns'
# 机构团体 'nt'
# 时间 't'
# 其他专名 'nz'

namelist, loctlist, orglist, tmlist, nzlist = [],[],[],[],[]
for sentence in sentences:
    name, loct, org, tm, nz = [],[],[],[],[]
    for term in HanLP.segment(sentence):
        if term.nature.toString() == 'nr':
            name.append(term.word)
        elif term.nature.toString() == 'ns':
            loct.append(term.word)
        elif term.nature.toString() == 'nt':
            org.append(term.word)
        elif term.nature.toString() == 't':
            tm.append(term.word)
        elif term.nature.toString() == 'nz':
            nz.append(term.word)
    namelist.append(name)
    loctlist.append(loct)
    orglist.append(org)
    tmlist.append(tm)
    nzlist.append(nz)
    #print('{}\t{}'.format(term.word, term.nature)) # 获取单词与词性

data['name'], data['location'], data['organisation'], data['time'], data['SpecialNoun'] = pd.Series(namelist),pd.Series(loctlist),pd.Series(orglist),pd.Series(tmlist),pd.Series(nzlist)
data.to_csv("nerIndex.csv")
data.to_csv("ner.csv", index =False)

new = pd.read_csv("ner.csv")




