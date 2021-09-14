import sys
sys.stdin=open('sample_input.txt')
case_num = int(input()) # test Case 받아오는것.
now_pos = 0 #현재 위치 변수 설정
refill_gas = 0 #충전 횟수 변수 설정

for m in range(case_num): #각 test Case 별 구문
    size_move, size_stop, size_charge = list(map(int, input().split()))
     #Size Move = 충전 한번에 움직일 수 있는 정류장 수
     #Size _Stop = 노선의 총 정류장 수
     # Size Charge = 노선 내 충전소 갯수
    fuel_tank = int(size_move) #Fuel tank는 버스의 남은 연료 표기
    pos_charge = list(map(int, input().split()))
    #Pos_charge는 정류장의 위치
    charge_stop = [True]*(size_stop+1)
    # Null list 를 만들줄 몰라서, 억지로 1by 10짜리 Array를 만든거임.
    # print(f'size_move : {size_move}') #표기용
    # print(f'size_stop : {size_stop}') #표기용
    # print(f'size_charge : {size_charge}') #표기용
    # print(f'pos_charge : {pos_charge}') #표기용

    for j in pos_charge:
        charge_stop[j] = True # 충전소 위치를 True로 표기하기로함.
    # print(charge_stop)
    for k in range(size_stop+1):
        now_pos = now_pos + 1
        fuel_tank = fuel_tank - 1
        # print(f'now we are in {k+1}')
        print(f'now we have {fuel_tank} more gases')
        determinant = []

        if k+1 < size_stop and charge_stop[k+1] == True:
            for temp_search in range(fuel_tank):
                if charge_stop[k+1+temp_search+1] == True:
                    determinant.append(1)
                else:
                    determinant.append(0)

            # print(f'it is determinant {determinant}')
            # print(f'it is sumf of determinant {sum(determinant)}')

            if sum(determinant)>0:
                refill_gas = refill_gas
                fuel_tank = fuel_tank
                determinant = []
                # print(refill_gas)
            else:
                refill_gas = refill_gas + 1
                print(f'Refilled gas')
                fuel_tank = size_move
                determinant = []
                # print(refill_gas)
        else:
            refill_gas = refill_gas
            fuel_tank = fuel_tank
            determinant = []
            # print(refill_gas)

    print(refill_gas)
    fuel_tank = size_move
    refill_gas=0