def longest_common_subsequence(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    max_length = 0  # length of longest common subsequence
    end_pos = 0  # end position of longest common subsequence in seq1

    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos = i
            else:
                dp[i][j] = 0

    return seq1[end_pos - max_length : end_pos]

# Test the function
seq1 = "MLRLL"
seq2 = "MQPILLLV"
print("Longest Common Subsequence: ", longest_common_subsequence(seq1, seq2))
