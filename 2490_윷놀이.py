for _ in range(3) :

    z_list = list(map(int,input().split()))

    if z_list.count(0) == 1:
        print("A")
    elif z_list.count(0) == 2:
        print("B")
    elif z_list.count(0) == 3:
        print("C")
    elif z_list.count(0) == 4:
        print("D")
    elif z_list.count(0) == 0:
        print("E")