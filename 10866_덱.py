import sys
input = sys.stdin.readline

class m_deque :
    def __init__(self) :
        self.list_deque = []

    def push_front(self,n) :
        self.list_deque.insert(0,n)
        
    def push_back(self,n) :
        self.list_deque.append(n)
        
    def pop_front(self) :
        if len(self.list_deque) != 0 :
            return print(self.list_deque.pop(0))
        else :
            return print(-1)

    def pop_back(self) :
        if len(self.list_deque) != 0 :
            return print(self.list_deque.pop())
        else :
            return print(-1)

    def size(self) :
        return print(len(self.list_deque))

    def empty(self) :
        if len(self.list_deque) != 0 :
            return print(0)
        else :
            return print(1)
    def front(self) :
        if len(self.list_deque) != 0 :
            return print(self.list_deque[0])
        else :
            return print(-1)
    def back(self) :
        if len(self.list_deque) != 0 :
            return print(self.list_deque[len(self.list_deque)-1])
        else :
            return print(-1)

if __name__ == "__main__" :
    m_dq = m_deque()
    n = int(input())

    for i in range(n) :
        line = input().split()
        
        if line[0] == "push_back" :
            m_dq.push_back(line[1])
        elif line[0] == "push_front" :
            m_dq.push_front(line[1])  
        elif line[0] == "front" :
            m_dq.front()
        elif line[0] == "back" :
            m_dq.back()
        elif line[0] == "size" :
            m_dq.size()
        elif line[0] == "empty" :
            m_dq.empty()
        elif line[0] == "pop_front" :
            m_dq.pop_front()
        elif line[0] == "pop_back" :
            m_dq.pop_back()
        #print(m_dq.list_deque)
  