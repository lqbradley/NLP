import spacy
# load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")
# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

from nltk.corpus import gutenberg
es = gutenberg.sents('austen-emma.txt')

# words
ew = gutenberg.words('austen-emma.txt')
len(ew)
len(set(ew))

# characters
cc = len([char for sentence in es for word in sentence for char in word])
print(cc)

# usually use functions from NLTK Text module
import nltk
from nltk.book import *
type(text1)
max([len(w) for w in text1])

# retrieve URL and store it in a temporary location
import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass

# send POST request to server
import urllib.parse
url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   the_page = response.read()

# handling errors
req = urllib.request.Request('http://www.python.org/fish.html')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())

# open corpus as Python text strings
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
with urllib.request.urlopen(url) as response:
        raw = response.read().decode('utf-8')
        type(raw)
        len(raw)

text1.concordance("monstrous")

# disperson plot
import matplotlib
import matplotlib.pyplot as plt
text4.dispersion_plot(["citizens", "democracy", "duties", "America", "citiznes"])
plt.show()

# determining lexical richness
from nltk.text import Text
text_new = Text(["a", "b", "c"])
text_new.generate()

len(set(text_new)) / len(text_new)

def lexical_diversity(text):
        return len(set(text)) / len(text)
def percentage(count, total):
        return 100 * count / total
count = text_new.count("a")
lexical_diversity(text_new)
percentage(count, len(text_new))

# determining word frequency
from nltk.book import *
fdist1 = FreqDist(text1)
fdist1.plot(50, cumulative=True)

# finding properties of words
V = set(text1)
long_words = [w for w in V if len(w) > 15]

# comparing languages
from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']

# reading a corpus
from nltk.corpus import PlaintextCorpusReader
corpus_root = './data'
wordlists = PlaintextCorpusReader(corpus_root,
                                  'deu_mixed-typical_2011_1M-sentences-unicode-error.txt')
wordlists.fileids()
wordlists.words()

# common corpus functions
words()  #list of str
sents()  #list of (list of str)
paras()  #list of (list of (list of str))
categories()    #list of str
tagged_words()  #list of (str,str) tuple
tagged_sents()  #list of (list of (str,str))
tagged_paras()  #list of (list of (list of (str,str)))
chunked_sents() #list of (Tree w/ (str,str) leaves)
parsed_sents()  #list of (Tree with str leaves)
parsed_paras()  #list of (list of (Tree with str leaves))
xml()   #A single xml ElementTree
raw()   #unprocessed corpus contents

from nltk.corpus import treebank

treebank.fileids()
treebank.sents('wsj_001.mrg')
tree1 = treebank.parsed_sents('wsj_001.mrg')[0]

from nltk.tree import Tree, TreePrettyPrinter
TreePrettyPrinter(tree1)

grammar1 = ntlt.CFG.fromstring('''
    S -> NP VP
    VP => V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked"
    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
    Det -> "a" | "an" | "the" | "my"
    N -> "man" | "dog" | "cat" | "telescope" | "park" 
    P -> "in" | "on" | "by" | "with"
    ''')
sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

# PoS tagging
from nltk import word_tokenize
text = word_tokenize("They refuse to permit us to obtain the refuse permit")
nltk.pos_tag(text)

from nltk.tag import UnigramTagger
from nltk.corpus import brown
tagger = UnigramTagger(brown.tagged_sents(categories='news')[:500])
sent = ['Mitchell', 'decried', 'the', 'high', 'rate', 'of', 'unemployment']
for word, tag in tagger.tag(sent):
    print(word, '->', tag)

# helping for tagset documentation
from nltk.book import *
raw = ''.join(text1)
nltk.pos_tag(text1[:20])
nltk.help.upenn_tagset('RB')

# counting similar tags
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag,word) for (word, tag) in tagged_text
                                   if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())
tagdict = findtags('NN', nltk.corpus.brown.tagged_words(cateogries='news'))
for tag in sorted(tagdict):
    print(tag, tagdict[tag])

