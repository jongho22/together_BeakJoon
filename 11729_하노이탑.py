n = int(input())

c = 2**n - 1
def hanoi(n,start_node,end_node,help_node) :
    
    if n == 1 :
        return print(start_node,end_node)
    # 중앙으로 옮기기
    hanoi(n-1,start_node,help_node,end_node)
    print(start_node,end_node)
    # 밑단 맨 뒤로 보내기
    hanoi(n-1,help_node,end_node,start_node)

print(c)  
hanoi(n,1,3,2)
    
