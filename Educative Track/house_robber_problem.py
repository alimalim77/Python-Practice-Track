from sys import prefix


def houserobber(amount):
    dp = [float("inf")] * (amount+1)
    dp[0] = 0
    for i in range(1,amount+1):
        if i == 1:
            dp[i] = 1
        if 2 <= i < 5:
            dp[i] = min(dp[i-2]+1,dp[i-1] + 1)
        else:
            dp[i] = min(dp[i-1] + 1,dp[i-2]+1, dp[i-5]+1)
    print(dp)
    return dp[-1]


print(houserobber(11))
