
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt

altx = [0,1,2,3]
alty = [0.60, 0.4667, 0.3333, 0.2]
E = 2000000
l = 3
b = 0.2
n = 30
h = 3/n
mult3 = []
mult2 = []
i = 1
c = 0
d = 0

def Func(x): 
    fH = 0.6-((0.4/3)*x)
    fI = ((((l-x)**2)/2)*(l-x))/((E*b*((fH)**3))/12)
    return fI

while i<30:
    if (i%3 == 0):
        mult2.append(i)
    if (i%3 != 0):
        mult3.append(i)
    i += 1
    
for j in range (len(mult3)):
    c += (Func((mult3[j])/10)) 

for k in range (len(mult2)):
    d += (Func((mult2[k])/10))

Res = ((3/8)*h)*(Func(0) + (3*c) + (2*d) + Func(3))

print ("Trabalho Referente à terceira nota da disciplina de Cálculo Numérico")
print ("Alunos: Caio Bertoldo, Carlos Henrique, Gabriel Lopes, Kevin Sanches")
print ("Exercício 9.7")
print ()
print ()
print ()
print ("Uma viga em balanço é carregada com uma carga uniformemente distribuiída de 1 t/m.")
print ("Dado um módulo de elasticidade do concreto de 2*10^6 t/m², o deslocamento vertical na extremidade em balanço pode ser dado como uma integral em x.")
print ()
print ("A altura da seção da viga segue uma reta, como:")

plt.plot(altx, alty)
plt.xlabel('Comprimento da Viga')
plt.ylabel('Altura da Seção')
plt.show()

print ("Portanto, pode-se definir a altura da seção da viga como a reta H = 0.6-0.133*x")

print ()
print ("Utilizando o método do 3/8 de Simpson, uma vez tendo obtido a equação que rege a altura da seção, utlizando 30 subintervalos para melhor aproximação do resultado real, obtêm-se o deslocamento vertical de ", format(Res, '5f'), "m.")
    

