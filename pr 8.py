temp=[-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,-5,-9,-10,-11]
ora=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
tempmedie=sum(temp)/24
print((sum(temp))/24)
maximultemp=max(temp)
print(max(temp))
minimtemp=min(temp)
print(min(temp))
tempmaximaora=[]
tempminimaora=[]
for i in range(len(ora)):
    if temp[i]==maximultemp:
        tempmaximaora.append(ora[i])
for i in range(len(ora)):
    if temp[i]==minimtemp:
        tempminimaora.append(ora[i])
print("Temperatura medie este:", tempmedie)
print("Maximul temp este:", maximultemp)
print("Minimul temp este:", minimtemp)
print("Ora cu temp maxima este:", tempmaximaora)
print("Ora cu temp minima este:", tempminimaora)