from nltk.corpus import wordnet as wn


def semantic_similarity(word1, word2):
    words1 = word1.split('_')
    words2 = word2.split('_')
    max_p = 0
    word1_sim = set([])
    for s1 in wn.synsets(word1):
        word1_sim.add(s1)
        # word1_sim.update(s1.similar_tos())

    word2_sim = set([])
    for s2 in wn.synsets(word2):
        word2_sim.add(s2)
        # word2_sim.update(s2.similar_tos())

    for st1 in word1_sim:
        for st2 in word2_sim:
            p = st1.wup_similarity(st2)
            if p is None:
                p = 0
            if p == 1:
                return p
            if p > max_p:
                max_p = p
    if len(words1) > 1 or len(words2) > 1:
        sub_similarity = .9 * semantic_similarity(words1[-1], words2[-1])
    else:
        sub_similarity = 0
    return max(max_p, sub_similarity)


