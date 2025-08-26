name="Jaadoo"
print(name)

for ch in name:
    print(ch)

le=len(name)

for i in range(0,le):
    print(i,"=",name[i])

for i in range(-le,0):
    print(i,"=",name[i])

n=-le
for i in range(0,le):
    print(i,"=",name[i],"=",n)
    n=n+1