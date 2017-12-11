# -*- coding: utf-8 -*-
from __future__ import print_function
from gensim.models import KeyedVectors
import pprint
google_filename = '/home/weiwu/share/deep_learning/data/GoogleNews-vectors-negative300.bin'
wiki_filename = '/home/weiwu/share/deep_learning/data/model/word2vec_org_level5_finance'
model_wiki = KeyedVectors.load_word2vec_format(wiki_filename, binary=False)
model_google = KeyedVectors.load_word2vec_format(google_filename, binary=True)
result = model_wiki.most_similar(
    positive=['woman', 'king'], negative=['man'], topn=1)
# pprint.pprint(result)
pprint.pprint(model_wiki.most_similar(['gdp'], topn=50))
pprint.pprint(model_google.most_similar(['gdp'], topn=50))
