temp=[-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,-5,-9,-10,-11]
ora=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
print("Temperatura medie este:",(sum(temp))/24)
maximultemp=max(temp)
print("Maximul de temperatura este:",max(temp))
minimtemp=min(temp)
print("Minimul de temperatura este:",min(temp))
tempmaximaora=[]
tempminimaora=[]
for i in range(len(ora)):
    if temp[i]==maximultemp:
        tempmaximaora.append(ora[i])
for i in range(len(ora)):
    if temp[i]==minimtemp:
        tempminimaora.append(ora[i])
print("Ora cu temp maxima este:", tempmaximaora)
print("Ora cu temp minima este:", tempminimaora)