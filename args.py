def summa(*sonlar):
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

a = 12
b = 14

print(summa(a, b))

