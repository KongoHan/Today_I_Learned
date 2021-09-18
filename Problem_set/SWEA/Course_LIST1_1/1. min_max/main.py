import sys
sys.stdin = open('sample_input.txt')

case_num = int(input())
num_in_set = 0
temp_mat = []
for test in range(case_num):
    num_in_set = int(input())
    temp_mat = list(map(int,input().split()))
    temp_max = temp_mat[0]
    temp_min = temp_mat[0]
    for i in range(len(temp_mat)):
        temp_max = max(temp_mat[i],temp_max)
        temp_min = min(temp_mat[i],temp_min)

    print(f'#{test+1} {temp_max-temp_min}')




