import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TKAgg')
fd = FreqDist()
for text in gutenberg.fileids():
	for word in gutenberg.word(text):
		fd.update(word)

ranks = []
freqs = []
for rank, word in enumerate(fd):
	ranks.append(rank+1)
	freqs.append(fd[word])

plt.loglog(ranks, freqs)
plt.xlabel('frequency(f', fontsize=14, fontweight='bold')
plt.ylabel('rank(r', fontsize=14, fontweight='bold')
plt.grid(True)
plt.show()