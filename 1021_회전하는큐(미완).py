from collections import deque

n,m=map(int,input().split())  # 큐의 크기 : n, 뽑아내려는 수의 개수: m

d = deque(range(1,n+1))

print(d)
