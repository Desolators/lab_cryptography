shifr = (
    "wofuqmoxgsokucfvhhrntzhreccilccurihktfkzivvzhkwwtobuwwgklcqyxzritbhytpcplogtpzzvsvoehszrcrhytuwiaufviszytvouawhka"
    "shfqwhvpbrkdpfvpyoescbttkvvcufvphrvpfhyuszcdbhytzoesvs"
    "tdizucczfcusiefctjfsvksbupwzpqfsrsbcnlvsewshydiuyicjvghvzhpmexuvkxbvzhpsupbrkdggvsopfjhwewwgrclwvimvvvfcrcsrrcrgr"
    "xrhfwwgnxtsnwohzhhcstqcdtctlhvcnpfsnthcwtsrfjfdfdfqyx"
    "zritbkytbkvcczfcusiwojvpbmkwwbxtjseucffjfgvajsjxzzktzzpdikyphvlhpoesobjlsfvshvvlcarcsoiamhfbcfidkafgbwevksnxzzkp"
    "yskwsqyxzritbcliwbkdhvvucfvhhhflvsitwhzhhvvivwtzsgkivsitksnxzz"
    "cxuvkptwittciivsdpbrxxjsvpqvfuhvvbcbvbcfvewsttctsgsoupbrkwsbntkwcauckdciilcfbpbrctojvivsdpzcethvvnkwcabckuwbuivs"
    "npmvfbsoxpwbrcrkvhvocapsixrcwivsdcckzusgrxrhytaoexkwcabckschyp"
    "hvflqoexpsrghcctojvbmqyxzritbocdbszchvvucfvhhhytkwcsobzbozjlcicsgcfcqcdtobuisoiivsdicdztqsjdmcluccchowuhvskwsbnt"
    "aijiozcuciiswsfuvievsfpdiarnogntzzgaobvivsgaobbhtcidiftdttzcgo"
    "esgvvastkwwaeddsrrsieiwzytqcehsbktrpliwtvtzjvgmgfgfmwdfhytdcfgqvzarfvcozcivsjpasjpwrkwsarc")
key = int(input("Enter key: "))
alp = "abcdefghijklmnopqrstuvwxyz"
lens = [0] * key
freq = [[0] * len(alp) for i in range(key)]
for i in range(len(shifr)):
    column_number = i % key
    c = ord(shifr[i])
    index = c - ord('a')
    freq[column_number][index] += 1
    lens[column_number] += 1
count_sdvig = [[0] for i in range(key - 1)]
umnoz_so_sdvigom = [[0] * len(alp) for i in range(key)]
for k in range(len(umnoz_so_sdvigom) - 1):
    if k > (key - 1):
        k -= 1
    index = 0
    count = 0
    while index <= 0.059:
        tmp = freq[k + 1][len(alp) - 1]
        for h in range(len(alp) - 2, -1, -1):
            freq[k + 1][h + 1] = freq[k + 1][h]
        freq[k + 1][0] = tmp
        for i in range(len(alp)):
            umnoz_so_sdvigom[k][i] = (freq[0][i] * freq[k + 1][i])
        sum_sdvig = sum(umnoz_so_sdvigom[k])

        for j in range(len(lens)):
            if j > (key - 1):
                j -= 1
            index = sum_sdvig / (lens[0] * lens[j + 1])
            break
        count += 1
        count_sdvig[k] = count
        print("Sdvigi  :", count_sdvig[k])
        print("index sdviga : ", index)
print("Sdvigi final  : ", count_sdvig)
x = [[] for i in range(key - 1)]
for k in range(len(alp)):
    for h in range(len(count_sdvig)):
        x[h] = k - count_sdvig[h]
        y = x[h]
        if x[h]:
            x[h] = alp[y]
    print(k + 1, ".", *alp[k], *x)
key_vizener = input('Enter key: ').split()
for k in range(len(key_vizener)):
    index0 = ord(key_vizener[k])
    index_current = index0 - ord("a")
    if key_vizener[k] == alp[index_current]:
        key_vizener[k] = index_current
otvet = [""] * len(shifr)
start = 0
for k in range(len(shifr)):
    if start > (key - 1):
        start = 0
    index0 = ord(shifr[k])
    index_current = index0 - ord("a")
    for h in range(start, len(key_vizener), 1):
        digital_shifr = (index_current - key_vizener[h]) % 26
        index_current = digital_shifr
        if digital_shifr == index_current:
            otvet[k] = alp[index_current]
        start += 1
        break
print("Plain text: ", *otvet, sep="")
