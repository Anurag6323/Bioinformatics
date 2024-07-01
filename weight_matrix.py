import math
import numpy as np
import pandas as pd
from collections import Counter

sequences = ["MVLSPADKTNVKGKVGAHAGEYGAAAW","MKRLPADPPCVKGKVKAKAGDYGATTW","MALSAADKTNVKSKVGGHAGEYGAATS","MVLSAADKTNVKSKAGGNAGEWWAAAW","MVLSAADKTNVKSKVLANAGEFGAAAW","ALLPIRTTYHKKCASGHIPEEKDLNNV","DEASSLKGHHIKKLEADALLIPLSASS"]

def check(column):
    counts = Counter(column)
    return [counts.get(aa, 0) for aa in "ACDEFGHIKLMNPQRSTVWY"]

weight_matrix = np.zeros((20, len(sequences[0])))

for i in range(len(sequences[0])):
    column = [sequence[i] for sequence in sequences]
    counts = check(column)
    for j in range(20):
        weight_matrix[j][i] = counts[j]

weight_matrix = np.log((weight_matrix + 0.05) / (0.05 * (len(sequences) + 1)))

# Create a DataFrame for visualization
amino_acids = list("ACDEFGHIKLMNPQRSTVWY")
positions = list(range(1, len(sequences[0]) + 1))
wt_matrix_df = pd.DataFrame(weight_matrix, index=amino_acids, columns=positions)

print(wt_matrix_df)