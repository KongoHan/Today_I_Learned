import sys

sys.stdin = open('input.txt')

T = int(input())

cal_avg = 0

for test_case in range(1, T + 1):
    temp = list(map(int, input().split()))
    for sector in temp:
        cal_avg = cal_avg+sector
    cal_avg= cal_avg/len(temp)
    print(f'#{test_case} {round(cal_avg)}')
    cal_avg = 0