# https://atcoder.jp/contests/abc188/tasks/abc188_a
# Three-Point Shot
X, Y = map(int, input().split())
if abs(X-Y) < 3:
    print("Yes")
else:
    print("No")
