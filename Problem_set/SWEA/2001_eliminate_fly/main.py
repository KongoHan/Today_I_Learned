import sys
sys.stdin=open('input.txt')

case_num = int(input())
# print(case_num)

for each_case in range(case_num):
    size_map, size_bat = list(map(int,input().split()))
    init_mat = []
    for i in range(size_map):
        temp = list(map(int,input().split()))
        init_mat.append(temp)
    total_map = init_mat
    # print(total_map)

    total_bat = []
    temp_total_bat_1 = (0)
    for init_x in range(size_map-size_bat+1):
        for init_y in range(size_map-size_bat+1):
            for pox_x in range(size_bat):
                for pox_y in range(size_bat):
                    total_bat.append(total_map[pox_x+init_x][pox_y+init_y])
            # print(sum(total_bat))
            temp_total_bat_1 = max(sum(total_bat),temp_total_bat_1)
            # print(temp_total_bat_1)
            total_bat = []
    print(f'#{each_case+1} {temp_total_bat_1}')
    temp_total_bat_1=0