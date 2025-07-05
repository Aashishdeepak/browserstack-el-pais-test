from collections import Counter
import re

def analyze_words(titles):
    words = re.findall(r'\w+', ' '.join(titles).lower())
    freq = Counter(words)
    return {word: count for word, count in freq.items() if count > 2}
