import pandas as pd

seq = []
s = input("Enter the sequence :\n")
seq.append(s)

def matrix(s):
    for m in range(3):
        dict = {'A': [0, 0, 0], 'R': [0, 0, 0], 'N': [0, 0, 0], 'D': [0, 0, 0], 'E': [0, 0, 0], 
                'Q': [0, 0, 0], 'G': [0, 0, 0], 'H': [0, 0, 0], 'I': [0, 0, 0], 'L': [0, 0, 0], 
                'K': [0, 0, 0], 'M': [0, 0, 0], 'F': [0, 0, 0], 'P': [0, 0, 0], 'S': [0, 0, 0], 
                'T': [0, 0, 0], 'W': [0, 0, 0], 'Y': [0, 0, 0], 'V': [0, 0, 0], 'C': [0, 0, 0]}
        findex = []
        dict1 = {}
        for i in dict:
            findex.append(i)
        for i in dict:
            k = ""
            for j in dict:
                k = i + j
                dict1[k] = [0, 0, 0]

        dict2 = {}
        for j in s:
            if j in dict:
                dict[j][0] += 1
        k2 = ""
        for i in range(0, len(s) - 1):
            k2 = s[i] + s[i + 1]
            dict1[k2][0] += 1
            k2 = ""
        for i in dict1:
            dict2[i] = [0, 0, 0]
        if m == 0:
            for i in dict1:
                a = dict[i[0]][0]
                b = dict[i[1]][0]
                c = dict1[i][0]
                if a + b != 0:
                    dict2[i][0] = c * 100 / (a + b)
                else:
                    dict2[i][0] = 0

            ml = []
            p = []
            for i in dict2:
                ml.append(dict2[i][0])
            for i in ml:
                p.append(i)
            p.sort()
            print(p[-10:-1])
            mls = [[] for i in range(20)]
            for i in range(20):
                mls[i] = ml[0:20]
                ml = ml[20:]
            df = pd.DataFrame(mls, index=findex)
            print(df)
        if m == 1:
            for i in dict1:
                a = dict[i[0]][0]
                b = dict[i[1]][0]
                c = dict1[i][0]
                if a + b != 0:
                    dict2[i][0] = c * 100 / (len(s) - 1)
                else:
                    dict2[i][0] = 0
            ml = []
            for i in dict2:
                ml.append(dict2[i][0])
            for i in ml:
                p.append(i)
            p.sort()
            print(p[-10:-1])
            mls = [[] for i in range(20)]
            for i in range(20):
                mls[i] = ml[0:20]
                ml = ml[20:]
            df = pd.DataFrame(mls, index=findex)
            print(df)
        if m == 2:
            for i in dict1:
                a = dict[i[0]][0]
                b = dict[i[1]][0]
                c = dict1[i][0]
                if a * b != 0:
                    dict2[i][0] = c * 100 / (a * b)
                else:
                    dict2[i][0] = 0
            ml = []
            for i in dict2:
                ml.append(dict2[i][0])
            for i in ml:
                p.append(i)
            p.sort()
            print(p[-10:-1])
            mls = [[] for i in range(20)]
            for i in range(20):
                mls[i] = ml[0:20]
                ml = ml[20:]
            df = pd.DataFrame(mls, index=findex)
            print(df)

for i in range(3):
    matrix(seq[i])
