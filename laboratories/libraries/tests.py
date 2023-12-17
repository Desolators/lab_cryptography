stroka = (
    'ajtyjfhergeruylgsfdfweqfwwwwwwwwwwwwwwwwwwdsafcxbcvmjnyrfgjwhkegljewrpogk;ldkglfdjglkskd;lfkds;lfksd;'
    'lfk;lsdkfl;sdkfsdkfklklklklklklyywfadasffdhgfjlkyuityulrtfyghjkl;kojihugyftdrfghjkl;[ppoiutrewasxdfcgvhbjnkml;egd')
dict_count = {}
for elem in stroka:
    if elem not in dict_count:
        dict_count[elem] = 0
    dict_count[elem] += 1
a1, a2 = list(dict_count.values()), list(dict_count.keys())
print(f'{a2[a1.index(max(a1))]} = {max(a1)}')
