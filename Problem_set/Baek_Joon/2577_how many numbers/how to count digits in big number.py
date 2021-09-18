import sys

sys.stdin = open('input.txt')

T=1
for numbers in range(3):
    T = T*int(input())

T_string=str(T)
T_map = map(int,T_string)
T_list = list(T_map)
# print(T_list) #just checking for how does it works in the middle of code.

for digits in range(0,9):
    print((T_list.count(digits)))