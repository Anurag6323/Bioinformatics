def find_common_subsequence(a, b):
    common_subsequence = ''
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i:].startswith(b[j:]) or b[j:].startswith(a[i:]):
                start = i
                while i < len(a) and j < len(b) and a[i] == b[j]:
                    i += 1
                    j += 1
                if len(common_subsequence) < i - start:
                    common_subsequence = a[start:i]
                i = start
    return common_subsequence

def identify_secondary_structures(sequence):
    alpha_helix_rules = {'A': 'Ha', 'C': 'ia', 'D': 'ia', 'E': 'Ha', 'F': 'ha',
                         'G': 'Ba', 'H': 'ha', 'I': 'Ia', 'K': 'Ia', 'L': 'Ha',
                         'M': 'ha', 'N': 'ba', 'P': 'Ba', 'Q': 'ha', 'R': 'ia',
                         'S': 'ia', 'T': 'ia', 'V': 'ha', 'W': 'ha', 'Y': 'ba'}
    beta_strand_rules = {'A': 'Ib', 'C': 'hb', 'D': 'ib', 'E': 'Bb', 'F': 'hb',
                          'G': 'ib', 'H': 'bb', 'I': 'Hb', 'K': 'bb', 'L': 'hb',
                          'M': 'Hb', 'N': 'bb', 'P': 'bb', 'Q': 'hb', 'R': 'ib',
                          'S': 'bb', 'T': 'hb', 'V': 'Hb', 'W': 'hb', 'Y': 'hb'}
    alpha_helix_propensity = {'A': 1.45, 'C': 0.77, 'D': 0.98, 'E': 1.53, 'F': 1.12,
                               'G': 0.53, 'H': 1.24, 'I': 1.00, 'K': 1.07, 'L': 1.34,
                               'M': 1.20, 'N': 0.73, 'P': 0.59, 'Q': 1.17, 'R': 0.79,
                               'S': 0.79, 'T': 0.82, 'V': 1.14, 'W': 1.14, 'Y': 0.61}
    beta_strand_propensity = {'A': 0.97, 'C': 1.30, 'D': 0.80, 'E': 0.26, 'F': 1.28,
                                'G': 0.81, 'H': 0.71, 'I': 1.60, 'K': 0.74, 'L': 1.22,
                                'M': 1.67, 'N': 0.65, 'P': 0.62, 'Q': 1.23, 'R': 0.90,
                                'S': 0.72, 'T': 1.20, 'V': 1.65, 'W': 1.19, 'Y': 1.29}
    secondary_structure_coefficients = {'Ha': 1, 'ha': 1, 'Ia': 0.5, 'ia': 0, 'ba': -1, 'Ba': -1,
                                        'Hb': 1, 'hb': 1, 'Ib': 0.5, 'ib': 0, 'bb': -1, 'Bb': -1}

    alpha_helices = []
    beta_strands = []

    print('\nAlpha Helices:')
    i = 0
    while i < len(sequence) - 6:
        total_score = 0
        for j in range(6):
            total_score += secondary_structure_coefficients[alpha_helix_rules[sequence[i:i+6][j]]]
        if total_score >= 4:
            done = 1
            k = 0
            while done == 1:
                next_segment = sequence[i+k+2:i+k+6]
                score = 0
                for l in range(4):
                    score += alpha_helix_propensity[next_segment[l]]
                if score < 4.00:
                    done = 0
                else:
                    k += 1
            if k == 0:
                print(f'Helix - {sequence[i:i + k + 6]}')
                alpha_helices.append(sequence[i:i + k + 6])
                i = i + k + 6
            else:
                print(f'Helix - {sequence[i:i + k + 5]}')
                alpha_helices.append(sequence[i:i + k + 5])
                i = i + k + 5
        else:
            i += 1

    print('\nBeta Strands:')
    i1 = 0
    while i1 < len(sequence) - 5:
        total_score = 0
        for j in range(5):
            total_score += secondary_structure_coefficients[beta_strand_rules[sequence[i1:i1+5][j]]]
        if total_score >= 3:
            done = 1
            k = 0
            while done == 1 and (i1+k+5) <= len(sequence):
                next_segment = sequence[i1+k+2:i1+k+5]
                score = 0
                for l in range(3):
                    score += beta_strand_propensity[next_segment[l]]
                if score < 3.00:
                    done = 0
                else:
                    k += 1
            if k == 0:
                print(f'Strand - {sequence[i1:i1 + k + 5]}')
                beta_strands.append(sequence[i1:i1 + k + 5])
                i1 = i1 + k + 5
            else:
                print(f'Strand - {sequence[i1:i1 + k + 4]}')
                beta_strands.append(sequence[i1:i1 + k + 4])
                i1 = i1 + k + 4
        else:
            i1 += 1

    common_segments = []
    print('\nCommon segments: ')
    for helix_segment in alpha_helices:
        for strand_segment in beta_strands:
            common = find_common_subsequence(helix_segment, strand_segment)
            length = len(common)
            if length != 0 and length >= 5:
                print(f'Helix - {helix_segment}, Strand - {strand_segment}, Common segment - {common}')
                prop_helix = sum(alpha_helix_propensity[aa] for aa in common)
                prop_strand = sum(beta_strand_propensity[aa] for aa in common)
                if prop_helix > prop_strand:
                    common_segments.append([strand_segment, helix_segment])
                else:
                    common_segments.append([helix_segment, strand_segment])

    for item in common_segments:
        if item[0] in beta_strands:
            beta_strands.remove(item[0])
        if item[1] in alpha_helices:
            alpha_helices.remove(item[1])

    print('\nConfirmed structures after comparing:')
    print('Alpha Helix segments:')
    for helix in alpha_helices:
        print(helix)
    print('\nBeta Strand segments:')
    for strand in beta_strands:
        print(strand)

sequence = "KVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQATNRNTDGSTDYGILQINSRWWCNDGRTPGSRNLCNIPCSALLSSDITASVNC"
identify_secondary_structures(sequence)
