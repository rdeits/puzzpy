from __future__ import print_function, division
from functools import reduce


class FilterSet(set):
    def __init__(self, test=lambda x: True):
        set.__init__(self, [])
        self.test = test

    def __contains__(self, element):
        return self.test(element)


def wrap(sets_or_functions):
    return [f if not callable(f) else FilterSet(f) for f in sets_or_functions]


def sort_filters(filtersets):
    nonzeros = [a for a in filtersets if len(a) > 0]
    zeros = [a for a in filtersets if len(a) == 0]
    if len(nonzeros) == 0:
        raise ValueError('You have to give me at least one set that I can iterate over (for example, a word list, or a constraint on the length of the output string)')
    return sorted(nonzeros, key=len) + zeros


def intersection(s1, s2):
    return set(el for el in s1 if el in s2)


def search(*filtersets):
    filters = sort_filters(wrap(filtersets))
    yield from (el for el in filters[0] if all(el in f for f in filters[1:]))
