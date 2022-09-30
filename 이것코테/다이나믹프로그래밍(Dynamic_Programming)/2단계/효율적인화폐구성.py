# 10:58~
# 9:10~

# n : 화폐 종류
# m : 최종적으로 만드려는 금액의 합
    # 화폐의 개수는 상관없음
    # 순서만 다른 것은 같은 경우로 구분
n, m = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

# dp 테이블
# 최종적으로 만드려는 가치의 합의 최댓값이 10000이므로, 해당 금액을 만들 수 있는 화폐 구성이 가능하지 않다는 의미로 10001로 초기값 설정
d = [10001] * (m+1)
# 중요 - 0원의 경우에는 화폐를 하나도 사용하지 않았을 때 만들 수 있으므로 0으로 설정
d[0] = 0

# 중요 - 화폐 종류 만큼 반복하면서 (화폐 종류 금액이 아니라 화폐 종류 부터 반복)
for i in range(n):
    # 현재 화폐 종류 금액 부터 최종적으로 만드려는 금액까지 반복하면서
    for j in range(coins[i], m + 1):
        # (i-k)원을 만드는 방법이 존재하는 경우 , ex) 현재 최소횟수를 찾으려는 값이 5원 이고 화폐 종류가 2,3원일 때 (5-2)를 만드는방법이 존재하는 경우
        if d[j - coins[i]] != 10001 :
            # 점화식, 둘중에 최소 횟수구하기(현재까지 저장된 최소 횟수 or 이전 동전까지의 최소횟수 + 1)
            # +1 하는 이유는 이전 동전횟수에 동전을 더하는 거니까 횟수 하나 더하는것
            d[j] = min(d[j], d[j - coins[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    # dp테이블의 해당금액 인덱스에는 해당금액을 만들기 위한 최소 횟수가 보장되어 있으므로 출력
    print(d[m])