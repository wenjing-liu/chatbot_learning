import nltk
from nltk.corpus import brown

'''
porter = nltk.PorterStemmer()
result = porter.stem('lying')
print(result)
'''

'''
text = nltk.word_tokenize("And now for something completely different")
result = nltk.pos_tag(text)
print(result)
'''
'''
result = nltk.pos_tag(['i', 'love', 'you'])
print(result)
'''

'''
result = nltk.pos_tag(['love', 'and', 'hate'])
print(result)
'''

'''
tagged_token = nltk.tag.str2tuple('fly/NN')
print(tagged_token)
'''

'''
sent = '我/NN 是/IN 一个/AT 大/JJ 傻×/NN'
result = [nltk.tag.str2tuple(t) for t in sent.split()]
print(result)
'''

'''
result = nltk.corpus.brown.tagged_words()
print(result)
'''

'''
default_tagger = nltk.DefaultTagger('NN')
raw = '我 累 个 去'
tokens = nltk.word_tokenize(raw)
tags = default_tagger.tag(tokens)
print(tags)
'''

'''
pattern = [(r'.*们$','PRO')]
tagger = nltk.RegexpTagger(pattern)
print(tagger.tag(nltk.word_tokenize('我们 累 个 去 你们 和 他们 啊')))
'''

tagged_sents = [[(u'我', u'PRO'), (u'小兔', u'NN')]]
unigram_tagger = nltk.UnigramTagger(tagged_sents)
sents = brown.sents(categories='news')
sents = [[u'我', u'你', u'小兔']]
tags = unigram_tagger.tag(sents[0])
print(tags)

brown_tagged_sents = brown.tagged_sents(categories='news')
print(brown_tagged_sents)

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)

