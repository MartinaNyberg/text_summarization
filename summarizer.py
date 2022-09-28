import spacy
from spacy.lang.sv.stop_words import STOP_WORDS
from string import punctuation

nlp = spacy.load("sv_core_news_sm")

punctuation = punctuation + " "
STOP_WORDS.add("är")

def load_document(filename):
    with open(filename , "r", encoding="utf8") as f:
        text = f.read()
    text = text.replace("\n", " ")
    doc = nlp(text)
    return doc


def get_word_frequency_scores(document):
    word_frequencies = {}

    for token in document:
        if token.text.lower() not in STOP_WORDS and token.text not in punctuation:
            if token.lemma_ in word_frequencies:
                word_frequencies[token.lemma_] += 1
            else:
                word_frequencies[token.lemma_] = 1

    for word in word_frequencies:
        word_frequencies[word] /= max(word_frequencies.values())

    return word_frequencies


def get_sentence_scores(word_frequencies, document):
    sentence_scores = {}

    for sent in document.sents:
        for token in sent:
            if token.lemma_ in word_frequencies:
                if sent in sentence_scores:
                    sentence_scores[sent] += word_frequencies[token.lemma_]
                else:
                    sentence_scores[sent] = word_frequencies[token.lemma_]

    for sent in sentence_scores:
        sentence_scores[sent] /= len(sent) 
    return sentence_scores


def create_summary(sentence_scores, document, n_sents):
    top_ranked = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n_sents]
    summary = []
    for sent in document.sents:
        if sent in top_ranked:
            summary.append(sent.text.strip())
    print(" ".join(summary))


doc = load_document("text_sample.txt")
word_freq_scores = get_word_frequency_scores(doc)
sent_scores = get_sentence_scores(word_freq_scores, doc)

create_summary(sent_scores, doc, 5)
