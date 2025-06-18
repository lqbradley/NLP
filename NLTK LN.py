import nltk
import nltk.data
from nltk.corpus.reader import PlaintextCorpusReader
from nltk.text import Text
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import string
import sentencepiece as spm

# nltk module
nltk.download('punkt')
sent_detector = nltk.data.load('tokenizers/punkt/german.pickle')

# Loading corpus
corpus_root = 'C:/Users/libra/PycharmProjects/NLP/.venv/data/deu_news_2021_30K'
corpus = PlaintextCorpusReader(corpus_root, 'deu_news_2021_30K-sentences.txt')
plaintext = corpus.raw().lower()
sentences = corpus.sents('deu_news_2021_30K-sentences.txt')
#
# # Join sentences into a single string, with each sentence joined by a newline
# text = '\n'.join([' '.join(sentence) for sentence in sentences])
# print(text[:500])
#
# text1 = corpus.raw()
# print(text[:500])
#
# # Remove numbers at begininng of sentences
# reg_pattern = r'^\d+\t.'
# cleaned_text = re.sub(reg_pattern, '', text, flags=re.MULTILINE)
# print(cleaned_text[:500])
#
# # tokenize into words
# wordlists = cleaned_text.split()
# print(len(wordlists))
words = corpus.words()
# print(len(words))

# Calculate lexical richness
unique_words = set(words)
lexical_diversity = len(unique_words) / len(words)
print(lexical_diversity)
# 0.15909503284845206 - with regex, and .split()
# 0.15911464128592703

# character distribution of corpus
chars = [char for sentence in sentences for word in sentence for char in word]
fdist1 = FreqDist(chars)
print(fdist1.most_common(10))
fdist1.plot(30, cumulative=True)

# preprocessing
plaintext = corpus.raw()
text = nltk.tokenize.WordPunctTokenizer().tokenize(plaintext)


# Task 8
# find longest word
longest_word = max(unique_words, key=len)
print("Longest word:", longest_word)

# train sentencepiece model

