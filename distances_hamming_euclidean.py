import numpy as np

def distances(Seq1, Seq2):
    sequence1 = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
               'I': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0,
               'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0}
    sequence2 = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
               'I': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0,
               'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0}

    for i in Seq1:
        sequence1[i] += 100 / len(Seq1)
    for j in Seq2:
        sequence2[j] += 100 / len(Seq2)

    hamming, euclidean = 0, 0
    
    for aa in sequence1:
        diff = sequence1[aa] - sequence2[aa]
        hamming += abs(diff)
        euclidean += diff ** 2
    hamming = hamming/100
    euclidean = np.sqrt(euclidean)
    
    return hamming, euclidean

Seq1 = 'AMENLNMDLLYMAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA'
Seq2 = 'AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI'
Seq3 = 'MALLPAAPGAPARATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA'

ham_12, euc_12 = distances(Seq1, Seq2)
ham_23, euc_23 = distances(Seq2, Seq3)
ham_31, euc_31 = distances(Seq3, Seq1)

print('Sequence Compared','\t', 'Hamming Distance','\t', 'Euclidean Distance')
print('Seq 1 and Seq 2','\t', ham_12,'\t', euc_12)
print('Seq 2 and Seq 3','\t', ham_23, '\t',euc_23)
print('Seq 3 and Seq 1','\t', ham_31,'\t', euc_31)
