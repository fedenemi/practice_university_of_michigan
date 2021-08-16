# Recomend correct words

import pandas as pd
import numpy as np
import nltk
from nltk.corpus import words
from nltk.metrics.distance import jaccard_distance, edit_distance
from nltk.util import ngrams


# Mispelled words. The correct ones are "riveting", "indulge" and "slink"
entries=["rivetting", "indulg","slinck"]

# Use Jaccard index to calculate distance between mispelled words and the ones in a dictionary
# With n-gram of 3 
correct_sp=pd.Series(words.words())
correct=[]
for w in entries:
    # the compared words have to begin with the same character
    spel=correct_sp[correct_sp.str.startswith(w[0])]
    distances = [(jaccard_distance(set(ngrams(w, 3)),set(ngrams(word, 3))), word) for word in spel]
    closest = min(distances)
    correct.append(closest[1])
print(correct)
# output=['riveting', 'indulge', 'sline']


# Now let's use Levenshtein edit-distance
outcomes = []
for entry in entries:
    distances = ((edit_distance(entry,
                                word), word)
                 for word in correct_sp)
    closest = min(distances)
    outcomes.append(closest[1])
    print(outcomes)
# output=['riveting', 'indulge', 'slick'] (it took longer)
