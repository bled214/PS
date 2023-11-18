"""
백준 단어정렬
https://www.acmicpc.net/problem/1181
"""

import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    words.append(input().rstrip())
words = list(set(words))

words.sort()
words.sort(key=lambda x:len(x))

for word in words:
    print(word)

