# Longest Common Subsequence using Dynamic Programming

X = input("Enter first sequence: ")
Y = input("Enter second sequence: ")

m = len(X)
n = len(Y)

# Create DP table
dp = [[0] * (n + 1) for _ in range(m + 1)]

# Fill the table
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if X[i - 1] == Y[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# Print LCS length
print("Length of LCS:", dp[m][n])

# Find the actual LCS
i = m
j = n
lcs = ""

while i > 0 and j > 0:
    if X[i - 1] == Y[j - 1]:
        lcs = X[i - 1] + lcs
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print("Longest Common Subsequence:", lcs)
