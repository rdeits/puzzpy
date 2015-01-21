from puzzpy.wordsets.sowpods import SOWPODS
from itertools import combinations, chain


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    from https://docs.python.org/2/library/itertools.html
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def subwords(word, contiguous=True):
    """
    Find all substrings of a word which are also words.
    """
    if contiguous:
        for n in range(1, len(word)):
            for offset in range(len(word)-n):
                candidate = word[offset:offset+n]
                if candidate in SOWPODS:
                    yield word[offset:offset+n]
    else:
        for indices in powerset(range(len(word))):
            if len(indices) == 0 or len(indices) == len(word):
                continue
            candidate = ''.join(word[x] for x in indices)
            if candidate in SOWPODS:
                yield candidate


def remainders(word, subword):
    """
    Return all possible (ordered) remainders after removing interleaved subword.
    """
    ovs = overlays(word, subword)
    for o in ovs:
        yield ''.join(l for (i, l) in enumerate(word) if i not in o)


def overlays(word, subword):
    """
    find all possible ways to overlay subword within word while maintaining order. Yields indices into word.
    """
    active_set = [[]]

    consumed = 0
    while True:
        new_active_set = []
        for item in active_set:
            if len(item) > 0:
                start = item[-1]+1
            else:
                start = 0
            for i, l in enumerate(word[start:], start):
                if l == subword[consumed]:
                    if consumed == len(subword) - 1:
                        yield item + [i]
                    else:
                        new_active_set.append(item + [i])
        if consumed == len(subword):
            break
        if len(new_active_set) == 0:
            break
        consumed += 1
        active_set = new_active_set[:]

