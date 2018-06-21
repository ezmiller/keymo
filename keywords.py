import nltk
import gensim
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

model_path = './corpora/brown_tfidf.mm'
vocab_path = './corpora/brown_vocab.mm'

model = gensim.utils.SaveLoad.load(model_path)
vocab = gensim.utils.SaveLoad.load(vocab_path)


def ngramise(sequence):
    for bigram in nltk.ngrams(sequence, 2):
        yield bigram
    for trigram in nltk.ngrams(sequence, 3):
        yield trigram


def get_pairs(phrase, tag_combos=[('JJ', 'NN')]):
    tagged = nltk.pos_tag(nltk.word_tokenize(phrase))
    for ngram in ngramise(tagged):
        tokens, tags = zip(*ngram)
        if tags in tag_combos:
            yield tokens


def get_unigrams(phrase, tags=('NN')):
    tagged = nltk.pos_tag(nltk.word_tokenize(phrase))
    return [word for word, tag in tagged
            if tag in tags]


def get_tokens(doc):
    # this one is super slow. wonder why?
    unigrams = [tuple([word]) for word in get_unigrams(doc, ('NNP', 'NN'))]
    bigrams = list(get_pairs(doc))
    return unigrams + bigrams


def get_keywords(text):
    tokens = [" ".join(x) for x in get_tokens(text)]
    bow = vocab.doc2bow(tokens)
    scores = model[bow]
    sorted_list = sorted(scores, key=lambda x: x[1], reverse=True)
    for word_id, score in sorted_list:
        yield vocab[word_id], score
