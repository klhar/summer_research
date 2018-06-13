"""
Mathematical Model for addiction as described by Grasman et al
S = self control, quantified by variable U. 
C = state variable (undermines S); craving
E = societal measures (random Possion distribution)
A = addiction (frequency of addictive action), A = q*V
V = addiction vulnerability (V = 0 if C - S - E < 0 || V = 1 if C - S - E > 0), V = min(1, max(0, C - S - E))
lambda = impact of A on C

t = time, unit is week


constants
b = constant of proportionality of the impact of  A; 'cue sensitivity'
p = proportionality constant as a psychological resilience parameter
q = value of A that corresponds with an extremely high consumption level added over one week
d = unlearning parameter, 0 < d < 1
h
q

for specific case of alcohol addiction,
maximum capacity for S: maxS = 0.5
d = 0.2
b = 0.5
q = 0.8
p = 0.4
h/2 = k*q/2 = p*maxS/2, so
h = 0.2
k = 0.25

"""
import numpy as np 
import matplotlib.pyplot as plt 

#define constants
maxCapS = 0.5
d = 0.2
b = 0.5
h = 0.2
k = 0.25
q = 0.8
p = 0.4


def min(a, b):
    if a > b:
        return b
    return a

def max(a, b):
    if a > b:
        return a 
    return b 

# A(t) = q * V  + f(R(lambda(t));q)
def A(t):
    return q * min(1, max(0, (C(t) - S(t) - E(t))))

# C(t) = C(t-1) + b*min(1, 1 - C(t-1))*A(t - 1) - d * C(t-1), C(0)
listC = [0]
def C(t):
    if len(listC) > t:
        return listC[t]
    else:
        listC.append(C(t-1) + b * min(1, 1- C(t-1)) * A(t - 1) - d * C(t-1))
    return listC[t]

# S(t) = S(t-1) + p * max(0, maxCapS - S(t-1)) - h * C(t - 1) - k *A (t - 1),  S(0) = maxCapS
listS = [maxCapS]
def S(t):
    if len(listS) > t:
        return listS[t]
    else:
        listS.append(S(t-1) + p * max(0, maxCapS - S(t-1)) - h * C(t-1) - k * A(t-1))
    return listS[t]

#for lambda and E, let's just use equation (6) and assume lambda = 0.5 and E = 0 
def _lambda(t):
    return 0.5

def E(t):
    return 0

listA = []

for t in range(0,51):
    addiction =  A(t)
    listA.append(addiction)


print listA
print listC
print listS

axisT = np.linspace(0, 50, 51)
plt.plot(axisT, listS, 'green')
plt.plot(axisT, listA, 'red')
plt.plot(axisT, listC, 'orange')
plt.xlabel("Time (weeks)")
plt.show()
