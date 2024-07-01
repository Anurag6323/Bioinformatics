def search_dna(sequence, search_strings):
    matches = {string: [] for string in search_strings}
    for string in search_strings:
        start = 0
        while start < len(sequence):
            index = sequence.find(string, start)
            if index == -1:
                break
            matches[string].append(index)
            start = index + 1
    return matches

dna_sequence = "GACATTGTGAACAGTAAAAAAGTCCATGCAATGCGCAAGGAGCAGAAGAGGAAGCAGGGCAAGCAGCGCTCCATGGGCTCTCCCATGGACTACTCTCCTCTGCCCATCGACAAGCATGAGCCTGAATTTGGTCCATGCAGAAGAAAACTGGATGGG"

search_strings = ['AAG', 'GTC', 'GAG', 'ACTA', 'ATAT']

matches = search_dna(dna_sequence, search_strings)

for string in search_strings:
    print(f"String searched: {string}")
    print(f"Total matches: {len(matches[string])}")
    print(f"Position of the matches: {matches[string]}"+'\n')
