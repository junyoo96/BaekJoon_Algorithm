# 9:10~ - 틀림
# 10:01~10:33/10:33~11:10

# 뱀
    # 벽이나 자기자신의 몸과 부딪히면 게임 끝
    # 맨왼쪽상단에 위치
    # 뱀 길이 1
    # 뱀 초기방향 오른쪽
    # 이동
        # 몸길이 늘려 머리 다음칸에 위치
        # 만약 이동한 칸에 사과가 있다면
            # 해당 칸에 사과가 없어지고 꼬리는 움직이지 않음
        # 만약 이동한 칸에 사과가 없다면
            # 몸길이를 줄여 꼬리가 위치한 칸 비우기
# n : 보드 크기
    # 보드의 상하좌우 끝에 벽 있음
    # 맨왼쪽상단(1,1)
# k : 사과 개수
# answer : 게임이 몇 초에 끝나는지 출력
#========================================================
# 내 코드
from collections import deque

# n 입력
n = int(input())
# k 입력
k = int(input())
# 사과만 저장할 격자 생성
apples = [[0] * n for _ in range(n)]
# k만큼 반복하면서
for _ in range(k):
    x, y = map(int, input().split())
    # 사과 위치 입력(위치 입력시 -1하기)
    apples[x - 1][y - 1] = 1

# 뱀의 방향 변환 횟수 입력
c = int(input())
# 회전 시간과 회전 방향 dictionary에 입력
rotation_info = {}
for _ in range(c):
    time, direction = input().split()
    rotation_info[int(time)] = direction

# 뱀 좌표(머리 앞, 꼬리 뒤) - deque
position = deque()
position.append((0, 0))
# 뱀 방향(1)
direction = 1
# 방향 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# answer 변수
answer = 0

# 이동 함수
def move():
    # 머리좌표에서 현재 방향으로 이동한 좌표 계산
    head_x, head_y = position[0]
    nx = head_x + dx[direction]
    ny = head_y + dy[direction]
    # 만약 이동한 좌표가 올바른 범위를 벗어났다면
    if not (0 <= nx < n and 0 <= ny < n):
        return False
    # 만약 이동한 좌표가 뱀 좌표안에 있다면
    if (nx, ny) in position:
        return False

    # 이동할 좌표를 뱀 좌표 deque의 맨앞에 추가
    position.appendleft((nx, ny))
    # 만약 이동할 좌표에 사과가 있다면
    if apples[nx][ny] == 1:
        # 사과 없애기
        apples[nx][ny] = 0
    # else
    else:
        # 뱀 좌표 deque의 맨 뒤 값 제거
        position.pop()

    return True

# while True
while True:
    # answer 증가
    answer += 1

    # 만약 이동 함수가 False라면
    if not move():
        break

    # 만약 현재 시간이 회전시간과 회전 방향 저장하는 dictionary에 있다면
    if answer in rotation_info:
        # 방향 변경
        if rotation_info[answer] == 'L':
            direction -= 1
        elif rotation_info[answer] == 'D':
            direction += 1

        if direction == -1:
            direction = 3
        elif direction == 4:
            direction = 0

# answer 출력
print(answer)

#=================================================
# 예시 답안

n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 뱀 머리 회전하는 함수
def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

# 게임 진행
def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction] # 이동한 뱀 머리 위치
        ny = y + dy[direction] # 이동한 뱀 머리 위치

        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면(뱀이 존재하는 곳은 2로 표시되고 있으니까)
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                # 뱀의 머리가 존재하는 위치 2로 표시
                data[nx][ny] = 2
                # 뱀이 차지하고 있는 위치 중 머리 위치 추가
                q.append((nx, ny))
                # 뱀이 차지하고 있는 위치 중 꼬리 위치 정보 제거
                px, py = q.pop(0)
                # 뱀의 꼬리가 존재하는 위치 0으로 표시
                data[px][py] = 0
            # 사과가 있다면
            if data[nx][ny] == 1:
                # 뱀 머리 위치만 추가하고 꼬리는 그대로 두기
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면(종료)
        else:
            time += 1
            break
        # 다음 위치로 머리를 이동
        x, y = nx, ny
        # 시간 증가
        time += 1
        # 회전할 시간인 경우 회전
        if index < l and time == info[index][0]:
            # 방향 회전하기
            direction = turn(direction, info[index][1])
            # 다음 회전 방향을 표시하기 위함
            index += 1
    return time

print(simulate())