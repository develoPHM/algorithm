today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
priviacies = ["2021.05.02 A",
              "2021.07.01 B",
              "2022.02.19 C",
              "2022.02.20 C"]
today2 = today.split('.')
today = []
for c in today2:
    today.append(int(c))
terms_dic = {}
for c in terms:
    if c[0] not in terms_dic:
        terms_dic[c[0]] = 0
    terms_dic[c[0]] = int(c[2:])
for c in priviacies:
    print(c)