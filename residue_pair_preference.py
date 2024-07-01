import pandas as pd

def compute_residue_matrix(sequence):
    residue_counts = {'A': 0, 'R': 0, 'N': 0, 'D': 0, 'E': 0, 'Q': 0, 'G': 0, 'H': 0, 'I': 0, 'L': 0, 
                      'K': 0, 'M': 0, 'F': 0, 'P': 0, 'S': 0, 'T': 0, 'W': 0, 'Y': 0, 'V': 0, 'C': 0}
    residue_pairs = {res1 + res2: 0 for res1 in residue_counts for res2 in residue_counts}
    
    # Count single residues and residue pairs
    for i in range(len(sequence)):
        residue_counts[sequence[i]] += 1
        if i < len(sequence) - 1:
            residue_pairs[sequence[i:i+2]] += 1
    
    # Initialize dictionaries to store preferences
    preferences = {'(a)': {}, '(b)': {}, '(c)': {}}
    
    # Compute preferences using the three given formulas
    for pair, count in residue_pairs.items():
        res1, res2 = pair[0], pair[1]
        total_count = residue_counts[res1] + residue_counts[res2]
        
        # Pair preference formula (a): [Nij*100/(Ni+Nj)]
        preferences['(a)'][pair] = (count * 100) / total_count if total_count != 0 else 0
        
        # Pair preference formula (b): [Nij*100/(N-1)]
        preferences['(b)'][pair] = (count * 100) / (len(sequence) - 1)
        
        # Pair preference formula (c): [Nij*100/(Ni*Nj)]
        preferences['(c)'][pair] = (count * 100) / (residue_counts[res1] * residue_counts[res2]) if residue_counts[res1] * residue_counts[res2] != 0 else 0
    
    return preferences

def print_top_10_preferred_residues(preferences):
    for pref_type, pref_name in preferences.items():
        sorted_preferences = sorted(pref_name, key=pref_name.get, reverse=True)
        print(f"\nTop 10 Preferred Residues for {pref_type}: {sorted_preferences[:10]}")

def main():
    sequences = []
    for i in range(3):
        sequence = input(f"Enter sequence {i + 1}: ").upper()
        sequences.append(sequence)
    
    for seq in sequences:
        print(f"\nMatrix for Sequence: {seq}")
        residue_preferences = compute_residue_matrix(seq)
        for pref_type, pref_name in residue_preferences.items():
            df = pd.DataFrame({pref_type: pref_name})
            print(df)
        print_top_10_preferred_residues(residue_preferences)

if __name__ == "__main__":
    main()
