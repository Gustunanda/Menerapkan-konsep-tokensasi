from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tag import CRFTagger
from pprint import pprint

reviews = [
    "Komputer adalah perangkat elektronik yang menerima" 
    "Menyimpan dan memproses data menjadi informasi"
    "Secara matematis atau logis sesuai dengan serangkaian instruksi yang diprogram"
    "Program-program ini memungkinkan komputer untuk melakukan berbagai macam tugas"
    "Sistem komputer adalah komputer lengkap yang mencakup perangkat keras"
    "sistem operasi (perangkat lunak utama)"
    "Perangkat keras adalah bagian fisik komputer"
    "erangkat lunak adalah serangkaian instruksi yang memberi tahu perangkat keras"
    "apa yang harus dilakukan dan cara melakukannya serta kapan harus berhenti melakukannya"
    "seperti peramban web, pemutar media, atau pengolah kata"

]

#indo_stopwords = stopwords.words('indonesian')
#print(indo_stopwords)
stop_words = set(stopwords.words("indonesian"))

#tokenizing
word_tokens = []
for review in reviews:
    word_tokens.append(word_tokenize(review))
pprint(word_tokens)

#case folding
casefolded_sentence = []
for word_token in word_tokens:
    casefolded_sentence.append([word.casefold() for word in word_token])
#pprint(casefolded_sentence)

#stop word removal
filtered_sentence = []
for sent in casefolded_sentence:
    filtered_sentence.append([word for word in sent if not word in stop_words])
#pprint(filtered_sentence)

# parse list of word to sentence
sentences = []
for filtered_sent in filtered_sentence:
    sentences.append(' '.join(filtered_sent))
#pprint(sentences)

#stemming
stemmer = StemmerFactory().create_stemmer()
for sentence in sentences:
    stemmed_sentence.append(stemmer.stem(sentence).split(" "))
#pprint(stemmed_sentence)

#pos tagging
ct = CRFTagger()
ct.set_model_file('komputer.crf.tagger')
results = ct.tag_sents(stemmed_sentence)
#pprint(results)