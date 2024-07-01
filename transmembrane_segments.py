import matplotlib.pyplot as plt

hydrophobicity_values = {
    "A": 13.85, "D": 11.61, "C": 15.37, "E": 11.38, "F": 13.93,
    "G": 13.34, "H": 13.82, "I": 15.28, "K": 11.58, "L": 14.13,
    "M": 13.86, "N": 13.02, "P": 12.35, "Q": 12.61, "R": 13.10,
    "S": 13.39, "T": 12.70, "V": 14.56, "W": 15.48, "Y": 13.88
}

def plot_hydrophobicity_profile(sequence, window_length):
    hydrophobicity_profile = []
    for i in range(len(sequence) - window_length + 1):
        window = sequence[i:i+window_length]
        window_hydrophobicity = sum(hydrophobicity_values.get(aa, 0) for aa in window) / window_length
        hydrophobicity_profile.append(window_hydrophobicity)
    

    plt.plot(range(len(sequence) - window_length + 1), hydrophobicity_profile)
    plt.xlabel('Position')
    plt.ylabel('Average Hydrophobicity')
    plt.title(f'Hydrophobicity Profile (Window Length {window_length})')
    plt.show()

# Threshold value set to 14.0
def find_transmembrane_segments(sequence, window_length, threshold=14.0):
    transmembrane_segments = []
    for i in range(len(sequence) - window_length + 1):
        window = sequence[i:i+window_length]
        window_hydrophobicity = sum(hydrophobicity_values.get(aa, 0) for aa in window) / window_length
        if window_hydrophobicity >= threshold:
            transmembrane_segments.append((i, i+window_length-1))
    return transmembrane_segments

sequence = "ALLSFERKYRVRGGTLIGGDLFDFWVGPYFVGFFGVSAIFFIFLGVSLIGYAASQGPTWDPFAISINPPDLKYGLGAAPLLEGGFWQAITVCALGAFISWMLREVEISRKLGIGWHVPLAFCVPIFMFCVLQVFRPLLLGSWGHAFPYGILSHLDWVNNFGYQYLNWHYNPGHMSSVSFLFVNAMALGLHGGLILSVANPGDGDKVKTAEHENQYFRDVVGYSIGALSIHRLGLFLASNIFLTGAFGTIASGPFWTRGWPEWWGWWLDIPFWS"

# Plot hydrophobicity profiles for window lengths 9 and 19
plot_hydrophobicity_profile(sequence, 9)
plot_hydrophobicity_profile(sequence, 19)

# Find transmembrane segments using window length
transmembrane_segments = find_transmembrane_segments(sequence, 9)
print("Transmembrane segments (Window Length 9):", transmembrane_segments)
transmembrane_segments = find_transmembrane_segments(sequence, 19)
print("\n Transmembrane segments (Window Length 19):", transmembrane_segments)
