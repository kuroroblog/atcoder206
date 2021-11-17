# 参考 : https://note.nkmk.me/python-collections-counter/
import collections

# 標準入力を受け付ける。
N = int(input())
A = list(map(int, input().split()))

# 配列内に含まれる整数の重複数を、各整数ごとにカウントする。
# 参考 : https://note.nkmk.me/python-collections-counter/
c = collections.Counter(A)

i = N
ans = 0
# 参考 : https://note.nkmk.me/python-collections-counter/
for item in c.items():
    # 整数
    num = item[0]
    # 整数の重複数
    duplicate_num = item[1]

    # 整数(num変数)と重複していない、残りの配列の数を洗い出す。
    i -= duplicate_num
    # 整数(num変数)に関する整数組の数を演算する。
    ans += duplicate_num * i

print(ans)
