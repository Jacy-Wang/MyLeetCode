def buildTable(target):
    t = [0 for _ in xrange(len(target))]
    length = 0
    i = 1
    while i < len(target):
        if target[i] == target[length]:
            length += 1
            t[i] = length
            i += 1
        else:
            if length == 0:
                t[i] = 0
                i += 1
            else:
                length = t[length - 1]
    return t

def kmp(src, target):
    print "src", src
    print "target", target
    t = buildTable(target)
    i = 0
    j = 0
    while i < len(src):
        if src[i] == target[j]:
            i += 1
            j += 1
        if j == len(target):
            print "start from pos " + str(i - len(target))
            j = t[j - 1]
        elif i < len(src) and src[i] != target[j]:
            if j != 0:
                j = t[j - 1]
            else:
                i += 1

def testTable():
    s = "ababac"
    s2 = "abdba"
    print buildTable(s)
    print buildTable(s2)

if __name__ == "__main__":
    testTable()
    kmp("ababdabacab", "ababac")
    kmp("abcabdbabdbaab", "abdba")
