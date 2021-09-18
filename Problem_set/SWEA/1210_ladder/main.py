import sys

sys.stdin = open('input.txt')

case_num = 10
mat_size = 100
case_number = int(input())
real_map = []
start_pos = [[0],[0]]
for m in range(mat_size):
    temp_mat = list(map(int,input().split()))
    for y in range(mat_size):
        real_map.append(temp_mat)
find_start_pt = []

for n in range(mat_size):
    if real_map [0][n]==1:
        find_start_pt.append(n)
    else:
        pass
print(find_start_pt)

for start in find_start_pt:
    start_pos [1][0] = start
    if #왼쪽을 비교

    else if : #우측을 비교

