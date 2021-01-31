N, S, D = map(int,input().split())
damage = []
for _ in range(N):
    X, Y = map(int, input().split())
    flag = False
    if X < S:
        if Y > D:
            flag = True

    damage.append(flag)

if sum(damage) > 0:
    print('Yes')
else:
    print('No')
