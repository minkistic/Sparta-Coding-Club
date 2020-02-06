a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(a)):
    print("***" + str(a[i]) + "단 출력 ***")
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(str(i) + '*' + str(j) + '=' + str(i * j))
        print("")


def f(hi):
    print(hi)


f('메롱')
