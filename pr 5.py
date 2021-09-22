x=[1,2,3,4,5]
y=x
produsx=1
print('Suma primelor 3 componente ale lui x= ',x[0]+x[1]+x[2])
print('Suma componentelor variabilei y= ',sum(y))
for i in range(0,len(x)):
    produsx*=x[i]
print('Produsul componentelor variabilei x= ',produsx)
valabsolut3=abs(y[2])
print('Valoarea absoluta a componentei a 3-a a variabilei y= ',valabsolut3)
sumprimelorcomp=x[0]+y[0]
print('Suma primelor componente ale variabilelor x si y',sumprimelorcomp)