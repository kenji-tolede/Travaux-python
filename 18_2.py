code1="CATA"
code2="ATGC"
adnMoutarde="CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCADN"
adnRose="CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN"
adnPervenche="AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCCADN"
adnLeblanc="CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"
listesuspects = [adnMoutarde, adnRose, adnPervenche, adnLeblanc]
nomsuspects = ["Colonel Moutarde","Mme Rose", "Mme Pervenche", "M Leblanc"]
i = 0

while i < 4:
    if listesuspects[i].find("CATA") != -1 and listesuspects[i].find("ATGC") != -1 and (listesuspects[i].find("CATATGC") or listesuspects[i].find("ATGCA")) == -1:
        print("Le suspect est", nomsuspects[i])
        break
    else:
        i += 1

