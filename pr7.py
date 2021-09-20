Zile=['Luni','Marti','Miercuri','Joi','Vineri','Sambata','Duminica']
Venit=[950,780,1200,1000,670,1050,900]
venitulsapt=sum(Venit)
print(sum(Venit))
mediavenitsapt=sum(Venit)/7
print((sum(Venit))/7)
celmaimarevenitziua=max(Venit)
print(max(Venit))
celmaimicvenitziua=min(Venit)
print(min(Venit))
cmmarevenitzi=[]
cmmicvenitzi=[]
for i in range(len(Zile)):
    if Venit[i]==celmaimarevenitziua:
        cmmarevenitzi.extend(Zile[i])
for i in range(len(Zile)):
    if Venit[i]==celmaimicvenitziua:
        cmmicvenitzi.extend(Zile[i])

print("Venitul sapt este:", venitulsapt)
print("Media venitului sapt este:", mediavenitsapt)
print("Ziua cu cel mai mare venit este:", cmmarevenitzi)
print("Ziua cu cel mai mic venit este:", cmmicvenitzi)