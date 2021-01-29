# https://atcoder.jp/contests/abc087/tasks/abc087_b
# Coins

# A, B, C, X = [int(input()) for i in range(4)]
# count = 0
#
# for a in range(A+1):
#     for b in range(B+1):
#         for c in range(C+1):
#             if 500*a+100*b+50*c == X:
#                 count += 1
#
# print(count)

#きれいな書き方
A, B, C, X = [int(input()) for i in range(4)]
print(sum(500*a+100*b+50*c == X for a in range(A+1) for b in range(B+1) for c in range(C+1)))
#リスト内表記を使い0からa,b,cそれぞれの場合の方程式の計算結果をXと比較し、Trueとなったものをsumを使って数える
