#9:55 ~
# 가로 N * 세로 2인 직사각형 바닥을 3종류 덮개를 이용해 채우는 문제
# 덮개 종류 : 2(가로) x 1(세로) , 1 x 2, 2 x 2

n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍 진행(Bottom-Up 방식)
d[1] = 1 # i - 1 까지 채워져 있을 때 1(가로) x 2(세로) 의 덮개를 채우는 1가지 방법밖에 없음
d[2] = 3 # i - 2 까지 채워져 있을 때는 3가지 방법 가능
for i in range(3, n+1):
    #점화식 표현 ; a[i] = a[i-1] + a[i-2] * 2
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(d[n])


