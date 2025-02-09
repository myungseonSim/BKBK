import sys
input = sys.stdin.readline

N = int(input())

first_row = list(map(int, input().split()))
max_dp = first_row[:]
min_dp = first_row[:]

for _ in range(N - 1):
    row = list(map(int, input().split()))

    new_max_dp = [
        row[0] + max(max_dp[0], max_dp[1]),  
        row[1] + max(max_dp[0], max_dp[1], max_dp[2]),  
        row[2] + max(max_dp[1], max_dp[2])  
    ]

    new_min_dp = [
        row[0] + min(min_dp[0], min_dp[1]),
        row[1] + min(min_dp[0], min_dp[1], min_dp[2]),
        row[2] + min(min_dp[1], min_dp[2])
    ]

    max_dp = new_max_dp
    min_dp = new_min_dp

print(max(max_dp), min(min_dp))
