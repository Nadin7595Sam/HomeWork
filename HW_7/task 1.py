d1 = input('')
d2 = d1.split()

k = [sum(x in 'а' for x in k) for k in d2]
 
if len(set(k)) == 1:
    res = "Парам пам-пам"  
else:
    res = "Пам парам"

print(d2)
print(k)
print(res)