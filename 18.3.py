N = int(input("введите количество билетов: "))
L = [input("введите возраст: ") for i in range(N)]

summa = 0

for i in range(N):
    if ((int(L[i]) >= 18) and (int(L[i]) < 25)):
        summa += 990
    if (int(L[i]) >= 25):
        summa += 1390

print("Стоимость билетов: ", summa)
if len(L) > 3:
    print("Стоимость со скидкой:", int(summa*0.9))