import numpy as np

def needleman(seq1, seq2, match_s, mismatch_s, penalty):
    rows, cols = len(seq1) + 1, len(seq2) + 1
    matrix = np.zeros((rows, cols), dtype=int)


    for i in range(rows):
        matrix[i][0] = i * penalty
    for j in range(cols):
        matrix[0][j] = j * penalty

 
    for i in range(1, rows):
        for j in range(1, cols):
            if seq1[i - 1] == seq2[j - 1]:
                diag_s = matrix[i - 1][j - 1] + match_s
            else:
                diag_s = matrix[i - 1][j - 1] + mismatch_s
            
            up_s = matrix[i - 1][j] + penalty
            left_s = matrix[i][j - 1] + penalty

            matrix[i][j] = max(diag_s, up_s, left_s)


    align1, align2 = "", ""
    i, j = len(seq1), len(seq2)

    while i > 0 or j > 0:
        current_s = matrix[i][j]

        if i > 0 and j > 0 and \
           current_s == matrix[i - 1][j - 1] + (match_s if seq1[i - 1] == seq2[j - 1] else mismatch_s):
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif i > 0 and current_s == matrix[i - 1][j] + penalty:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    return matrix, align1, align2

seq1 = "ACAGTCGAACG"
seq2 = "ACCGTCCG"
match_s = 2
mismatch_s = -1
penalty = -2

matrix, alignment1, alignment2 = needleman(seq1, seq2, match_s, mismatch_s, penalty)
print("Score Matrix:\n", matrix)
print("Alignment:\n", alignment1, "\n", alignment2)
