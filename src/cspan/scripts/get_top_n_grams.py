import pickle
import numpy as np

with open('/data/corpora/cspan/vocabulary_counts.pkl') as f:
	unigram_counts = pickle.load(f)

with open('/data/corpora/cspan/bigram_counts.pkl') as f:
	bigram_counts = pickle.load(f)

with open('/data/corpora/cspan/trigram_counts.pkl') as f:
	trigram_counts = pickle.load(f)

u_order = np.argsort(list(unigram_counts.values()))
b_order = np.argsort(list(bigram_counts.values()))
t_order = np.argsort(list(trigram_counts.values()))

unigrams=list(zip(np.array(list(unigram_counts.keys()))[u_order],np.array(list(unigram_counts.values()))[u_order]))
unigrams.reverse()

bgrams=list(zip(np.array(list(bigram_counts.keys()))[b_order],np.array(list(bigram_counts.values()))[b_order]))
bgrams.reverse()

tgrams=list(zip(np.array(list(trigram_counts.keys()))[t_order],np.array(list(trigram_counts.values()))[t_order]))
tgrams.reverse()

top_unigrams = [v for v in unigrams if v[1] >=5]
top_bgrams = [v for v in bgrams if v[1] >=5]
top_tgrams = [v for v in tgrams if v[1] >=5]

with open('/data/corpora/cspan/top_unigrams.pkl','wb') as f:
	pickle.dump(top_unigrams, f)

with open('/data/corpora/cspan/top_bigrams.pkl','wb') as f:
	pickle.dump(top_bgrams, f)

with open('/data/corpora/cspan/top_trigrams.pkl','wb') as f:
	pickle.dump(top_tgrams, f)
