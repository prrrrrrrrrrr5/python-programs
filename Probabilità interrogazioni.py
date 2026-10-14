d={}
I=697
F=1040
y=0
for i in range(I,F+1):
    x=str(i)
    s=0
    for j in range(len(x)):
        s+=int(x[j])
    if s in d.keys():
        d[s]+=1
    else:
        if s<23:
            d.setdefault(s,1)

s=0
for i in d:
    s+=d[i]

D=dict(sorted(d.items()))

for i in D:
    x=(D[i]*100)/s
    D[i]=round(x,2)

print(D)
