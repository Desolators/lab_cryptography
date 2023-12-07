from copy import deepcopy
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
alp = "abcdefghijklmnopqrstuvwxyz"
dict_alp = {'a': [0, 0], 'b': [0, 1], 'c': [0, 2], 'd': [0, 3], 'e': [0, 4], 'f': [0, 5], 'g': [0, 6], 'h': [0, 7],
            'i': [0, 8], 'j': [0, 9], 'k': [0, 10], 'l': [0, 11], 'm': [0, 12], 'n': [0, 13], 'o': [0, 14], 'p': [0, 15],
            'q': [0, 16], 'r': [0, 17], 's': [0, 18], 't': [0, 19], 'u': [0, 20], 'v': [0, 21], 'w': [0, 22],
            'x': [0, 23], 'y': [0, 24], 'z': [0, 25]}
key = int(input("Enter key: "))
list_of_nested_dictionaries = [deepcopy(dict_alp) for i in range(key)]
lens = [0] * key
for i in range(len(shifr)):
    column_number = i % key
    current_element = str(shifr[i])
    if shifr[i]:
        list_of_nested_dictionaries[column_number][current_element][0] += 1
        lens[column_number] += 1
freq = [list(list_of_nested_dictionaries[i].values()) for i in range(key)]
count_sdvig = [[0] for i in range(key - 1)]
umnoz_so_sdvigom = [[0] * len(dict_alp) for i in range(key)]
for k in range(len(umnoz_so_sdvigom) - 1):
    if k > (key - 1):
        k -= 1
    index = 0
    count = 0
    while index <= 0.059:
        tmp = freq[k + 1][len(dict_alp) - 1][0]
        for h in range(len(dict_alp) - 2, -1, -1):
            freq[k + 1][h + 1][0] = freq[k + 1][h][0]
        freq[k + 1][0][0] = tmp
        for i in range(len(dict_alp)):
            umnoz_so_sdvigom[k][i] = (freq[0][i][0] * freq[k + 1][i][0])
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
for k in range(len(dict_alp)):
    for h in range(len(count_sdvig)):
        x[h] = k - count_sdvig[h]
        y = x[h]
        if x[h]:
            x[h] = alp[y]
    print(k + 1, ".", *alp[k], *x)
key_vizener = input('Enter key: ').split()
for k in range(len(key_vizener)):
    current_element = key_vizener[k]
    if key_vizener[k]:
        key_vizener[k] = dict_alp[current_element][1]
otvet = [""] * len(shifr)
start = 0
for i in range(len(shifr)):
    if start > (key - 1):
        start = 0
    current_element = shifr[i]
    for j in range(start, len(key_vizener)):
        current_element = (dict_alp[current_element][1] - key_vizener[j]) % 26
        if current_element >= 0:
            otvet[i] = alp[current_element]
        start += 1
        break
print("Plain text: ", *otvet, sep="")
