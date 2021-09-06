import sys

sys.stdin = open('input.txt')

T = int(input())

sum_up = 0

for test_case in range(1, T + 1):
    temp = list(map(int, input().split()))
    for sector in temp:
        if (sector % 2) ==1:
            sum_up = sum_up + sector

        else:
            sum_up = sum_up
    print(f'#{test_case} {sum_up}')
    sum_up = 0