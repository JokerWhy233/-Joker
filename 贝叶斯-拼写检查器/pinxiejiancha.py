# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 19:30:24 2018

@author: Administrator
"""

import re, collections
 
def words(text): return re.findall('[a-z]+', text.lower()) 
 
def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model
 
NWORDS = train(words(open('big.txt').read()))
 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
 
def edits1(word):
    n = len(word)
    return set([word[0:i]+word[i+1:] for i in range(n)] +                     # deletion删除
               [word[0:i]+word[i+1]+word[i]+word[i+2:] for i in range(n-1)] + # transposition换置
               [word[0:i]+c+word[i+1:] for i in range(n) for c in alphabet] + # alteration改变
               [word[0:i]+c+word[i:] for i in range(n+1) for c in alphabet])  # insertion插入
    
def edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))

def known(words): return set(w for w in words if w in NWORDS)

#如果known(set)非空, candidate 就会选取这个集合, 而不继续计算后面的
def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=lambda w: NWORDS[w])
