import nltk
from nltk import word_tokenize
from nltk.util import bigrams
from collections import Counter, defaultdict

nltk.download('punkt')

# Sample text
text = "This is a simple example of a bigram model. This bigram model is a simple example."

# Tokenize the text
tokens = word_tokenize(text.lower())

# Generate bigrams
bi_grams = list(bigrams(tokens))

# Count bigram frequencies
bigram_freqs = Counter(bi_grams)

# Count unigram frequencies
unigram_freqs = Counter(tokens)

# Calculate probabilities
bigram_prob = defaultdict(lambda: defaultdict(float))

for (w1, w2), count in bigram_freqs.items():
    bigram_prob[w1][w2] = count / unigram_freqs[w1]

# Print the probabilities
for w1 in bigram_prob:
    for w2 in bigram_prob[w1]:
        print(f"P({w2} | {w1}) = {bigram_prob[w1][w2]:.4f}")

# Generate text
import random

def generate_text(start_word, length=10):
    current_word = start_word
    result = [current_word]
    for _ in range(length - 1):
        next_words = list(bigram_prob[current_word].keys())
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        current_word = next_word
    return ' '.join(result)

# Generate text starting with 'this'
print(generate_text('this'))