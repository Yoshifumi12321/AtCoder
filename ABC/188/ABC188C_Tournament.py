# https://atcoder.jp/contests/abc188/tasks/abc188_c
# Tournament
# 未完成

N = int(input())
A = list(map(int, input().split()))
index = []

i = 0
while True:
    if A[i] > A[i+1]:
        index.append(i)
    else:
        index.append(i+1)
    i += 2
