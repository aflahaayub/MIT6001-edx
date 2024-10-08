def lyrics_to_freq(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

lyrics = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'yeah', 'she' ,'loves', 'you']
print(lyrics_to_freq(lyrics))


def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result


# this method sometimes called "MEMOIZATION"
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2,d)
        d[n]=ans
        return ans

d = {1:1, 2:2}
print(fib_efficient(6, d))

def fib_efficient(n, d):
    global numFibCalled
    numFibCalled += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2,d)
        d[n]=ans
        return ans

d = {1:1, 2:2}
print(fib_efficient(6, d))