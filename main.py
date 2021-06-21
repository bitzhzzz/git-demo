import cv2
from functools import reduce

num = [1, 2, 3, 4, 5, 6]
s = ('A', 'B', 'C', 'D')
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
z = set([1, 2, 3, 4])
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(s):
    def float2num(s):
        return digits[s]

    def fn(x, y):
        return x*10+y

    for i in range(len(s)):
        if s[i] == '.':
            break
    I = [x for x in s if x != '.']

    r = reduce(fn, map(float2num, I))
    return r/10**i


img = cv2.imread('D:/aaa.jpg')
cv2.imshow('FRAME', img)
cv2.waitKey(0)
cv2.destroyAllWindows()





    

















