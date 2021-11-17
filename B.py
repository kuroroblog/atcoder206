# 標準入力を受け付ける。
N = int(input())

# 貯金日数を管理する変数
day_cnt = 0
# 貯金額を管理する変数
sum_money = 0

# 貯金額がN以上になるまでwhile文を回す。
while sum_money < N:
    # 貯金日数を+1する。
    day_cnt += 1
    # 貯金額を貯金日数分、足し合わせる。
    sum_money += day_cnt

print(day_cnt)
