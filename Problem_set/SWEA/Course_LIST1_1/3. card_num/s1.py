import sys

sys.stdin = open('sample_input.txt')

case_num = int(input())
temporary_directory_list = []
determinant = []
for m in range(case_num):
    exp_num = int(input())
    temporary_directory_int = int(input())
    while temporary_directory_int!=0:
        temporary_directory_list.append(temporary_directory_int%10)
        temporary_directory_int=temporary_directory_int//10
    for n in range(10):
        determinant.append(temporary_directory_list.count(n))
    print(f'#{m+1} {determinant.index(max(determinant))} {max(determinant)}')
    determinant = []
    temporary_directory_list = []
