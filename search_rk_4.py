abc={
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
q=13
T='cabcadcadbacadcbacacad'
P='baca'
T1=''
for i in T:
    s=str(i)
    T1+=str(abc[s])
P1=''
for x in P:
    P1+=x.replace(x,str(abc[x]))
comp1=int(P1)%13
counter=0
for z in range(len(T)-len(P)+1):
    comp2=T1[counter]+T1[counter+1]+T1[counter+2]+T1[counter+3]
    if int(comp2)%13==comp1:
        if P1==comp2:
            print(counter)
        else:
            pass
    counter+=1
