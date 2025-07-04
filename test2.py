# importing libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download("punkt")
nltk.download("stopwords")

# Input text - to summarize
text = """Non voglio negare che la testa appiattita e minuscola del grosso "stegosauro" ospita poco cervello dal nostro punto di vista soggettivo e pesante, ma desidero affermare che non dovremmo aspettarci di più dalla bestia. PRIMA DI TUTTO, gli animali di grandi dimensioni hanno cervelli relativamente più piccoli rispetto ai piccoli animali affini. La correlazione tra le dimensioni del cervello e le dimensioni del corpo tra gli animali affini (tutti i rettili, tutti i mammiferi, PER ESEMPIO) è straordinariamente regolare. QUANDO passiamo da animali piccoli a grandi, dai topi agli elefanti o dalle piccole lucertole ai draghi di Komodo, le dimensioni del cervello aumentano, MA non così velocemente come le dimensioni del corpo. IN ALTRE PAROLE, i corpi crescono più velocemente del cervello, E gli animali di grandi dimensioni hanno un basso rapporto tra peso del cervello e peso corporeo. IN FATTI, il cervello cresce solo a una velocità pari a circa due terzi della velocità del corpo. POICHÉ non abbiamo motivo di credere che gli animali di grandi dimensioni siano costantemente più stupidi dei loro parenti più piccoli, dobbiamo concludere che gli animali di grandi dimensioni richiedono relativamente meno cervello per fare altrettanto bene degli animali più piccoli. Se non riconosciamo questa relazione, è probabile che sottovalutiamo il potere mentale di animali molto grandi, in particolare dei dinosauri."""
# Tokenizing the text
stopWords = set(stopwords.words("italian"))
words = word_tokenize(text)

# Creating a frequency table to keep the
# score of each word

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

# Creating a dictionary to keep the score
# of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

# Sort sentenceValue dictionary by its values
sentenceValue = dict(sorted(sentenceValue.items(), key=lambda item: item[1], reverse=True))

# Storing sentences into our summary.
summary = ''
word_count = 0
for sentence in sentenceValue:
    if word_count >= 100:
        break
    summary += " " + sentence
    word_count += len(sentence.split())
print(summary)
