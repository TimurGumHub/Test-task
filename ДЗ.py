#Test task
sp=[]
list_of_ints=[-10,-10,1,3,2]
for i in list_of_ints:
    sp.append(abs(i))
a=max(sp)
sp.remove(a)
b=max(sp)
sp.remove(b)
c=max(sp)
sp.remove(c)
result=a*b*c
print(result)
