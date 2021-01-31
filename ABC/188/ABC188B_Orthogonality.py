# https://atcoder.jp/contests/abc188/tasks/abc188_b
# Orthogonality
N = int(input())
An = input().split()
Bn = input().split()
sum = 0

for i in range(N):
    sum += int(An[i]) * int(Bn[i])
if sum==0:
    print('Yes')
else:
    print('No')
