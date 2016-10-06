import sys
import ctrigram

class Trigdict:
    def __init__(self):
        self.allKeys = set()
        self.allValues = set()
        self.valdict = {}
        self.recreatedict = 1
        self.lock = 0
        self.shortdict = {}

    def makedict(self):
        ctrigram.buildindex([w for w in self.allKeys])
        self.lock = 1
        self.recreatedict = 0

    def     __setitem__(self, source, val):
        self.allKeys.add(source)
        self.allValues.add(val)
        if len(source)<3:
            self.shortdict.setdefault(source, []).append(val)
        self.valdict.setdefault(source, []).append(val)
        self.recreatedict = 1

    def exactmatch(self, source):
        if self.valdict.has_key(source):
            return [(1, b) for b in self.valdict[source]]
        else:
            return None

    def __getitem__(self, source, numitem=1):
        if self.recreatedict:
            self.makedict()
        matchlist = []
        matchdict = {}
        if len(source)<3:
            return [(1, w) for w in self.shortdict.get(source, [])]
        candidateMatches = ctrigram.lookup(source, numitem)
        if candidateMatches is None:
            return []
        res = []
        for matSource, score in candidateMatches[:numitem]:
            for stem in self.valdict[matSource]:
                res.append((score, stem))
        res.reverse()
        return res

    def bestmatches(self, word, numitem):
        return self.__getitem__(word, numitem)

    def keys(self):
        return self.allKeys

    def values(self):
        return self.allValues
