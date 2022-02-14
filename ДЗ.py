#Test task
sp=[]
sp1=[]
len_array=int(input("Введи длину массива:" ))
print("Длина массива:", len_array)
for i in range(len_array):
    i=int(input("Введи число для массива:"))
    sp.append(i)
print("Наш массив:", sp)
for j in sp:
    sp1.append(abs(j))
a=max(sp1)
sp1.remove(a)
b=max(sp1)
sp1.remove(b)
c=max(sp1)
sp1.remove(c)
result=a*b*c
print("Результат:", result)
