import puzzpy.wordplay
import re
from puzzpy.filter import search
from puzzpy.wordsets.sowpods import SOWPODS
from puzzpy.wordsets.foods import FOODS


"""
Backsolve answers to the spiky tower meta from the 2015 MIT Mystery Hunt. We are looking for words which can be expressed as two shorter words interleaved, one of which is a food and the other has some semantic relationship with a given image.
"""


def test():
    def match(word):
        for target in target_words:
            if re.match('.*' + '.*'.join(list(target)) + '.*', word):
                remainders = puzzpy.wordplay.remainders(word, target)
                for r in remainders:
                    if r in FOODS:
                        return True
        return False

    target_words = ['rump', 'rear', 'butt', 'back', 'nude', 'baby']
    print("=============")
    print(target_words)
    matches = sorted(search(SOWPODS, match))
    print('\n'.join(matches))
    assert 'frumpish' in matches

    target_words = ['ring', 'bell', 'ding', 'dong', 'toll']
    print("=============")
    print(target_words)
    matches = sorted(search(SOWPODS, match))
    print('\n'.join(matches))
    assert 'roiling' in matches


if __name__ == '__main__':
    test()