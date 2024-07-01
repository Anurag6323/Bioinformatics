def calculate_propensity(seq, ss):
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
    composition = {aa: 0 for aa in amino_acids}
    helix_counts = {aa: 0 for aa in amino_acids}
    helix_total = 0
    for i in range(len(seq)):
        aa = seq[i]
        composition[aa] += 1
        if ss[i] == 'H':
            helix_counts[aa] += 1
            helix_total += 1

    propensity = {aa: helix_counts[aa] / composition[aa] * len(seq) / helix_total if composition[aa] != 0 else 0 for aa in amino_acids}
    print('Propensity:')
    for aa, value in propensity.items():
        print(f'{aa}\t:\t{value}')

seq = (
    "LGASGIAAFAFGSTAILIILFNMAAEVHFDPLQFFRQFFWLGLYPPKAQY"
    "GMGIPPLHDGGWWLMAGLFMTLSLGSWWIRVYSRARALGLGTHIAWNFAA"
    "AIFFVLCIGCIHPTLVGSWSEGVPFGIWPHIDWLTAFSIRYGNFYYCPWH"
    "GFSIGFAYGCGLLFAAHGATILAVARFGGDREIEQITDRGTAVERAALFW"
)
ss = (
    "XHHHHHHHHHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXX"
    "XXXXXXXXXXHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHXXHHHHHHHH"
    "HHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXHHH"
    "HHHHHHHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXX"
)
calculate_propensity(seq, ss)
