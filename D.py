from collections import deque

################################
# <方針>
# 回文とは何かについて考える。
# 回文とは「前から読んでも後ろから読んでも同じ言葉、数字であるもの」を意味する。
# 例えば`13531`, `あいういあ`, `93244239`などが回文にあたる。
# 今回、回文を生成するために、組み合わせ(x, y)を選んで、現在Aに含まれるxをyに置換するが、まず置換しなくていい箇所を洗い出す。
# <置換しないていい箇所>
# ・奇数の場合、真ん中のA。(どんな値に置換されても回文になるため。)
# ・A[i]番目の数字とA[N - i + 1]番目の数字が等しい箇所。
# 上記の箇所以外を、最適に置換して回文を作ることを考える。
# <どのように置換していくのか?>
# ・A[i]番目の数字とA[N - i + 1]番目の数字どちらかを、もう片方の数字にすると最小の操作でうまくいく。 ⏩ A[i] 〜 A[N - i]間の無効グラフであると考える。
# ・無向グラフに対してDFS(深さ優先探索)を行う。
# ・DFS(深さ優先探索)とは? : https://qiita.com/drken/items/4a7869c5e304883f539b
# ・参考 : https://www.youtube.com/watch?v=Nd31ytkNrgQ
################################

# 標準入力を受け付ける。
N = int(input())
A = list(map(int, input().split()))

# 正整数列の最大値を格納する。
max_val = max(A) + 1

# 数値間情報(A[i]番目 〜 A[N - i])を格納する。
edges = []
for _ in range(max_val):
    edges.append([])

mid = N // 2
for i in range(0, mid):
    a = A[i]
    b = A[N - i - 1]
    # 異なる2数字の場合のみ、無向グラフの生成を行う。
    if a != b:
        edges[a].append(b)
        edges[b].append(a)

# A[i]番目へ訪れたかどうか表す、フラグ情報を格納する。
visited = [False] * (max_val)
ans = 0
for i in range(1, max_val):
    # 無向グラフがないA[i]番目に関しては考えない。
    if edges[i] == []:
        continue

    # 一度訪れた無向グラフに関しては考えない。
    if visited[i]:
        continue

    # 参考 : https://docs.python.org/ja/3/library/collections.html#collections.deque
    dq = deque([i])
    while len(dq) != 0:
        now = dq.pop()
        # 訪れたA[i]番目に関して、フラグをTrueへ変更する。
        visited[now] = True
        for to in edges[now]:
            if visited[to] == 1:
                continue
            visited[to] = True
            ans += 1
            dq.append(to)

print(ans)
