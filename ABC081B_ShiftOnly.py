import sys
# 再帰回数上弦を100000回に設定
sys.setrecursionlimit(100000)

n = input()
a = input()
an = a.split()

class info:
    count = 0
    index = 0

def divJudge(an_result):
    info.index = 0
    for i in an:
        if (int)(i) % 2 == 0:
            an_result[info.index] = (int)(i) / 2
        else:
            return
        info.index += 1
    divJudge(an_result)
    info.count += 1

divJudge(an)
print(info.count)
