shifr = ("isfptitekthhcxatwbsipppdlmmweujgdtxhuaaxxxlelwegseedrzwegspxsfkjwawiljvotcxsxatjxcgxprwppevptsrxhwetjmwmfprwp"
         "hxttftptcgadprhimipxshhlrnesgwmlhtbgmmilbgxrnekswhufhpvwuigrigxrxuixilbvlexjxisaxqltifthadpedatchxmmliigriujx"
         "tqyksighmzwmgvlxsmieiwwmlqvnhltchipwlthbieedrzilxisibsliteprdgiitemthmwiheikpxbdrwxhbiezpmgrsfeekthmwibcwbvrb"
         "umvprmllbiippwathlivxpopxxailxuekgitrlbckvdrmxrxcxhuygllbiippwathytrvtegswtihhlrhcemgixqsqsmlrsngezthcxqvpqxh"
         "obetbckhjxtixatktiipxxapxbcttxptchlxrzxrzqyyueedktawugmgvmgvatiikuvhbxatxhlrijqiwewppppclqixcltiiyjppdvdxrmdq"
         "ltcxhfxusktfnirhlmmsmwcsmhxkxoxwmfhsatvxbifqikthmwemilxgippwvdqiprrpxmwiijqillbiifjptixhprwcizgsudclprwvmkawp"
         "tvxppppclilxgippmmxrzilxxvmjvghvxhxbckmgewxrzeptnxaxrzhunpvktpexrzumzwxbcklzcepvdxrzprwwiktqxbfxgiwiltieeilhj"
         "kailxeyfeathsgactwygsvxsegsjbuxrnekswhujcxqgtzxgkhiftropxxapfnroxisylemtvnchxgegwsngegsiotrmwighsftfhscztrxge"
         "eacaphmdkhpjmtvaxq")
alp = "abcdefghijklmnopqrstuvwxyz"
dict_alp = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j',
            'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't',
            'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
freq_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
           'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
dict_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
            'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
            'z': 25}
key = int(input("Enter key: "))
generator = [dict(freq_dict) for i in range(key)]
lens = [0] * key
for elem in range (len(shifr)):
    column_number = elem % key
    current_element = str(shifr[elem])
    if shifr[elem] == dict_alp[current_element]:
        generator[column_number][current_element] += 1
        lens[column_number] += 1
freq = [list(generator[elem].values()) for elem in range(key)]
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
    index_current = key_vizener[k]
    if key_vizener[k] == dict_alp[index_current]:
        key_vizener[k] = dict_num[index_current]
otvet = [""] * len(shifr)
start = 0
for k in range(len(shifr)):
    if start > (key - 1):
        start = 0
    index_current = shifr[k]
    for h in range(start, len(key_vizener)):
        digital_shifr = (dict_num[index_current] - key_vizener[h]) % 26
        index_current = digital_shifr
        if digital_shifr == index_current:
            otvet[k] = alp[index_current]
        start += 1
        break
print("Plain text: ", *otvet, sep="")
