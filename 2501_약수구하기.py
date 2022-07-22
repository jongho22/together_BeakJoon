#자연수 => N 의 약수 중에서 K 번째로 작은수          
n,k = map(int,input().split())

l =[]

for i in range(1,n+1) :
    yaksu = n % i
    if yaksu == 0 : # 약수이면 리스트에 저장
        l.append(i)

if not l : # 리스트에 아무것도 없는지 확인
    print(0)
else :  
    l.sort()  # 리스트 오름차순 정렬
    if len(l) < k : # 리스트 원소 총 개수보다 숫자 K가 더 클면 0 출력
        print(0)
    else :
        print(l[k-1])  # 안크면 정상적으로 출력