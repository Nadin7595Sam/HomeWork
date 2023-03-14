d1 = input('')
d2 = d1.split()

k = [sum(x in 'а' for x in k) for k in d2]
 
if len(k) == 1:
    res = "Пам парам"  
else:
    res = "Парам пам-пам"

print(d2)
print(k)
print(res)