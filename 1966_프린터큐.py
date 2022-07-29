class List_Q:
    def __init__(self) :
        self.queue = []
    def push(self,n) :
        return self.queue.append(n)
    def pop(self) :
        if len(self.queue) == 0 :
            pass 
        else :
            return self.queue.pop(0)
    def print_q(self):
        print(self.queue)

for i in range(int(input())) :
    a = List_Q()
    b = List_Q()
    c = 0
    t = True

    n,m = map(int,input().split())
    b.queue = list(range(n))

    for i in list(map(int,input().split())) :
        a.push(i)
    
    while t == True :
        if a.queue[0] == max(a.queue) : # 첫번째 인덱스가 최대 값 일때 최대값을 빼버림
            a.pop()
            b.pop()
            if m not in b.queue :
                print(c+1)
                t =False
            c+=1
        else : # 뒤에 큰 수가 있으면 앞에 원소를 뒤로 보냄
            a.push(a.pop())
            b.push(b.pop())