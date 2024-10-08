#   [1, 4, 8, 9]
def toAbs(L):
    for i in range(len(L)):
        testList[i] = abs(testList[i])

#   [2, -3, 9, -8]
def probTwo(L):
    for i in range(len(L)):
        if i%2 ==0 :
            testList[i] = testList[i]+1
        else:
            testList[i] = (testList[i]-1)*-1


#   [1, 16, 64, 81]

testList = [1, 4, 8, 9]
probTwo(testList)
print(testList)