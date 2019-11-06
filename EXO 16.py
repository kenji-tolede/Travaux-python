m1 = input('entrez 1er mot')
m2 = input('entrez le 2eme mot')

def hamming_distance(m1, m2):
    distance = 0
    for i in range(len(m1)):
        if m1[i] != m2[i]:
            distance += 1
    return distance


print(hamming_distance(m1,m2))