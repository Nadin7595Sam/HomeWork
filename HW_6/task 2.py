from random import randint

n = int(input('Введите количество элементов: '))
lst_1 = [randint(-10, 10) for i in range(n)]
print(lst_1)

maxim = int(input("Максимум = "))
minim = int(input("Минимум = "))

lst_2 = []

for i in range(n):
   if maxim >= lst_1[i] and minim <= lst_1[i]:
      lst_2.append(i)
print(lst_2)