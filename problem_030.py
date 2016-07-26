# Substring with Concatenation of All Words - https://leetcode.com/problems/substring-with-concatenation-of-all-words/
from Queue import Queue

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        ln = len(words[0])
        parts = len(s) / ln
        d = {}
        did = {}
        id = 0
        for word in words:
            if word not in d:
                d[word] = [id, 1]
                did[id] = word
                id += 1
            else:
                d[word][1] += 1
        res = []
        for i in xrange(ln):
            a = []
            for j in xrange(parts):
                ix = i + j * ln
                part = s[ix:ix + ln]
                if part in d:
                    a.append((d[part][0], ix))
                else:
                    a.append((-1, ix))
            j = 0
            start = 0
            counter = 0
            check = [0] * len(d)
            q = Queue()
            start_ix = 0
            while start < len(a):
                if counter == len(words):
                    found = True
                    for id in xrange(len(check)):
                        if check[id] != d[did[id]][1]:
                            found = False
                            break
                    if found:
                        res.append(start_ix)
                if j == len(a) or counter == len(words):
                    counter -= 1
                    start += 1
                    id = q.get()
                    check[id] -= 1
                    start_ix += ln
                    continue
                id, ix = a[j]
                if id == -1:
                    counter = 0
                    start = j + 1
                    j = start
                    check = [0] * len(d)
                    start_ix = 0
                    continue
                if counter == 0:
                    start_ix = ix
                check[id] += 1
                q.put(id)
                counter += 1
                j += 1
        return res