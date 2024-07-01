fasta_file = "uniref_transcription_factors_AND_ide_2024_03_04.fasta"
count = 0
with open(fasta_file, "r") as f:
    for line in f:
        if line.startswith(">"):
            count += 1
print("Total number of sequences:", count)