Zile=['Luni','Marti','Miercuri','Joi','Vineri','Sambata','Duminica']
Venit=[950,780,1200,1000,670,1050,900]
print("Venitul saptamanal este:", sum(Venit))
print("Media venitului saptamanal este:", (sum(Venit))/7)
celmaimarevenitziua=max(Venit)
print("Cel mai mare venit este:",max(Venit))
celmaimicvenitziua=min(Venit)
print("Cel mai mic venit este:", min(Venit))
cmmarevenitzi=[]
cmmicvenitzi=[]
for i in range(len(Zile)):
    if Venit[i]==celmaimarevenitziua:
        cmmarevenitzi.append(Zile[i])
for i in range(len(Zile)):
    if Venit[i]==celmaimicvenitziua:
        cmmicvenitzi.append(Zile[i])
print("Ziua cu cel mai mare venit este:", cmmarevenitzi)
print("Ziua cu cel mai mic venit este:", cmmicvenitzi)