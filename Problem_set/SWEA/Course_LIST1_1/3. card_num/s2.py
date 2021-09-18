import sys

sys.stdin = open('sample_input.txt')

case_num = int(input())
temporary_directory_list = []
determinant = []
for m in range(case_num):
    exp_num = int(input())
    temporary_directory_list = list(input())
    for n in range(0,10):
        determinant.append(temporary_directory_list.count(f'{n}'))
    print(f'#{m+1} {len(determinant)-determinant[::-1].index(max(determinant))-1} {max(determinant)}')
    determinant = []
    temporary_directory_list = []