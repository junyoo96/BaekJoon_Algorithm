#https://programmers.co.kr/learn/courses/30/lessons/42584
#아이디어 시간 8:20~8:35
#구현 시간 : 8:35~9:00

#처음 풀이 
def solution(prices):
    answer = []
    
    for i in range(len(prices)-1):
        cnt=0
        for j in range(i+1,len(prices)):
            cnt+=1
            if prices[i]>prices[j]:
                break
        answer.append(cnt)
    
    answer.append(0)
    
    return answer
  
#비슷한 풀이 중 깔끔한 코드
def solution(prices):
  answer = [0] * len(prices)
  for i in range(len(prices)):
      for j in range(i+1, len(prices)):
          if prices[i] <= prices[j]:
              answer[i] += 1
          else:
              answer[i] += 1
              break
  return answer
  
#베스트 코드
  #dequeue 사용
   
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer
  
  
  
  
  
