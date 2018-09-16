
# coding: utf-8

# In[20]:


comp = []
comp0 = []
comp200 = []
volumes = []
pressoes = [1, 2, 5, 20, 40, 60, 80, 120, 140, 160, 180, 200]
temp = [273.15, 473.15]
P0 = 1
R = 0.082
Ao = 2.2769
Bo = 0.05587
a = 0.01855
b = -0.01587
c = 128300

def Pressure(T0, beta0, gama0, psi0, V0, P0):
    P = ((R*T0)/V0)+(beta0/(V0**2))+(gama0/(V0**3))+(psi0/(V0**4)) - P0
    return P

def Pressureder(T0, beta0, gama0, psi0, V0):
    P = ((-R*T0)/(V0**2))-((2*beta0)/(V0**3))-((3*gama0)/(V0**4))-((4*psi0)/(V0**5))
    return P

e = 0
k = 0
for i in range (12):
    for j in range (2):
        V0 = R*(temp[j])/(pressoes[i])
        beta = (R*(temp[j])*Bo)-Ao-((R*c)/((temp[j])**2))
        gama = (-R*(temp[j])*Bo*b)+(Ao*a)-((R*c*Bo)/((temp[j])**2))
        psi = (R*Bo*b*c)/((temp[j])**2)
        while (True):
            y = Pressure(temp[j], beta, gama, psi, V0, pressoes[i])
            yder = Pressureder(temp[j], beta, gama, psi,V0)
            Va = V0
            Vp= Va-(y/yder)
            e = abs((Vp-Va)/Vp)
            k += 1
            if (e<10**-6):
                volumes.append(Vp)
                break
            else:
                V0 = Vp

n=0               
for l in range (12):
    for m in range (2):
        print ("O volume do gás metano, com temperatura de", temp[m], "K e pressão de ", pressoes[l], " atm é: ", format(volumes[n], '6f'), " Litros por mol")
        n += 1

r = 0
for o in range (12):
    for q in range (2):
        z = (pressoes[o]*volumes[r])/(0.082*temp[q])
        comp.append(z)
        r += 1

u = 0
print()
for s in range (12):
    for t in range (2):
        print("O fator de compressibilidade do gás metano, com temperatura de", temp[t], "K e pressão de ", pressoes[s], " atm é: ", format(comp[u], '6f'))
        u += 1

d = 0
while (d<=22):
    comp0.append(comp[d])
    d += 2

f = 1
while (f<=23):
    comp200.append(comp[f])
    f += 2


    
print ()
print ("A curva, que representa o fator de compressibilidade em função da pressão, do gás metano a 273.15 Kelvin é: ")
plt.plot(pressoes, comp0)
plt.show()
print()
print ("A curva, que representa o fator de compressibilidade em função da pressão, do gás metano a 473.15 Kelvin é: ")
plt.plot(pressoes, comp200)
plt.show()
        

