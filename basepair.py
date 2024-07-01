def average_bs_energy(seq, energy_dict):
    total_energy = 0
    num_pairs = 0
    for i in range(len(seq)-1):
        pair = seq[i:i+2]
        if pair in energy_dict:
            total_energy += energy_dict[pair]
            num_pairs += 1
    if num_pairs == 0:
        return 0
    avg = total_energy / num_pairs
    return avg


sequence = "CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCATTG"
energy_dict = {'AA': -4, 'AT': -7, 'AC': -5, 'AG': -11,'TA': -7, 'TT': -2, 'TC': -3, 'TG': -4,'CA': -9, 'CT': -5, 'CC': -6, 'CG': -7,'GA': -9, 'GT': -6, 'GC': -4, 'GG': -11}

average_energy = average_bs_energy(sequence, energy_dict)

print("Average base stacking energy:", average_energy)
