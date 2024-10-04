def isPalindrome(s):
    def isChar(s):
        palinStr = ''
        s = s.lower()
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                palinStr += c
        return palinStr

    def isPalin(str):
        if len(str) == 0 or len(str) == 1:
            return True
        else:
            return str[0] == str[-1] and isPalin(str[1:-1])
    return isPalin(isChar(s))

print(isPalindrome("abcde"))