from itertools import chain


def combine(filenames):
    yield from chain(*(open(f) for f in filenames))
