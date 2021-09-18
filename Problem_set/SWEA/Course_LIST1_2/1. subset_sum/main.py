import sys
sys.stdin = open('sample_input.txt')
test_case = int(input())
field_size = 10
empty_field =[[0 for _ in range(field_size)] for _ in range(field_size)]

for case in range(test_case):
    mat_num = int(input())
    for num in range(mat_num):
        position_information = list(map(int,input().split()))
        if position_information[4] == 1:
            for row in range(position_information[2]-position_information[0]+1):
                for col in range(position_information[3]-position_information[1]+1):
                    empty_field[position_information[0]+row][position_information[1]+col]\
                        =empty_field[position_information[0]+row][position_information[1]+col]+1
        else:
            for row in range(position_information[2] - position_information[0] + 1):
                for col in range(position_information[3] - position_information[1] + 1):
                    empty_field[position_information[0] + row][position_information[1] + col] = \
                    empty_field[position_information[0] + row][position_information[1] + col] + 2
    print(f'#{case+1} {sum(sector.count(3) for sector in empty_field)}')
    empty_field = [[0 for _ in range(field_size)] for _ in range(field_size)]