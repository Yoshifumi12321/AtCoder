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
