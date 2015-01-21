import puzzpy.wordplay
from puzzpy.filter import search
from puzzpy.semantics import semantic_similarity
from puzzpy.wordsets.sowpods import SOWPODS
from puzzpy.wordsets.foods import FOODS


"""
Backsolve answers to the spiky tower meta from the 2015 MIT Mystery Hunt. We are looking for words which can be expressed as two shorter words interleaved, one of which is a food and the other has some semantic relationship with a smiling face.
"""

face_words = set(word for word in SOWPODS if len(word) == 4 and semantic_similarity(word, 'face') > 0.8)
print('got face words')

def match(word):
    for subword1 in puzzpy.wordplay.subwords(word, contiguous=False):
        if subword1 in FOODS:
            remainders = puzzpy.wordplay.remainders(word, subword1)
            for r in remainders:
                if len(r) == 4 and r in SOWPODS:
                    if r in face_words:
                    # if semantic_similarity(r, 'face') > 0.8:
                        print(word, subword1, r)
                        return True
    return False


for r in search(SOWPODS, match):
    print(r)

