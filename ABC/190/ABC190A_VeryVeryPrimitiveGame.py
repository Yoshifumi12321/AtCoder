# https://atcoder.jp/contests/abc190/tasks/abc190_a
# Very Very Primitive Game

A, B, C = map(int, input().split())

if A == B:
    if C == 1:
        print('Takahashi')
    else:
        print('Aoki')
elif A>B:
    print('Takahashi')
elif A<B:
    print('Aoki')
