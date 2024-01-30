def computeJoinPoint(s1, s2):
    while s1 != s2:
        if s1 < s2:
            s1 += sum(int(digit) for digit in str(s1))
        else:
            s2 += sum(int(digit) for digit in str(s2))
    return s1
