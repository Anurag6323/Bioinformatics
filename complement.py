def complement(seq):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    new_seq=""
    for base in seq:
        new_seq = ''.join(complement_dict[base] for base in seq)
    print("Complementary Strand (3' to 5'): ",new_seq)
    print("Complementary Reversed Strand (5' to 3'): ",new_seq[::-1])

s1="CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCATTG"
complement(s1)