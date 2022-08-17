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
one_count = 0
two_count = 0
save_list = []
#save = []

# 8x8 필터
for j in range(n-7) :
    for i in range(m-7) :
        one_count = 0
        two_count = 0
        for p2 in range(8) :
            #ine_list = []
            for p in range(8) :
                if (p2+p)%2 == 0 :
                    if chess_box[j+p2][i+p] != "W" :
                        one_count += 1
                    elif chess_box[j+p2][i+p] != "B" :
                        two_count += 1
                else :
                    if chess_box[j+p2][i+p] != "B" :
                        one_count += 1
                    elif chess_box[j+p2][i+p] != "W" :
                        two_count += 1
                
                #print(chess_box[j+p2][i+p])
                #line_list.append(chess_box[j+p2][i+p])
        save_list.append(min(one_count,two_count))
print(min(save_list))     
    