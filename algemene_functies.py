def mijn_functie_1(a):
    a = a * a
    return a

print(mijn_functie_1(2))
print(mijn_functie_1(4))
print(mijn_functie_1(10))
print(mijn_functie_1(12))

def mijn_functie_2(a,b):
    list = []
    list.append(a+b)
    list.append(a-b)
    list.append(a*b)
    list.append(int(a/b))

    return list

print(mijn_functie_2(12,3))
print(mijn_functie_2(12,2))
print(mijn_functie_2(10,5))
print(mijn_functie_2(100,20))