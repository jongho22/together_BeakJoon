def pebo(n) : # 재귀함수를 이용한 피보나치 수열 구현
    if 0< n <= 2 :
        return 1
    elif n == 0 :
        return 0
    else :
        return pebo(n-1) + pebo(n-2)

print(pebo(int(input()))) # 숫자 입력 받고 출력