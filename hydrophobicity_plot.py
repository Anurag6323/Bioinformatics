import matplotlib.pyplot as plt

hydrophobicity_values = {
    "A": 13.85, "D": 11.61, 'C': 15.37, 'E': 11.38, 'F': 13.93,
    'G': 13.34, 'H': 13.82, 'I': 15.28, 'K': 11.58, 'L': 14.13,
    'M': 13.86, 'N': 13.02, 'P': 12.35, 'Q': 12.61, 'R': 13.10,
    'S': 13.39, 'T': 12.70, 'V': 14.56, 'W': 15.48, 'Y': 13.88
}

sequences = [
    "FDCAEYRSTNIYGYGLYEVSMKPAKNTGIVSSFFTYTGPAHGTQWEIDIEFLGKDTTKVQFNYYTNGVGGHEKVISLGFDASKGFHTYAFDWQPGYIKWYVDGVLK",
    "KASEDLVKKHAGVLGAILKKKGHHEAELKPLAQSHATKAHKNIFISEAIIHVLHSRHPGDFGADAQGAMNKALELFRKDIAAKYKELGY",
    "TVEGAGSIAAATGFVKKDQLGKNEEGAPQEGILEDMPVDPDNEAYEMPSEEGYQDYEPEA"
]

def plot_hydrophobicity_profile(sequence):
    x = list(range(len(sequence)))
    y = [hydrophobicity_values.get(aa, 0) for aa in sequence]
    plt.plot(x, y)
    plt.xlabel('Amino acid sequence')
    plt.ylabel('Hydrophobicity index')
    plt.title('Relationship between sequence position and hydrophobicity profile')

# Assuming threshold value to be 13.30 for identifying the secondary structure
def identify_beta_strands(sequence, threshold=13.30):
    beta_strands = []
    y = [hydrophobicity_values[i] for i in sequence]
    for i in range(0,len(sequence)-9):
        temp = [k for k in range(i,i+6,2) if y[k]>threshold]
        temp2 = [k for k in range(i+1,i+7,2) if y[k]<threshold]
        if len(temp)==len(temp2) and len(temp) >= 3:
            beta_strands.append((temp[0],temp2[-1]))
    return beta_strands

def identify_alpha_helices(sequence, threshold=13.30):
    alpha_helices = []
    y = [hydrophobicity_values[i] for i in sequence]
    for i in range(0, len(sequence)-7):
      if (y[i] < threshold and y[i+1] < threshold) and (y[i+2] > threshold and y[i+3] > threshold) and (y[i+4] < threshold and y[i+5] < threshold) and (y[i+6] > threshold and y[i+7] > threshold):
        alpha_helices.append((i,i+7))
      elif ((y[i] > threshold and y[i+1] > threshold) and (y[i+2] < threshold and y[i+3] < threshold)) and (y[i+4] > threshold and y[i+5] > threshold) and (y[i+6] < threshold and y[i+7] < threshold):
        alpha_helices.append((i,i+7))
      else:
         continue
    return alpha_helices

# Plot hydrophobicity profiles and identify secondary structures for each sequence
for i, sequence in enumerate(sequences, start=1):
    print(f"Sequence {i}:", sequence)
    plot_hydrophobicity_profile(sequence)
    beta_strands = identify_beta_strands(sequence)
    alpha_helices = identify_alpha_helices(sequence)
    print("Beta strands:", beta_strands)
    print("Alpha helices:", alpha_helices)
    plt.show()
