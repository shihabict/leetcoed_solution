k = 'bcab'
li = []
x = len(k)
for i in range(0,x):
    li.append(k[i])

print("List is : ",li)


for i in range(0,x):
    for j in range(0,x):
        if li[i]<li[j]:
            temp = li[i]
            li[i]=li[j]
            li[j]=temp
j=""
print(li)

for i in range(0,x):
    j = j+li[i]

print("After sorting String is : ",j)