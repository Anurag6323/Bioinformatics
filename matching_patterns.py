import regex as re

pattern1 = "[SV]T[VT][DERK]{2}[^IL]"
pattern2 = "[FILV]Q...[^RK]G...[RK]..[FILVWY]"

file1 = open("Q4.fasta")
lines = file1.readlines()

print("Finding all matches for pattern 1:\n")
for i in range(1, len(lines)):
    if re.findall(pattern1, lines[i]):
        print(re.findall(pattern1, lines[i]), "in", "\n", lines[i-1].rstrip(), "\n", lines[i].rstrip(), '\n')

print("Finding all matches for pattern 2:\n")
for i in range(1, len(lines)):
    if re.findall(pattern2, lines[i]):
        print(re.findall(pattern2, lines[i]), "in", "\n", lines[i-1].rstrip(), "\n", lines[i].rstrip(), '\n')

file1.close()