# RegEx Tagger
patterns = [
    (r'.*ing$', 'VBG'), # gerunds
    (r'.*ed$', 'VBD'), # simple past
    (r'.*es$', 'VBZ'), # 3rd singular present
    (r'.*ould$', 'MD'), # modals
    (r'.*\'s$', 'NN$'), # possessive nouns
    (r'.*s$', 'NNS'), # plural nouns
    (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'), # cardinal numbers
    (r'.*', 'NN') # nouns (default)
    ]
regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.tag(brown_sents[3])

# split train-test data
split_perc = 0.1
split_size = int(len(tagged_sents)* split_perc)
train_sents, test_sents = tagged_sents[split_size:], tagged_sents[:split_size]

from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import ClassifierBasedGermanTagger
tagger = ClassifierBasedGermanTagger(train=train_sents)

# combining taggers
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t2.evaluate(test_sents)

# can save a tagger after training using pickle
from pickle import dump
output = open('t2.pkl', 'wb')
dump(t2, output, -1)
output.close()

from pickle import load
input = open('t2.pkl','rb')
tagger = load(input)
input.close()

# German Tagger
corp = nltk.corpus.ConllCorpusReader('./data', 'tiger_release_aug07.corrected.1601'
    ['ignore', 'words', 'ignore', 'ignore', 'pos'],
    encoding='utf-8')
import random
tagged_sents = list(corp.tagged_sents())
random.shuffle(tagged_sents)
split_perc = 0.1
split_size = int(len(tagged_sents)* split_perc)
train_sents, test_sents = tagged_sents[split_size:], tagged_sents[:split_size]

from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import ClassifierBasedGermanTagger
tagger = ClassifierBasedGermanTagger(train=train_sents)
accuracy = tagger.accuracy(test_sents)
tagger.tag(['Das', 'ist', 'ein', 'einfacher', 'Test'])

# Stemmer
from nltk.stem.porter import *
stemmer = PorterStemmer()
plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
    'died', 'agreed', 'owned', 'humbled', 'sized',
           'meeting', 'stating', 'siezing', 'itemization',
           'sensational', 'traditional', 'reference', 'colonizer', 'plotted']
singles = [stemmer.stem(plural) for plural in plurals]
print(' '.join(singles))

# Lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
# pos is Part of Speech parameter, a=adjective,
# Valid options are `"n"` for nouns,
# `"v"` for verbs, `"a"` for adjectives, `"r"` for adverbs and `"s"`
# for satellite adjectives.
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))


# NLTK 101 Jupyter Notebook
from nltk import *
nltk.download()

# reading a file
f = open (FILE, 'r')
data = f.read()
# alternative way to read a file
for line in f:
    do_something(line)

myfile = './textfile.txt'
with open(myfile) as f:
    read_data = f.read() # read full content of file
    lines = set(read_data.splitlines()) # create a list of lines in file
# alternative: read file line by line
# for line in f:
# do_something(line)

thewords = word_tokenize(data)
from timeit import default_timer as timer
start = timer()
# do time-consuming operation
end = timer()
print("Operated %s seconds" % (end-start))

# Filtering a list
words = ['Hello', 'this', 'is', 'a', 'wordlist', 'with', '7', 'words']
words = [word.lower() for word in words]
words = [word for word in words if not word.isnumeric()]

wordfilter = filter(lambda w: not w.isnumeric(), words)
words = list(wordfilter)
print(words)

# Basic corpus functions
import matplotlib.pyplot as plt

fdist = nltk.FreqDist(ch.lower() for ch in text2 if ch.isalpha())
print(fdist.most_common(25))
plot = fdist.plot()
words = word_tokenize(data)
lengths = [ len(w) for w in words ]
wordsfd = nltk.FreqDist(words)
print(wordsfd.most_common(20))
from timeit import default_timer as timer
start = timer()
# do time-consuming operation
end = timer()
print("Operated %s seconds" % (end-start))

text1 = corp1.raw()
len(set(text1))/len(text1)

# Counters in Python
from collections import Counter

wordcounts = Counter(corp1.words())
wordcounts['Aber']

# NGrams built to analyze context of words
ngrams = nltk.ngrams( words, 2 )
frequencies = FreqDist( ngrams )
frequencies.most_common( 10 )

# do keyword-in-context searching against the text
text2 = Text(words)
print(text2.concordance('Kuste'))

# create a dispersion plot of given words
plot = text2.dispersion_plot( [ 'Liebe', 'Effi', 'Küste', 'Gott' ] )

# outputs the most significant bigrams, considering surrounding words
print(text2.collocations( num=10, window_size=4 ))  # window_size = no. of surrounding words

# given a set of words, what words are nearby
text2.common_contexts( ['herr', 'briest'], 200)

# list the words (features) most associated with the given word
text2.similar('herr',20)

# XMLCorpusReader
from nltk.corpus import XMLCorpusReader
corpus_root = './data'  # subdirectory called data is used to store the corpus file
corp1 = XMLCorpusReader(corpus_root, 'dewiki-latest-abstract1.xml')
# can then use functions like sents() and words() to split the corpus into sentences or words

# use stopwords from NLTK
default_stopwords = set(stopwords.words('german'))
# read additional stopwords from file
stopwords_file = './stopwords.txt'
with open(stopwords_file) as f:
    read_data = f.read()
    custom_stopwords = set(read_data.splitlines())
# bundle both words for all stopwords
all_stopwords = default_stopwords | custom_stopwords

# wordclouds