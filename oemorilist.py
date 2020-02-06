import csv

with open('easyodailist3.csv', 'r', encoding='shift_jis') as f:
    reader = csv.reader(f)
    tmp_list = []
    for row in reader:
        col = [x for x in row]
        # print(l)
        tmp_list.append(col)

with open('easyodailist_ryo.csv', 'r', encoding='shift_jis') as g:
    reader2 = csv.reader(g)
    tmp_list2 = []
    test = []

    for row2 in reader2:
        col2 = [x for x in row2]
        tmp_list2.append(col2)
        both = row2[0]
        for i, y in enumerate(tmp_list):
            if y[0] == both:
                tmp_list[i][3] = row2[3]
                test.append(tmp_list[i])

    print("[")
    for a in tmp_list:
        print(f"\t{a},")
    print("]")

