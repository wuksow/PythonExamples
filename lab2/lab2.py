#1

zakres = range(0, 5)

for elements in zakres:
    print(elements)

przerwa = ""

for elements in range(10):
    print(przerwa)


#2

num = 6

for elements in range(5):
    print(num)
    num = num + 6


for elements in range(10):
    print(przerwa)


#3


num1 = 52
for elements in range(5):
    num1 = num1 + 1
    print(num1)


for elements in range(10):
    print(przerwa)


#4
for elements in range(1, 8):
    if elements == 5:
        print("Znalazlem 5")
        continue
    print(elements)

for elements in range(10):
    print(przerwa)


#5
list = list(range(1,9))
liczba = 0
for elements in list:
    if liczba == 5:
        break
    print(list[liczba])
    liczba = liczba + 1

for elements in range(10):
    print(przerwa)


#6
liczby = range(20)

for elements in liczby:
    if elements % 3 == 0:
        print(elements)


for elements in range(10):
    print(przerwa)


#7
czas = 20

while czas >= 0:
    if czas == 0:
        print("Koniec odliczania!")
    else:
        print(czas)
    czas = czas-1

    for elements in range(10):
        print(przerwa)


#20.03.2022