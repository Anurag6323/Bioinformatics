human = 'MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH'
chicken = 'MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALARKYH'


arr = []
for i in range(len(human)-5):
    query = human[i:i+5]
    if query in chicken:
        arr.append([query, human.count(query), chicken.count(query)])

print('Pentapeptide | Frequency in Human | Frequency in Chicken ')
for a in arr:
    print(f'{a[0]} | {a[1]} | {a[2]}')


import blosum

def blsm62(seq1, seq2, matrix):
    score = 0
    m_score = 0
    for a, b in zip(seq1, seq2):
        if a == '-' or b == '-':
            score -= 2
        else:
            score += matrix[a][b]
            m_score += matrix[a][a]
    return ((score*100)/m_score)


human = 'MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH'
chicken = 'MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALARKYH'

match = gaps = 0

for a, b in zip(human, chicken):
    if a == b:
        match += 1
    elif a == '-' or b == '-':
        gaps += 1

identity = (match / len(human)) * 100
query_cov = ((len(human) - gaps) / len(human)) * 100
gap_per = (gaps / len(human)) * 100
similarity = blsm62(human, chicken, blosum.BLOSUM(62))

print(f' Identity = {identity}\n Query Coverage = {query_cov}\n Gap Percentage = {gap_per}\n Similarity (using BLOSUM62) = {similarity}')