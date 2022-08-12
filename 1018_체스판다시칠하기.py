n,m = map(int,input().split())

chess_box = []

# n,m을 통한 체스판 만들기
for j in range(n) :
    line = []
    w_b = input()
    for char in w_b :
        line.append(char)
    chess_box.append(line)

# 완성된 체스판 확인
#print(chess_box)
#print(chess_box[0][1])

# 체스판 8x8 필터로 확인하면서 w,b 개수가 각각 32개에 근접한 위치 확인
# w,b의 개수는 다른 리스트에 넣어서 저장
w_count = 0
b_count = 0
save_list = []
save = []

# 8x8 필터
for j in range(n-7) :
    for i in range(m-7) :
        for p2 in range(8) :
            line_list = []
            for p in range(8) :
                if chess_box[j+p2][i+p] == "W" :
                    w_count += 1
                elif chess_box[j+p2][i+p] == "B" :
                    b_count += 1
                #print(chess_box[j+p2][i+p])
                line_list.append(chess_box[j+p2][i+p])
            save_list.append(line_list)
        
        # 각 필터마다 체스판과 부족한 칸의 개수를 저장해야됨
        save_list.append(b_count)
        save_list.append(w_count)
        save.append(save_list)
        
        save_list = []
        w_count = 0
        b_count = 0

#print(save)    

# w,b가 번갈아 나오는지 확인 번갈아 안나왔을때 카운트 => 카운트가 가장 적은것을 출력 (인덱스 list[::2])

min = 1000
for i in save :
    #print(i[-1],i[-2])
    # w,b 비교해서 32와 가장 가까운 숫자를 찾음
    if i[-1] > i[-2] :
        if min >= abs(32 - i[-1]) :
            min = abs(32 - i[-1])
    elif i[-1] < i[-2] :
        if min >= abs(32 - i[-2]) :
            min = abs(32 - i[-2])
    else :
        min = 0
print(min)