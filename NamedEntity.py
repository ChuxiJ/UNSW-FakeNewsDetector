<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:40:47 2019

@author: 24583
"""
import pandas as pd
#import jieba
#import jieba.analyse
#import jieba.posseg as posg


data = pd.read_csv("train.csv")
#natures = pd.read_csv("natures.csv")

"""
sentence = data.iloc[177,1]

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

#data = data.iloc[:100]
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
#speechParts = ['n', 'm', 'v', 'a', 't', 'nr', 'ns', 'nt', 'nz', 'ng', 'nx', 'nnt']

speechParts = ['Mg', 'Rg', 'a', 'ad', 'ag', 'al', 'an', 'b', 'bl', 'c', 'cc', 'd',
 'dg', 'dl', 'e', 'f', 'g', 'gb', 'gc', 'gg', 'gi', 'gm', 'gp', 'i', 'j', 'k', 'l',
 'm', 'mq', 'n', 'nba', 'nbc', 'nf', 'ng', 'nhd', 'nhm', 'nis', 'nit', 'nmc', 'nnd',
 'nnt', 'nr', 'nrf', 'nrj', 'ns', 'nsf', 'nt', 'ntc', 'ntcb', 'ntch', 'nth', 'nto',
 'nts', 'ntu', 'nx', 'nz', 'o', 'p', 'pba', 'pbei', 'q', 'qt', 'qv', 'r', 'rr',
 'ry', 'rys', 'ryt', 'ryv', 'rz', 'rzs', 'rzt', 'rzv', 's', 't', 'tg', 'u', 'ude1',
 'ude2', 'ude3', 'udeng', 'udh', 'uguo', 'ule', 'ulian', 'uls', 'usuo', 'uyy', 'uzhe',
 'uzhi', 'v', 'vd', 'vf', 'vg', 'vi', 'vl', 'vn', 'vshi', 'vx', 'vyou', 'w', 'x', 'y', 'z']
    
#counts,nerlist, nlist, mlist, vlist, alist, tlist, nrlist, nslist, ntlist, nzlist, nglist, nxlist, nntlist = [],[],[],[],[],[],[],[],[],[],[],[],[],[]
counts = []
nerlist = []
natures = {}
for e in speechParts:
    natures[e] = []

#all_parts = set()
for sentence in sentences:
    ner = HanLP.segment(sentence)
    count = {}
    lists = {}
    for e in speechParts:
        lists[e] = {}
    #n, m, v, a, t, nr, ns, nt, nz, ng, nx, nnt = {},{},{}, {},{},{}, {},{},{}, {},{},{}
    for term in ner:
        nature = term.nature.toString()
        #all_parts.add(nature)
        nature_count = nature+'_count'
        if nature_count in count.keys():
            count[nature_count] += 1 
        else:
            count[nature_count] = 1              
        
        if term.word in lists[nature]:
            lists[nature][term.word] += 1
        else:
            lists[nature][term.word] = 1
    
    for e in speechParts:
        natures[e].append(lists[e])    
    counts.append(count)
    nerlist.append(ner)  
    #print('{}\t{}'.format(term.word, term.nature)) # 获取单词与词性

data['count'] = counts
data['NER'] = nerlist
for e in speechParts:
    data[e] = natures[e]

#data['name'], data['location'], data['organisation'], data['time'], data['SpecialNoun'] = pd.Series(namelist),pd.Series(loctlist),pd.Series(orglist),pd.Series(tmlist),pd.Series(nzlist)
data.to_csv("nerIndex.csv")
data.to_csv("ner.csv", index =False)

new = pd.read_csv("ner.csv")

### unicode中文范围 4E00-9FBF

print(data['n'])
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:40:47 2019

@author: 24583
"""
import pandas as pd
#import jieba
#import jieba.analyse
#import jieba.posseg as posg


data = pd.read_csv("train.csv")
#natures = pd.read_csv("natures.csv")

"""
sentence = data.iloc[177,1]

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

#data = data.iloc[:100]
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
#speechParts = ['n', 'm', 'v', 'a', 't', 'nr', 'ns', 'nt', 'nz', 'ng', 'nx', 'nnt']

speechParts = ['Mg', 'Rg', 'a', 'ad', 'ag', 'al', 'an', 'b', 'bl', 'c', 'cc', 'd',
 'dg', 'dl', 'e', 'f', 'g', 'gb', 'gc', 'gg', 'gi', 'gm', 'gp', 'i', 'j', 'k', 'l',
 'm', 'mq', 'n', 'nba', 'nbc', 'nf', 'ng', 'nhd', 'nhm', 'nis', 'nit', 'nmc', 'nnd',
 'nnt', 'nr', 'nrf', 'nrj', 'ns', 'nsf', 'nt', 'ntc', 'ntcb', 'ntch', 'nth', 'nto',
 'nts', 'ntu', 'nx', 'nz', 'o', 'p', 'pba', 'pbei', 'q', 'qt', 'qv', 'r', 'rr',
 'ry', 'rys', 'ryt', 'ryv', 'rz', 'rzs', 'rzt', 'rzv', 's', 't', 'tg', 'u', 'ude1',
 'ude2', 'ude3', 'udeng', 'udh', 'uguo', 'ule', 'ulian', 'uls', 'usuo', 'uyy', 'uzhe',
 'uzhi', 'v', 'vd', 'vf', 'vg', 'vi', 'vl', 'vn', 'vshi', 'vx', 'vyou', 'w', 'x', 'y', 'z']
    
#counts,nerlist, nlist, mlist, vlist, alist, tlist, nrlist, nslist, ntlist, nzlist, nglist, nxlist, nntlist = [],[],[],[],[],[],[],[],[],[],[],[],[],[]
counts = []
nerlist = []
natures = {}
for e in speechParts:
    natures[e] = []

#all_parts = set()
for sentence in sentences:
    ner = HanLP.segment(sentence)
    count = {}
    lists = {}
    for e in speechParts:
        lists[e] = {}
    #n, m, v, a, t, nr, ns, nt, nz, ng, nx, nnt = {},{},{}, {},{},{}, {},{},{}, {},{},{}
    for term in ner:
        nature = term.nature.toString()
        #all_parts.add(nature)
        nature_count = nature+'_count'
        if nature_count in count.keys():
            count[nature_count] += 1 
        else:
            count[nature_count] = 1              
        
        if term.word in lists[nature]:
            lists[nature][term.word] += 1
        else:
            lists[nature][term.word] = 1
    
    for e in speechParts:
        natures[e].append(lists[e])    
    counts.append(count)
    nerlist.append(ner)  
    #print('{}\t{}'.format(term.word, term.nature)) # 获取单词与词性

data['count'] = counts
data['NER'] = nerlist
for e in speechParts:
    data[e] = natures[e]

#data['name'], data['location'], data['organisation'], data['time'], data['SpecialNoun'] = pd.Series(namelist),pd.Series(loctlist),pd.Series(orglist),pd.Series(tmlist),pd.Series(nzlist)
data.to_csv("nerIndex.csv")
data.to_csv("ner.csv", index =False)

new = pd.read_csv("ner.csv")

### unicode中文范围 4E00-9FBF

print(data['n'])
>>>>>>> 0907af8103ffadc83d62ff2d595418c40f8a729c
