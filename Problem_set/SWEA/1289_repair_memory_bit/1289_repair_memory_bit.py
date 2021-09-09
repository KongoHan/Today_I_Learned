import  sys
sys.stdin = open('input.txt')
T_num = int(input())
for repeat in range(T_num):
    switch=0
    init_val=0
    T_list = list(map(int,input()))

    if init_val != T_list[0] :
        switch = switch+1
    else :
        switch = switch

    for sector in range(0,len(T_list)-1):
        if T_list[sector] != T_list[sector+1]:
            switch = switch+1
        else :
            switch = switch
    print(f'#{repeat+1} {switch}')