import numpy as np
def smith_w(seq1, seq2):
    match = 2
    mismatch = -1
    penalty = -2
    n_rows = len(seq1) + 1
    n_cols = len(seq2) + 1

    # Initialize the scoring matrix
    score_matrix = np.zeros((n_rows, n_cols), dtype=int)
    max_score = 0
    max_pos = None

    # Fill in the matrix
    for i in range(1, n_rows):
        for j in range(1, n_cols):
            if seq1[i - 1] == seq2[j - 1]:
                diag_s = score_matrix[i - 1][j - 1] + match
            else:
                diag_s = score_matrix[i - 1][j - 1] + mismatch

            up_s = score_matrix[i - 1][j] + penalty
            left_s = score_matrix[i][j - 1] + penalty
            score = max(0, diag_s, up_s, left_s)

            score_matrix[i][j] = score

            if score > max_score:
                max_score = score
                max_pos = (i, j)

    # Highest score search
    align1, align2 = "", ""
    i, j = max_pos

    while score_matrix[i][j] != 0:
        current_score = score_matrix[i][j]

        if i > 0 and j > 0 and \
           current_score == score_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif i > 0 and current_score == score_matrix[i - 1][j] + penalty:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    return score_matrix, align1, align2

seq1 = "ACGTATCGCGTATA"
seq2 = "GATGCGTATCG"
score_matrix_sw, alignment1, alignment2 = smith_w(seq1, seq2)

print("Scoring Matrix:")
print(score_matrix_sw)
print("\nAlignment:")
print(alignment1)
print(alignment2)
