from copy import deepcopy
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
dict_alp = {'a': ['a', 0, 0], 'b': ['b', 0, 1], 'c': ['c', 0, 2], 'd': ['d', 0, 3], 'e': ['e', 0, 4], 'f': ['f', 0, 5],
            'g': ['g', 0, 6], 'h': ['h', 0, 7], 'i': ['i', 0, 8], 'j': ['j', 0, 9], 'k': ['k', 0, 10], 'l': ['l', 0, 11],
    'm': ['m', 0, 12], 'n': ['n', 0, 13], 'o': ['o', 0, 14], 'p': ['p', 0, 15], 'q': ['q', 0, 16], 'r': ['r', 0, 17],
    's': ['s', 0, 18], 't': ['t', 0, 19], 'u': ['u', 0, 20], 'v': ['v', 0, 21], 'w': ['w', 0, 22], 'x': ['x', 0, 23],
    'y': ['y', 0, 24], 'z': ['z', 0, 25]}
key = int(input("Enter key: "))
generator = [deepcopy(dict_alp) for i in range(key)]
lens = [0] * key
for elem in range (len(shifr)):
    column_number = elem % key
    current_element = str(shifr[elem])
    if shifr[elem] == dict_alp[current_element][0]:
        generator[column_number][current_element][1] += 1
        lens[column_number] += 1
freq = [list(generator[elem].values()) for elem in range(key)]
count_sdvig = [[0] for i in range(key - 1)]
umnoz_so_sdvigom = [[0] * len(dict_alp) for i in range(key)]
for k in range(len(umnoz_so_sdvigom) - 1):
    if k > (key - 1):
        k -= 1
    index = 0
    count = 0
    while index <= 0.059:
        tmp = freq[k + 1][len(dict_alp) - 1][1]
        for h in range(len(dict_alp) - 2, -1, -1):
            freq[k + 1][h + 1][1] = freq[k + 1][h][1]
        freq[k + 1][0][1] = tmp
        for i in range(len(dict_alp)):
            umnoz_so_sdvigom[k][i] = (freq[0][i][1] * freq[k + 1][i][1])
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
    index_current = key_vizener[k]
    if key_vizener[k] == dict_alp[index_current][0]:
        key_vizener[k] = dict_alp[index_current][2]
otvet = [""] * len(shifr)
start = 0
for k in range(len(shifr)):
    if start > (key - 1):
        start = 0
    index_current = shifr[k]
    for h in range(start, len(key_vizener)):
        digital_shifr = (dict_alp[index_current][2] - key_vizener[h]) % 26
        index_current = digital_shifr
        if digital_shifr == index_current:
            otvet[k] = alp[index_current]
        start += 1
        break
print("Plain text: ", *otvet, sep="")
