seq1 = 'AATCTATA'
seq2 = 'AAG--ATA'
match_score = 1
origination_penalty = -2
mismatch_score = 0
gap_penalty = -1
score = 0 

is_gap = False
for char1, char2 in zip(seq1, seq2):
    if char1 == '-' or char2 == '-':
        if not is_gap:
            score += origination_penalty
            is_gap = True
        score += gap_penalty
    elif char1 == char2:
        is_gap = False
        score += match_score
    else:
        is_gap = False
        score += mismatch_score

print(score)
