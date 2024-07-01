import matplotlib.pyplot as plt

chicken_hae = 'MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALARKYH'
human_hae = 'MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH'

plt.figure(figsize=(10, 10))
for i in range(len(human_hae)):
    for j in range(len(chicken_hae)):
        if human_hae[i] == chicken_hae[j]:
            plt.scatter(i, j, c='white')
        if j == 20:
            break
    if i == 20:
        break

plt.gca().set_facecolor('black')
plt.title("Dot Plot_Human vs Chicken Hemoglobin")
plt.xlabel("Human")
plt.ylabel("Chicken")
plt.show()

