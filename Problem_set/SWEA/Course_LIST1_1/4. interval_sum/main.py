import sys
sys.stdin = open('sample_input.txt')

test_case = int(input())
for case_order in range(test_case):
    size_N , size_M = list(map(int,input().split()))
    array_N = list(map(int,input().split()))
    determinant_max=0
    determinant_min = sum(array_N)
    for now_position in range(size_N-size_M+1):
        determinant_max=(max(sum(array_N[now_position:now_position+size_M]),determinant_max))
        determinant_min=(min(sum(array_N[now_position:now_position + size_M]),determinant_min))
    print(f'#{case_order+1} {determinant_max-determinant_min}')

