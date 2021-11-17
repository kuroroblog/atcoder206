# 標準入力を受け付ける。
N = int(input())

# ⌊x⌋はx以下の最大の整数 ⏩ 小数点以下は切り捨てる。
# 参考 : https://note.nkmk.me/python-math-floor-ceil-int/
price = int(1.08 * N)

if price < 206:
    print('Yay!')
elif price == 206:
    print('so-so')
else:
    print(':(')
